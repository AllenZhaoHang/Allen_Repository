#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Task 1F: Test the trained model on handwritten digit images

# Import statements
import sys
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
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
    model.eval()
    return model

# Function to process and predict handwritten digits
def process_and_predict(model, image_paths):
    """
    Process handwritten digit images and predict their labels.
    Args:
        model: Loaded network model
        image_paths: List of paths to handwritten digit images (0-9)
    Returns:
        predictions: List of predicted labels
        images: List of processed images
    """
    transform = transforms.Compose([
        transforms.Grayscale(),          # Convert to grayscale
        transforms.Resize((28, 28)),     # Resize to 28x28
        transforms.ToTensor(),           # Convert to tensor
        transforms.Normalize((0.5,), (0.5,))  # Normalize to match MNIST
    ])
    
    predictions = []
    images = []
    
    for path in image_paths:
        # Load and process image
        img = Image.open(path)
        img_tensor = transform(img)
        
        # Invert if necessary (MNIST is white digits on black background)
        if img_tensor.mean() > 0:  # If mean > 0, likely black on white
            img_tensor = 1 - img_tensor  # Invert intensities
        
        # Add batch dimension and predict
        img_tensor = img_tensor.unsqueeze(0)  # Shape: [1, 1, 28, 28]
        with torch.no_grad():
            output = model(img_tensor)
            _, pred = torch.max(output, 1)
            predictions.append(pred.item())
            images.append(img_tensor.squeeze(0))  # Remove batch dim for plotting
    
    return predictions, images

# Function to plot results
def plot_results(images, predictions):
    """
    Plot the handwritten digits with their predicted labels.
    Args:
        images: List of processed image tensors
        predictions: List of predicted labels
    """
    fig, axes = plt.subplots(2, 5, figsize=(10, 4))
    fig.suptitle("Handwritten Digits with Predictions", fontsize=12)
    
    for i, (img, pred) in enumerate(zip(images, predictions)):
        row = i // 5
        col = i % 5
        axes[row, col].imshow(img.squeeze(), cmap='gray')
        axes[row, col].set_title(f"Pred: {pred}")
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.savefig('handwritten_results.png')
    plt.show()

# Main function
def main(argv):
    """
    Main function to test the model on handwritten digits.
    Args:
        argv: Command line arguments (not used)
    """
    # Load the trained model
    model = load_model("mynetwork.pth")
    
    # List of handwritten digit image paths (replace with your actual paths)
    image_paths = [
        "digit_0.jpg", "digit_1.jpg", "digit_2.jpg", "digit_3.jpg", "digit_4.jpg",
        "digit_5.jpg", "digit_6.jpg", "digit_7.jpg", "digit_8.jpg", "digit_9.jpg"
    ]
    
    # Process images and predict
    print("Processing handwritten digits...")
    predictions, images = process_and_predict(model, image_paths)
    
    # Print predictions
    for i, pred in enumerate(predictions):
        print(f"Digit {i}: Predicted label = {pred}")
    
    # Plot results
    plot_results(images, predictions)
    print("Task 1F completed: Results saved as 'handwritten_results.png'.")

if __name__ == "__main__":
    main(sys.argv)