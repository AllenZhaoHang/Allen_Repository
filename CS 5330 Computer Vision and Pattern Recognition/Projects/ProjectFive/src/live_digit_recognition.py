#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Extension: Live Video Digit Recognition Application

import sys
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import cv2
import numpy as np

# Define the MyNetwork class (same as Task 1)
class MyNetwork(nn.Module):
    def __init__(self, num_classes=10):
        super(MyNetwork, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.dropout = nn.Dropout(0.25)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(20 * 4 * 4, 50)
        self.fc2 = nn.Linear(50, num_classes)

    def forward(self, x):
        x = self.pool1(torch.relu(self.conv1(x)))
        x = self.pool2(self.dropout(torch.relu(self.conv2(x))))
        x = x.view(-1, 20 * 4 * 4)
        x = torch.relu(self.fc1(x))
        return torch.log_softmax(self.fc2(x), dim=1)

# Function to preprocess frame for prediction
def preprocess_frame(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Resize to 28x28
    resized = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
    # Normalize and invert (MNIST digits are white on black)
    resized = cv2.bitwise_not(resized)  # Invert intensities
    resized = resized.astype(np.float32) / 255.0
    # Apply MNIST normalization
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    tensor = transform(resized).unsqueeze(0)  # Add batch dimension
    return tensor

# Main function
def main(argv):
    # Load the pre-trained model
    model = MyNetwork(num_classes=10)
    model.load_state_dict(torch.load("mynetwork.pth"))
    model.eval()
    print("Model loaded successfully.")

    # Open webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting live digit recognition. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Preprocess the frame
        input_tensor = preprocess_frame(frame)

        # Perform inference
        with torch.no_grad():
            output = model(input_tensor)
            _, predicted = torch.max(output, 1)
            predicted_digit = predicted.item()

        # Display the prediction on the frame
        cv2.putText(frame, f"Predicted Digit: {predicted_digit}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Live Digit Recognition", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print("Extension 6 completed: Live video digit recognition application closed.")

if __name__ == "__main__":
    main(sys.argv)