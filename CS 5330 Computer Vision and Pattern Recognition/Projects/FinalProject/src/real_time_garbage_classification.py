#!/usr/bin/env python3
# Hang Zhao
# Date: March 30, 2025
# Project: Real-Time Garbage Classification Using Webcam

import sys
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import cv2
import numpy as np

# Lightweight CNN Model (same as in training script)
class LightweightCNN(nn.Module):
    def __init__(self, num_classes=3):
        super(LightweightCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 8, kernel_size=3, padding=1)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(8, 16, kernel_size=3, padding=1)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(0.25)
        self.fc1 = nn.Linear(16 * 16 * 16, 64)
        self.fc2 = nn.Linear(64, num_classes)

    def forward(self, x):
        x = self.pool1(torch.relu(self.conv1(x)))
        x = self.pool2(torch.relu(self.conv2(x)))
        x = self.dropout(x)
        x = x.view(-1, 16 * 16 * 16)
        x = torch.relu(self.fc1(x))
        return torch.log_softmax(self.fc2(x), dim=1)

# Preprocess frame for prediction
def preprocess_frame(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Threshold to binarize (assuming dark object on light background)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    # Find contours to locate the object
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Get the largest contour (assumed to be the garbage)
        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)
        # Extract the object region
        object_img = gray[y:y+h, x:x+w]
        # Resize to 64x64
        object_img = cv2.resize(object_img, (64, 64), interpolation=cv2.INTER_AREA)
        # Normalize
        object_img = object_img.astype(np.float32) / 255.0
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])
        tensor = transform(object_img).unsqueeze(0)  # Add batch dimension
        return tensor, True
    return None, False

# Main function
def main(argv):
    # Load the trained model
    model = LightweightCNN(num_classes=3)
    model.load_state_dict(torch.load("garbage_classifier.pth"))
    model.eval()
    print("Model loaded successfully.")

    # Open webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    classes = ['Recyclable', 'Wet', 'Dry']
    print("Starting real-time garbage classification. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Preprocess the frame
        input_tensor, object_found = preprocess_frame(frame)

        # Perform inference if an object is found
        if object_found:
            with torch.no_grad():
                output = model(input_tensor)
                _, predicted = torch.max(output, 1)
                predicted_class = classes[predicted.item()]
            # Display the prediction on the frame
            cv2.putText(frame, f"Class: {predicted_class}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "No Object Detected", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Real-Time Garbage Classification", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print("Real-time garbage classification application closed.")

if __name__ == "__main__":
    main(sys.argv)