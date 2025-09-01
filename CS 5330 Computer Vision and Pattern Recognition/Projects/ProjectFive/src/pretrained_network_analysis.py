#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Extension: Analyze Pre-trained Network Convolutional Layers

import sys
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Load MNIST dataset
def load_mnist():
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    test_dataset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    return test_dataset

# Load pre-trained ResNet18 and modify for MNIST
def load_pretrained_resnet():
    # Use weights instead of deprecated pretrained parameter
    model = torchvision.models.resnet18(weights=torchvision.models.ResNet18_Weights.IMAGENET1K_V1)
    # Modify the first layer to accept 1-channel input (MNIST)
    model.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)
    return model

# Function to visualize filters
def plot_filters(filters, filename, title):
    plt.figure(figsize=(10, 5))
    for i in range(min(12, filters.shape[0])):  # Show first 12 filters
        plt.subplot(3, 4, i+1)
        plt.imshow(filters[i, 0], cmap='gray')
        plt.title(f'Filter {i+1}')
        plt.xticks([])
        plt.yticks([])
    plt.suptitle(title)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(filename)
    plt.close()

# Function to apply filters to an image
def apply_filters(image, filters, filename):
    plt.figure(figsize=(10, 5))
    for i in range(min(12, filters.shape[0])):  # Show first 12 filtered images
        with torch.no_grad():
            filter_kernel = filters[i, 0].numpy()
            # Image is already a NumPy array, no need to call .numpy() again
            filtered = cv2.filter2D(image, -1, filter_kernel)
        plt.subplot(3, 4, i+1)
        plt.imshow(filtered, cmap='gray')
        plt.title(f'Filtered {i+1}')
        plt.xticks([])
        plt.yticks([])
    plt.suptitle('Filtered Images Using ResNet18 Conv1 Filters')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(filename)
    plt.close()

# Main function
def main(argv):
    # Load MNIST test dataset
    test_dataset = load_mnist()
    image, _ = test_dataset[0]  # First test image
    image = image.numpy()[0]  # Shape: 28x28, already a NumPy array

    # Load pre-trained ResNet18
    model = load_pretrained_resnet()
    model.eval()

    # Extract weights of the first convolutional layer
    conv1_weights = model.conv1.weight.data  # Shape: [64, 1, 7, 7]
    print(f"Conv1 weights shape: {conv1_weights.shape}")

    # Plot the first 12 filters
    plot_filters(conv1_weights, 'resnet18_conv1_filters.png', 'ResNet18 Conv1 Filters')

    # Apply the first 12 filters to the first test image
    apply_filters(image, conv1_weights, 'resnet18_filtered_images.png')

    print("Extension 4 completed: Plots saved as 'resnet18_conv1_filters.png' and 'resnet18_filtered_images.png'.")

if __name__ == "__main__":
    main(sys.argv)