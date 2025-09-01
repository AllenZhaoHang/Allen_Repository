#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Task 3: Transfer learning on Greek letters dataset using MyNetwork

# Import statements
import sys
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to avoid GUI issues
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

# MyNetwork class from Task 1 (without conv3)
class MyNetwork(nn.Module):
    """
    A convolutional neural network for MNIST digit recognition (Task 1 version).
    """
    def __init__(self, num_classes=10):
        super(MyNetwork, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.dropout = nn.Dropout(0.25)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(20 * 4 * 4, 50)  # 20 channels, 4x4 spatial dimension
        self.fc2 = nn.Linear(50, num_classes)

    def forward(self, x):
        x = self.pool1(torch.relu(self.conv1(x)))
        x = self.pool2(self.dropout(torch.relu(self.conv2(x))))
        x = x.view(-1, 20 * 4 * 4)
        x = torch.relu(self.fc1(x))
        return torch.log_softmax(self.fc2(x), dim=1)

# GreekTransform class for preprocessing Greek letter images
class GreekTransform:
    """
    Transform to convert Greek letter images to MNIST-like format.
    """
    def __init__(self):
        pass

    def __call__(self, x):
        x = torchvision.transforms.functional.rgb_to_grayscale(x)
        x = torchvision.transforms.functional.affine(x, 0, (0, 0), 36/128, 0)
        x = torchvision.transforms.functional.center_crop(x, (28, 28))
        return torchvision.transforms.functional.invert(x)

# Function to load Greek letters dataset using ImageFolder
def load_greek_data(training_set_path, test_set_path, batch_size=5):
    """
    Load Greek letters dataset with data loaders.
    Args:
        training_set_path: Path to training set directory
        test_set_path: Path to test set directory
        batch_size: Number of samples per batch
    Returns:
        train_loader, test_loader: DataLoaders for training and test sets
    """
    transform = transforms.Compose([
        transforms.ToTensor(),
        GreekTransform(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    train_dataset = torchvision.datasets.ImageFolder(training_set_path, transform=transform)
    test_dataset = torchvision.datasets.ImageFolder(test_set_path, transform=transform)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, test_loader

# Function to load and modify the pre-trained model
def load_and_modify_pretrained_model(filename="mynetwork.pth", num_classes=3):
    """
    Load the pre-trained model, freeze weights, and replace the last layer.
    Args:
        filename: Path to the pre-trained model weights
        num_classes: Number of classes for the new task (3 for alpha, beta, gamma)
    Returns:
        model: Modified pre-trained model
    """
    # Load the pre-trained model
    model = MyNetwork(num_classes=10)  # Original MNIST model with 10 classes
    model.load_state_dict(torch.load(filename))
    
    # Freeze all weights
    for param in model.parameters():
        param.requires_grad = False
    
    # Replace the last layer (fc2) with a new Linear layer for 3 classes
    model.fc2 = nn.Linear(50, num_classes)
    
    return model

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
    Fine-tune the model on the Greek letters dataset (only the last layer).
    Args:
        model: Pre-trained model with frozen weights
        train_loader: DataLoader for training set
        test_loader: DataLoader for test set
        epochs: Number of training epochs
    Returns:
        metrics: Dictionary with training and testing losses and accuracies
    """
    criterion = nn.NLLLoss()
    # Only optimize the last layer (fc2) since others are frozen
    optimizer = optim.SGD(filter(lambda p: p.requires_grad, model.parameters()), lr=0.001, momentum=0.9)
    
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

# Function to save network structure to a file
def save_network_structure(model, filename="network_structure.txt"):
    """
    Save the network structure to a file.
    Args:
        model: The neural network model
        filename: Output file name
    """
    with open(filename, 'w') as f:
        f.write("Modified Model for Greek Letters:\n")
        f.write(str(model))
        f.write("\n")

# Function to save test results to a file
def save_test_results(metrics, filename="greek_test_results.txt"):
    """
    Save the test results to a file.
    Args:
        metrics: Dictionary containing loss and accuracy lists
        filename: Output file name
    """
    with open(filename, 'w') as f:
        f.write("Test Results on Greek Letters Dataset:\n")
        for epoch in range(len(metrics["test_losses"])):
            f.write(f"Epoch {epoch+1} - Test Loss: {metrics['test_losses'][epoch]:.4f}, "
                    f"Test Acc: {metrics['test_accuracies'][epoch]:.2f}%\n")

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
    plt.title('Training and Testing Loss (Greek Letters)')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.savefig('greek_loss_plot.png')
    plt.close()  # Close the figure to free memory
    
    # Plot accuracies
    plt.figure(figsize=(10, 5))
    plt.plot(epochs, metrics["train_accuracies"], 'b-', label='Training Accuracy')
    plt.plot(epochs, metrics["test_accuracies"], 'r-', label='Testing Accuracy')
    plt.title('Training and Testing Accuracy (Greek Letters)')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy (%)')
    plt.legend()
    plt.grid(True)
    plt.savefig('greek_accuracy_plot.png')
    plt.close()  # Close the figure to free memory

# Main function
def main(argv):
    """
    Main function to perform transfer learning on Greek letters dataset.
    Args:
        argv: Command line arguments (not used)
    """
    # Define paths to Greek letters dataset
    training_set_path = './greek_letters/train'
    test_set_path = './greek_letters/test'
    
    # Load Greek letters dataset
    train_loader, test_loader = load_greek_data(training_set_path, test_set_path, batch_size=5)
    
    # Load and modify pre-trained model
    model = load_and_modify_pretrained_model(filename="mynetwork.pth", num_classes=3)
    print("Modified Model for Greek Letters:")
    print(model)
    save_network_structure(model, "network_structure.txt")  # Save network structure
    
    # Fine-tune the model (only the last layer)
    print("Starting fine-tuning on Greek letters dataset...")
    metrics = train_model(model, train_loader, test_loader, epochs=5)
    
    # Save test results
    save_test_results(metrics, "greek_test_results.txt")
    
    # Plot the results
    plot_metrics(metrics)
    print("Task 3 completed: Plots saved as 'greek_loss_plot.png' and 'greek_accuracy_plot.png'. "
          "Network structure saved as 'network_structure.txt'. Test results saved as 'greek_test_results.txt'.")

if __name__ == "__main__":
    main(sys.argv)