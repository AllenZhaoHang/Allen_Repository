# CS 5330 Pattern Recognition and Computer Vision
## Project 5: Recognition using Deep Networks

### Project 5 Information
- **Name**: Hang Zhao
- **Team Member**: Hang Zhao  

### Environment
- **Operating System**: Mac OS
- **IDE**: Visual Studio Code 2022

### Travel Days
- **Travel Days**: 0

### Task Implementations

- **Task 1 - Build and train a network to recognize digits**: 
  A Get the MNIST digit data set: task1a.py
  B Build a network model : task1b.py
  C Train the model: task1c.py
  D Save the network to a file: mynetwork.pth https://drive.google.com/file/d/1RFgECrg0BOrvXlHllwovU93Jiv43Vn20/view?usp=sharing
  E Read the network and run it on the test set: task1e.py
  F Test the network on new inputs: task1f.py
  

- **Task 2 - Examine your network**: 
  A Analyze the first layer: task2a.py
  B Show the effect of the filters: task2b.py

- **Task 3 - Transfer Learning on Greek Letters**: 
    task3.py
    greeks letter training dataset: https://drive.google.com/drive/folders/1iAx9o-vl5tzit2kGVBm_Dg--NCD37tvP?usp=sharing

- **Task 4 - Test on Your Own Handwritten Digits**: 
    task4.py

### Extensions

- **Extension 1: Load a Pre-trained Network and Evaluate Its First Couple of Convolutional Layers**: [`pretrained_network_analysis.py`](pretrained_network_analysis.py)  
  Loads a pre-trained ResNet18, visualizes its first layer filters, and applies them to MNIST images, showing complex edge detection patterns.

- **Extension 2: Build a Live Video Digit Recognition Application**: [`live_digit_recognition.py`](live_digit_recognition.py)  
  Implements a real-time digit recognition system using the MNIST network, displaying predictions on webcam video feed with 90% accuracy on test digits.
  Demo: https://youtu.be/T3OC5e2Gd0U

### All Other Files
- **You can find all other files in the link below**:
    https://drive.google.com/drive/folders/1lZP9wyfv98dCJ6PoVXjZNt9yUSrs-daT?usp=sharing