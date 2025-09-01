#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Task 1B: Build a convolutional neural network for MNIST digit recognition
# Import statements
import sys
import torch
import torch.nn as nn
import torch.nn.functional as F

# Neural network class definition
class MyNetwork(nn.Module):
    """
    A convolutional neural network for MNIST digit recognition.
    """
    def __init__(self):
        """
        Initialize the network layers.
        """
        super(MyNetwork, self).__init__()
        # Convolutional layer with 10 5x5 filters, 1 input channel (grayscale)
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        # Max pooling layer with 2x2 window
        self.pool1 = nn.MaxPool2d(2, 2)
        # Convolutional layer with 20 5x5 filters
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        # Dropout layer with 25% dropout rate
        self.dropout = nn.Dropout(0.25)
        # Max pooling layer with 2x2 window
        self.pool2 = nn.MaxPool2d(2, 2)
        # Fully connected layer with 50 nodes
        self.fc1 = nn.Linear(320, 50)
        # Final fully connected layer with 10 nodes (one per digit)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        """
        Define the forward pass of the network.
        Args:
            x: Input tensor of shape (batch_size, 1, 28, 28)
        Returns:
            Output tensor with log softmax applied
        """
        # First convolutional layer + ReLU + pooling
        x = self.pool1(F.relu(self.conv1(x)))
        # Second convolutional layer + ReLU + dropout + pooling
        x = self.pool2(self.dropout(F.relu(self.conv2(x))))
        # Flatten the tensor for fully connected layers
        x = x.view(-1, 320)  # 20 filters * 4 * 4 (after pooling)
        # First fully connected layer + ReLU
        x = F.relu(self.fc1(x))
        # Final fully connected layer + log softmax
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

# Function to instantiate and test the network
def test_network():
    """
    Create an instance of MyNetwork and test its structure with a dummy input.
    """
    # Create network instance
    model = MyNetwork()
    print("Network structure:")
    print(model)
    
    # Create a dummy input (batch_size=1, channels=1, height=28, width=28)
    dummy_input = torch.randn(1, 1, 28, 28)
    # Forward pass with dummy input
    output = model(dummy_input)
    print("\nOutput shape with dummy input:", output.shape)
    print("Sample output (log softmax values):", output[0].detach().numpy())

# Main function
def main(argv):
    """
    Main function to execute the network building and testing.
    Args:
        argv: Command line arguments (not used in this task)
    """
    # Test the network structure
    test_network()
    print("Task 1B completed: Network model built and tested.")

if __name__ == "__main__":
    main(sys.argv)