#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Task 2B: Apply conv1 filters to the first training image and visualize results

# Import statements
import sys
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import matplotlib.pyplot as plt
import cv2
import numpy as np

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

# Function to load the first training image
def load_first_training_image():
    """
    Load the first image from the MNIST training set.
    Returns:
        image: First training image as a numpy array
    """
    train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True,
                                               transform=torchvision.transforms.ToTensor())
    image, _ = train_dataset[0]  # Shape: [1, 28, 28]
    image = image.squeeze().numpy()  # Shape: [28, 28]
    return image

# Function to apply filters and visualize results
def apply_and_visualize_filters():
    """
    Apply the conv1 filters to the first training image and visualize the results.
    """
    # Create an instance of the network
    model = MyNetwork()
    
    # Load the first training image
    image = load_first_training_image()
    
    # Get the weights of conv1
    with torch.no_grad():
        weights = model.conv1.weight  # Shape: [10, 1, 5, 5]
    
    # Apply each filter to the image using OpenCV's filter2D
    filtered_images = []
    for i in range(10):
        # Detach the tensor to remove gradient tracking before converting to numpy
        filter_weights = weights[i, 0].detach().numpy()  # Shape: [5, 5]
        # Apply filter2D (image must be float32 for OpenCV)
        filtered = cv2.filter2D(image, -1, filter_weights)
        filtered_images.append(filtered)
    
    # Visualize the filtered images in a 5x2 grid
    fig, axes = plt.subplots(5, 2, figsize=(4, 10))
    fig.suptitle("Filtered Images (First Training Sample)", fontsize=12)
    
    for i in range(10):
        row = i // 2
        col = i % 2
        axes[row, col].imshow(filtered_images[i], cmap='gray')
        axes[row, col].set_title(f"Filter {i}")
        axes[row, col].set_xticks([])
        axes[row, col].set_yticks([])
    
    plt.tight_layout()
    plt.savefig('filtered_images.png')
    plt.show()

# Main function
def main(argv):
    """
    Main function to apply conv1 filters and visualize results.
    Args:
        argv: Command line arguments (not used)
    """
    apply_and_visualize_filters()
    print("Task 2B completed: Filtered images saved as 'filtered_images.png'.")

if __name__ == "__main__":
    main(sys.argv)