#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Task 1C: Train the MNIST recognition model and plot training/testing metrics

# Import statements
import sys
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import matplotlib.pyplot as plt

# Define the network class
class MyNetwork(nn.Module):
    """
    A convolutional neural network for MNIST digit recognition.
    """
    def __init__(self):
        super(MyNetwork, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.dropout = nn.Dropout(0.25)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = self.pool1(torch.relu(self.conv1(x)))
        x = self.pool2(self.dropout(torch.relu(self.conv2(x))))
        x = x.view(-1, 320)
        x = torch.relu(self.fc1(x))
        return torch.log_softmax(self.fc2(x), dim=1)

# Function to load MNIST data
def load_mnist_data(batch_size=64):
    """
    Load MNIST dataset with data loaders.
    Args:
        batch_size: Number of samples per batch
    Returns:
        train_loader: DataLoader for training set
        test_loader: DataLoader for test set
    """
    train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True,
                                               transform=torchvision.transforms.ToTensor())
    test_dataset = torchvision.datasets.MNIST(root='./data', train=False, download=True,
                                              transform=torchvision.transforms.ToTensor())
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    return train_loader, test_loader

# Function to evaluate the model
def evaluate_model(model, data_loader, criterion):
    """
    Evaluate the model on a dataset.
    Args:
        model: Trained network model
        data_loader: DataLoader for the dataset
        criterion: Loss function
    Returns:
        loss: Average loss
        accuracy: Accuracy percentage
    """
    model.eval()
    total_loss = 0
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in data_loader:
            outputs = model(images)
            total_loss += criterion(outputs, labels).item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    loss = total_loss / len(data_loader)
    accuracy = 100 * correct / total
    return loss, accuracy

# Function to train the model
def train_model(model, train_loader, test_loader, epochs=5):
    """
    Train the model and collect metrics.
    Args:
        model: Network model to train
        train_loader: DataLoader for training set
        test_loader: DataLoader for test set
        epochs: Number of training epochs
    Returns:
        metrics: Dictionary with training and testing losses and accuracies
    """
    criterion = nn.NLLLoss()  # Negative log likelihood loss for log softmax
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    
    train_losses, test_losses = [], []
    train_accuracies, test_accuracies = [], []
    
    for epoch in range(epochs):
        model.train()
        running_loss = 0
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        
        # Evaluate after each epoch
        train_loss, train_acc = evaluate_model(model, train_loader, criterion)
        test_loss, test_acc = evaluate_model(model, test_loader, criterion)
        
        train_losses.append(train_loss)
        test_losses.append(test_loss)
        train_accuracies.append(train_acc)
        test_accuracies.append(test_acc)
        
        print(f"Epoch {epoch+1}/{epochs} - Train Loss: {train_loss:.4f}, Test Loss: {test_loss:.4f}, "
              f"Train Acc: {train_acc:.2f}%, Test Acc: {test_acc:.2f}%")
    
    return {"train_losses": train_losses, "test_losses": test_losses,
            "train_accuracies": train_accuracies, "test_accuracies": test_accuracies}

# Function to plot metrics
def plot_metrics(metrics):
    """
    Plot training and testing losses and accuracies.
    Args:
        metrics: Dictionary containing loss and accuracy lists
    """
    epochs = range(1, len(metrics["train_losses"]) + 1)
    
    # Plot losses
    plt.figure(figsize=(10, 5))
    plt.plot(epochs, metrics["train_losses"], 'b-', label='Training Loss')
    plt.plot(epochs, metrics["test_losses"], 'r-', label='Testing Loss')
    plt.title('Training and Testing Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.savefig('loss_plot.png')
    plt.show()
    
    # Plot accuracies
    plt.figure(figsize=(10, 5))
    plt.plot(epochs, metrics["train_accuracies"], 'b-', label='Training Accuracy')
    plt.plot(epochs, metrics["test_accuracies"], 'r-', label='Testing Accuracy')
    plt.title('Training and Testing Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy (%)')
    plt.legend()
    plt.grid(True)
    plt.savefig('accuracy_plot.png')
    plt.show()

# Main function
def main(argv):
    """
    Main function to train the model and plot results.
    Args:
        argv: Command line arguments (not used)
    """
    # Initialize model and data
    model = MyNetwork()
    train_loader, test_loader = load_mnist_data(batch_size=64)
    
    # Train the model and collect metrics
    metrics = train_model(model, train_loader, test_loader, epochs=5)
    
    # Plot the results
    plot_metrics(metrics)
    print("Training completed. Plots saved as 'loss_plot.png' and 'accuracy_plot.png'.")

if __name__ == "__main__":
    main(sys.argv)