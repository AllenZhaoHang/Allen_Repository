#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Task 2A: Analyze and visualize the first layer filters of MyNetwork

# Import statements
import sys
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt

# Modified network class from Task 2A
class MyNetwork(nn.Module):
    """
    A modified convolutional neural network for MNIST digit recognition with three conv layers.
    """
    def __init__(self):
        super(MyNetwork, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.dropout = nn.Dropout(0.25)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.conv3 = nn.Conv2d(20, 40, kernel_size=3)
        self.pool3 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(40 * 1 * 1, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.pool2(self.dropout(F.relu(self.conv2(x))))
        x = self.pool3(F.relu(self.conv3(x)))
        x = x.view(-1, 40 * 1 * 1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

# Function to analyze and visualize the first layer filters
def analyze_first_layer():
    """
    Analyze the weights of the first convolutional layer and visualize the filters.
    """
    # Create an instance of the network
    model = MyNetwork()
    
    # Access the weights of the first layer (conv1)
    weights = model.conv1.weight  # Shape: [10, 1, 5, 5]
    
    # Print the shape and weights
    print("Shape of conv1 weights:", weights.shape)
    print("\nWeights of conv1 filters:")
    for i in range(10):
        filter_weights = weights[i, 0].detach().numpy()  # Shape: [5, 5]
        print(f"Filter {i}:\n{filter_weights}\n")
    
    # Visualize the 10 filters in a 3x4 grid
    fig, axes = plt.subplots(3, 4, figsize=(8, 6))
    fig.suptitle("First Layer Filters (conv1)", fontsize=12)
    
    for i in range(10):
        row = i // 4
        col = i % 4
        filter_weights = weights[i, 0].detach().numpy()
        axes[row, col].imshow(filter_weights, cmap='viridis')  # Use viridis colormap
        axes[row, col].set_title(f"Filter {i}")
        axes[row, col].set_xticks([])
        axes[row, col].set_yticks([])
    
    # Hide the last two subplots (empty)
    for i in range(10, 12):
        row = i // 4
        col = i % 4
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.savefig('conv1_filters.png')
    plt.show()

# Main function
def main(argv):
    """
    Main function to analyze and visualize the first layer filters.
    Args:
        argv: Command line arguments (not used)
    """
    analyze_first_layer()
    print("Task 2B completed: First layer filters visualized and saved as 'conv1_filters.png'.")

if __name__ == "__main__":
    main(sys.argv)