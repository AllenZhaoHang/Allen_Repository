// File: features.h
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Header file declaring functions for all tasks and extensions in Project 2.

#ifndef FEATURES_H
#define FEATURES_H

#include <opencv2/opencv.hpp>

// Task functions:
void runTask1();
void runTask2();
void runTask3();
void runTask4();
void runTask5();
void runTask6();
void runTask7();

// Extension: Blue Bin Retrieval
void runBlueBinRetrieval();

// Feature extraction function (keep default arguments here)
cv::Mat extractColorHist(const cv::Mat& img, int hBins = 16, int sBins = 16);

#endif // FEATURES_H
