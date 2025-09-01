#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Project 5 Task 4: Experimentation with deep network on Fashion MNIST

# Import statements
import sys
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
import time
import random
import csv

# Dynamic MyNetwork class with configurable convolution layers
class MyNetwork(nn.Module):
    """
    A configurable convolutional neural network for Fashion MNIST.
    Args:
        num_conv_layers: Number of convolution layers (2 or 3)
        dropout_rate: Dropout rate for the dropout layer
        num_classes: Number of output classes (default 10 for Fashion MNIST)
    """
    def __init__(self, num_conv_layers=2, dropout_rate=0.25, num_classes=10):
        super(MyNetwork, self).__init__()
        self.num_conv_layers = num_conv_layers
        self.dropout_rate = dropout_rate
        
        # Define convolution layers dynamically
        self.conv_layers = nn.ModuleList()
        in_channels = 1
        out_channels = [10, 20, 40][:num_conv_layers]  # Number of filters increases
        for i in range(num_conv_layers):
            self.conv_layers.append(nn.Conv2d(in_channels, out_channels[i], kernel_size=3))
            in_channels = out_channels[i]
        
        # Pooling layers after each convolution (only if input size allows)
        self.pools = nn.ModuleList()
        size = 28
        for i in range(num_conv_layers):
            size = size - 3 + 1  # After conv with kernel 3
            if size >= 2:  # Only add pooling if size is large enough
                self.pools.append(nn.MaxPool2d(2, 2))
                size = size // 2
            else:
                self.pools.append(nn.Identity())  # No pooling if size too small
        
        # Calculate the size after convolutions and pooling
        self.flatten_size = out_channels[num_conv_layers-1] * size * size
        
        # Fully connected layers
        self.dropout = nn.Dropout(dropout_rate)
        self.fc1 = nn.Linear(self.flatten_size, 50)
        self.fc2 = nn.Linear(50, num_classes)

    def forward(self, x):
        for i in range(self.num_conv_layers):
            x = self.conv_layers[i](x)
            x = torch.relu(x)
            x = self.pools[i](x)
        x = self.dropout(x)
        x = x.view(-1, self.flatten_size)
        x = torch.relu(self.fc1(x))
        return torch.log_softmax(self.fc2(x), dim=1)

# Function to load Fashion MNIST dataset
def load_fashion_mnist(batch_size):
    """
    Load Fashion MNIST dataset with data loaders.
    Args:
        batch_size: Number of samples per batch
    Returns:
        train_loader, test_loader: DataLoaders for training and test sets
    """
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    train_dataset = torchvision.datasets.FashionMNIST(root='./data', train=True, download=True, transform=transform)
    test_dataset = torchvision.datasets.FashionMNIST(root='./data', train=False, download=True, transform=transform)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, test_loader

# Function to evaluate the model
def evaluate_model(model, data_loader, criterion):
    """
    Evaluate the model on a dataset.
    Args:
        model: Trained network model
        data_loader: DataLoader for the dataset
        criterion: Loss function
    Returns:
        loss: Average loss
        accuracy: Accuracy percentage
    """
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

# Function to train the model
def train_model(model, train_loader, test_loader, epochs=5):
    """
    Train the model on Fashion MNIST dataset.
    Args:
        model: Network model
        train_loader: DataLoader for training set
        test_loader: DataLoader for test set
        epochs: Number of training epochs
    Returns:
        test_acc: Final test accuracy
        training_time: Total training time in seconds
    """
    criterion = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    
    start_time = time.time()
    for epoch in range(epochs):
        model.train()
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
    training_time = time.time() - start_time
    
    # Evaluate on test set
    _, test_acc = evaluate_model(model, test_loader, criterion)
    return test_acc, training_time

# Function to run experiment for a single configuration
def run_experiment(num_conv_layers, dropout_rate, batch_size, epochs=5):
    """
    Run a single experiment with the given configuration.
    Args:
        num_conv_layers: Number of convolution layers
        dropout_rate: Dropout rate
        batch_size: Batch size for training
        epochs: Number of training epochs
    Returns:
        test_acc: Test accuracy
        training_time: Training time in seconds
    """
    # Load data
    train_loader, test_loader = load_fashion_mnist(batch_size)
    
    # Create model
    model = MyNetwork(num_conv_layers=num_conv_layers, dropout_rate=dropout_rate)
    
    # Train and evaluate
    test_acc, training_time = train_model(model, train_loader, test_loader, epochs)
    return test_acc, training_time

# Function to plot results
def plot_results(results, filename_prefix="experiment"):
    """
    Plot the results for each dimension.
    Args:
        results: List of dictionaries containing experiment results
        filename_prefix: Prefix for the output plot files
    """
    # Group results by each dimension
    conv_layers = sorted(set(r['num_conv_layers'] for r in results))
    dropout_rates = sorted(set(r['dropout_rate'] for r in results))
    batch_sizes = sorted(set(r['batch_size'] for r in results))
    
    # Plot test accuracy vs. number of conv layers
    plt.figure(figsize=(10, 5))
    for dr in dropout_rates:
        for bs in batch_sizes:
            accs = [r['test_acc'] for r in results if r['dropout_rate'] == dr and r['batch_size'] == bs]
            cl = [r['num_conv_layers'] for r in results if r['dropout_rate'] == dr and r['batch_size'] == bs]
            plt.plot(cl, accs, marker='o', label=f'Dropout={dr}, Batch={bs}')
    plt.title('Test Accuracy vs. Number of Conv Layers')
    plt.xlabel('Number of Conv Layers')
    plt.ylabel('Test Accuracy (%)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{filename_prefix}_conv_layers.png')
    plt.close()
    
    # Plot test accuracy vs. dropout rate
    plt.figure(figsize=(10, 5))
    for cl in conv_layers:
        for bs in batch_sizes:
            accs = [r['test_acc'] for r in results if r['num_conv_layers'] == cl and r['batch_size'] == bs]
            dr = [r['dropout_rate'] for r in results if r['num_conv_layers'] == cl and r['batch_size'] == bs]
            plt.plot(dr, accs, marker='o', label=f'ConvLayers={cl}, Batch={bs}')
    plt.title('Test Accuracy vs. Dropout Rate')
    plt.xlabel('Dropout Rate')
    plt.ylabel('Test Accuracy (%)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{filename_prefix}_dropout_rate.png')
    plt.close()
    
    # Plot test accuracy vs. batch size
    plt.figure(figsize=(10, 5))
    for cl in conv_layers:
        for dr in dropout_rates:
            accs = [r['test_acc'] for r in results if r['num_conv_layers'] == cl and r['dropout_rate'] == dr]
            bs = [r['batch_size'] for r in results if r['num_conv_layers'] == cl and r['dropout_rate'] == dr]
            plt.plot(bs, accs, marker='o', label=f'ConvLayers={cl}, Dropout={dr}')
    plt.title('Test Accuracy vs. Batch Size')
    plt.xlabel('Batch Size')
    plt.ylabel('Test Accuracy (%)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{filename_prefix}_batch_size.png')
    plt.close()
    
    # Plot training time vs. number of conv layers
    plt.figure(figsize=(10, 5))
    for dr in dropout_rates:
        for bs in batch_sizes:
            times = [r['training_time'] for r in results if r['dropout_rate'] == dr and r['batch_size'] == bs]
            cl = [r['num_conv_layers'] for r in results if r['dropout_rate'] == dr and r['batch_size'] == bs]
            plt.plot(cl, times, marker='o', label=f'Dropout={dr}, Batch={bs}')
    plt.title('Training Time vs. Number of Conv Layers')
    plt.xlabel('Number of Conv Layers')
    plt.ylabel('Training Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{filename_prefix}_conv_layers_time.png')
    plt.close()

# Main function
def main(argv):
    """
    Main function to perform experimentation on Fashion MNIST dataset.
    Args:
        argv: Command line arguments (not used)
    """
    # Options for each dimension
    conv_layers_options = [2, 3]  # Removed 4 due to input size constraints
    dropout_rate_options = [0.25, 0.5, 0.75]
    batch_size_options = [32, 64, 128]
    
    # Initial configuration
    best_config = {'num_conv_layers': 2, 'dropout_rate': 0.25, 'batch_size': 64}
    best_acc = 0
    
    # Results storage
    results = []
    
    # Run 3 cycles of round-robin optimization
    for cycle in range(3):
        print(f"\nCycle {cycle+1}/3")
        
        # Optimize number of conv layers
        print("Optimizing number of conv layers...")
        for cl in conv_layers_options:
            config = best_config.copy()
            config['num_conv_layers'] = cl
            print(f"Testing config: {config}")
            test_acc, training_time = run_experiment(cl, config['dropout_rate'], config['batch_size'])
            results.append({
                'num_conv_layers': cl,
                'dropout_rate': config['dropout_rate'],
                'batch_size': config['batch_size'],
                'test_acc': test_acc,
                'training_time': training_time
            })
            if test_acc > best_acc:
                best_acc = test_acc
                best_config['num_conv_layers'] = cl
        
        # Optimize dropout rate
        print("Optimizing dropout rate...")
        for dr in dropout_rate_options:
            config = best_config.copy()
            config['dropout_rate'] = dr
            print(f"Testing config: {config}")
            test_acc, training_time = run_experiment(config['num_conv_layers'], dr, config['batch_size'])
            results.append({
                'num_conv_layers': config['num_conv_layers'],
                'dropout_rate': dr,
                'batch_size': config['batch_size'],
                'test_acc': test_acc,
                'training_time': training_time
            })
            if test_acc > best_acc:
                best_acc = test_acc
                best_config['dropout_rate'] = dr
        
        # Optimize batch size
        print("Optimizing batch size...")
        for bs in batch_size_options:
            config = best_config.copy()
            config['batch_size'] = bs
            print(f"Testing config: {config}")
            test_acc, training_time = run_experiment(config['num_conv_layers'], config['dropout_rate'], bs)
            results.append({
                'num_conv_layers': config['num_conv_layers'],
                'dropout_rate': config['dropout_rate'],
                'batch_size': bs,
                'test_acc': test_acc,
                'training_time': training_time
            })
            if test_acc > best_acc:
                best_acc = test_acc
                best_config['batch_size'] = bs
        
        # Add some randomization to avoid local optima
        best_config['num_conv_layers'] = random.choice(conv_layers_options)
        best_config['dropout_rate'] = random.choice(dropout_rate_options)
        best_config['batch_size'] = random.choice(batch_size_options)
    
    # Save results to CSV
    with open('experiment_results.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['num_conv_layers', 'dropout_rate', 'batch_size', 'test_acc', 'training_time'])
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    # Plot results
    plot_results(results, "fashion_mnist_experiment")
    print("Task 4 completed: Results saved in 'experiment_results.csv'. Plots saved with prefix 'fashion_mnist_experiment'.")

if __name__ == "__main__":
    main(sys.argv)