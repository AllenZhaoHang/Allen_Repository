#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Task 1E: Load the trained model, evaluate on the first 10 test samples, and save results as CSV

# Import statements
import sys
import torch
import torch.nn as nn
import torchvision
import matplotlib.pyplot as plt
import csv

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

# Function to load the test dataset
def load_test_data(batch_size=10):
    """
    Load the MNIST test dataset.
    Args:
        batch_size: Number of samples per batch
    Returns:
        test_loader: DataLoader for test set
    """
    test_dataset = torchvision.datasets.MNIST(root='./data', train=False, download=True,
                                              transform=torchvision.transforms.ToTensor())
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    return test_loader

# Function to load the trained model
def load_model(filename="mynetwork.pth"):
    """
    Load the trained model from a file.
    Args:
        filename: Name of the file containing the model weights
    Returns:
        model: Loaded network model
    """
    model = MyNetwork()
    model.load_state_dict(torch.load(filename))
    model.eval()  # Set to evaluation mode
    return model

# Function to evaluate, print, and save results as CSV
def evaluate_and_print(model, test_loader):
    """
    Evaluate the model on the first 10 test samples, print results, and save as CSV.
    Args:
        model: Loaded network model
        test_loader: DataLoader for test set
    Returns:
        images: First batch of test images
        labels: Correct labels
        predictions: Predicted labels
    """
    with torch.no_grad():
        # Get the first batch (10 samples)
        images, labels = next(iter(test_loader))
        outputs = model(images)
        _, predictions = torch.max(outputs, 1)
        
        # Prepare CSV data
        csv_data = []
        header = ["Sample", "Output_0", "Output_1", "Output_2", "Output_3", "Output_4",
                  "Output_5", "Output_6", "Output_7", "Output_8", "Output_9",
                  "Predicted_Label", "True_Label"]
        csv_data.append(header)
        
        # Print and collect results
        for i in range(10):
            output_values = outputs[i].numpy().round(2)  # Round to 2 decimal places
            pred = predictions[i].item()
            true_label = labels[i].item()
            print(f"Sample {i+1}:")
            print(f"Output values: {output_values}")
            print(f"Predicted label: {pred}, True label: {true_label}")
            print()
            
            # Add row to CSV data
            row = [i+1] + output_values.tolist() + [pred, true_label]
            csv_data.append(row)
        
        # Save to CSV file
        with open("test_results.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)
        
        return images, labels, predictions

# Function to plot the first 9 samples
def plot_samples(images, predictions):
    """
    Plot the first 9 test samples with their predicted labels in a 3x3 grid.
    Args:
        images: Tensor of test images
        predictions: Predicted labels
    """
    fig, axes = plt.subplots(3, 3, figsize=(6, 6))
    fig.suptitle("First 9 Test Samples with Predictions", fontsize=12)
    
    for i in range(9):
        row = i // 3
        col = i % 3
        axes[row, col].imshow(images[i].squeeze(), cmap='gray')
        axes[row, col].set_title(f"Pred: {predictions[i].item()}")
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.savefig('test_samples_plot.png')
    plt.show()

# Main function
def main(argv):
    """
    Main function to load the model, evaluate, and save results.
    Args:
        argv: Command line arguments (not used)
    """
    # Load test data and model
    test_loader = load_test_data(batch_size=10)
    model = load_model("mynetwork.pth")
    
    # Evaluate and print results
    print("Evaluating the first 10 test samples:")
    images, labels, predictions = evaluate_and_print(model, test_loader)
    
    # Plot the first 9 samples
    plot_samples(images, predictions)
    print("Task 1E completed: Results printed, saved as 'test_results.csv', "
          "plot saved as 'test_samples_plot.png'.")

if __name__ == "__main__":
    main(sys.argv)