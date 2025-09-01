#!/usr/bin/env python3
# Hang Zhao
# Date: March 30, 2025
# Project: Train Lightweight CNN for Real-Time Garbage Classification

import sys
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, Dataset
import os
import time
# Custom Dataset for Garbage Classification
class GarbageDataset(Dataset):
    def __init__(self, image_dir, transform=None):
        self.image_dir = image_dir
        self.transform = transform
        self.classes = ['recyclable', 'wet', 'dry']  # 3 categories
        self.image_paths = []
        self.labels = []
        for idx, cls in enumerate(self.classes):
            cls_dir = os.path.join(self.image_dir, cls)
            for img_name in os.listdir(cls_dir):
                if img_name.endswith('.jpg'):
                    self.image_paths.append(os.path.join(cls_dir, img_name))
                    self.labels.append(idx)

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        label = self.labels[idx]
        image = torchvision.io.read_image(img_path, mode=torchvision.io.ImageReadMode.GRAY)
        image = image.float() / 255.0  # Normalize to [0, 1]
        if self.transform:
            image = self.transform(image)
        return image, label

# Lightweight CNN Model
class LightweightCNN(nn.Module):
    def __init__(self, num_classes=3):
        super(LightweightCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 8, kernel_size=3, padding=1)
        self.pool1 = nn.MaxPool2d(2, 2)  # 64x64 -> 32x32
        self.conv2 = nn.Conv2d(8, 16, kernel_size=3, padding=1)
        self.pool2 = nn.MaxPool2d(2, 2)  # 32x32 -> 16x16
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

# Load dataset with augmentation
def load_garbage_data(batch_size=16):
    train_transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomAdjustSharpness(sharpness_factor=2),
        transforms.Normalize((0.5,), (0.5,))
    ])
    test_transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.Normalize((0.5,), (0.5,))
    ])
    # Adjusted paths to point to the parent directory
    train_dataset = GarbageDataset(image_dir='./garbage_data/train', transform=train_transform)
    test_dataset = GarbageDataset(image_dir='./garbage_data/test', transform=test_transform)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    return train_loader, test_loader

# Evaluate the model
def evaluate_model(model, data_loader, criterion):
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

# Train the model
def train_model(model, train_loader, test_loader, epochs=10):
    criterion = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    train_losses, test_losses = [], []
    train_accuracies, test_accuracies = [], []
    
    start_time = time.time()
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
        train_loss, train_acc = evaluate_model(model, train_loader, criterion)
        test_loss, test_acc = evaluate_model(model, test_loader, criterion)
        train_losses.append(train_loss)
        test_losses.append(test_loss)
        train_accuracies.append(train_acc)
        test_accuracies.append(test_acc)
        print(f"Epoch {epoch+1}/{epochs}, Train Acc: {train_acc:.2f}%, Test Acc: {test_acc:.2f}%")
    training_time = time.time() - start_time
    return {"train_losses": train_losses, "test_losses": test_losses,
            "train_accuracies": train_accuracies, "test_accuracies": test_accuracies}, test_acc, training_time

# Plot metrics
def plot_metrics(metrics):
    epochs = range(1, len(metrics["train_losses"]) + 1)
    plt.figure(figsize=(10, 5))
    plt.plot(epochs, metrics["train_accuracies"], 'b-', label='Training Accuracy')
    plt.plot(epochs, metrics["test_accuracies"], 'r-', label='Testing Accuracy')
    plt.title('Training and Testing Accuracy on Garbage Dataset')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy (%)')
    plt.legend()
    plt.grid(True)
    plt.savefig('garbage_accuracy_plot.png')
    plt.close()

# Main function
def main(argv):
    train_loader, test_loader = load_garbage_data(batch_size=16)
    model = LightweightCNN(num_classes=3)
    print("Starting training on garbage dataset...")
    metrics, test_acc, training_time = train_model(model, train_loader, test_loader, epochs=10)
    print(f"Final Test Accuracy: {test_acc:.2f}%, Training Time: {training_time:.2f} seconds")
    plot_metrics(metrics)
    torch.save(model.state_dict(), 'garbage_classifier.pth')
    print("Model saved as 'garbage_classifier.pth'. Plot saved as 'garbage_accuracy_plot.png'.")

if __name__ == "__main__":
    main(sys.argv)