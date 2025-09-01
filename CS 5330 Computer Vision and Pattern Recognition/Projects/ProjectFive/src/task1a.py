#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Task 1A: Load MNIST dataset and visualize the first six test samples

# Import statements
import sys
import torch
import torchvision
import matplotlib.pyplot as plt

# Function to load MNIST dataset
def load_mnist_data():
    """
    Load the MNIST dataset for training and testing.
    Returns:
        train_dataset: Training dataset object
        test_dataset: Test dataset object
    """
    train_dataset = torchvision.datasets.MNIST(root='./data', train=True, 
                                               download=True, transform=torchvision.transforms.ToTensor())
    test_dataset = torchvision.datasets.MNIST(root='./data', train=False, 
                                              download=True, transform=torchvision.transforms.ToTensor())
    return train_dataset, test_dataset

# Function to visualize the first six test samples
def visualize_test_samples(test_dataset):
    """
    Visualize the first six samples from the test dataset in a 2x3 grid.
    Args:
        test_dataset: Test dataset object containing MNIST images and labels
    """
    # Create a 2x3 subplot grid
    fig, axes = plt.subplots(2, 3, figsize=(8, 5))
    fig.suptitle('First Six MNIST Test Samples', fontsize=16)

    # Display the first six test samples
    for i in range(6):
        image, label = test_dataset[i]  # Get image and label
        row = i // 3  # Calculate row index
        col = i % 3   # Calculate column index
        axes[row, col].imshow(image.squeeze(), cmap='gray')  # Display grayscale image
        axes[row, col].set_title(f'Label: {label}')          # Set title as label
        axes[row, col].axis('off')                          # Turn off axes
    
    plt.tight_layout()
    plt.savefig('first_six_test_samples.png')  # Save the plot to a file
    plt.show()

# Main function
def main(argv):
    """
    Main function to execute the MNIST loading and visualization.
    Args:
        argv: Command line arguments (not used in this task)
    """
    # Load MNIST dataset
    train_dataset, test_dataset = load_mnist_data()
    
    # Visualize the first six test samples
    visualize_test_samples(test_dataset)
    print("Visualization of the first six test samples completed.")

if __name__ == "__main__":
    main(sys.argv)