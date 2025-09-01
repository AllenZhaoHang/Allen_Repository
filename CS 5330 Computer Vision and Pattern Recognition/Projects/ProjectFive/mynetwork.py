#!/usr/bin/env python3
# Hang Zhao
# Date: March 15, 2025
# Generate network structure diagram using torchviz

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchviz import make_dot

# Define the network class
class MyNetwork(nn.Module):
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
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.pool2(self.dropout(F.relu(self.conv2(x))))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        return F.log_softmax(self.fc2(x), dim=1)

# Create model instance and dummy input
model = MyNetwork()
x = torch.randn(1, 1, 28, 28)

# Forward pass to generate computation graph
y = model(x)

# Generate and save the network diagram
graph = make_dot(y, params=dict(model.named_parameters()))
graph.render("network_structure", format="png", view=True)