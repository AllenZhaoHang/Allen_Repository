// File: features.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Implementation file containing function definitions for all tasks and extensions in Project 2.

#include <iostream>
#include <opencv2/opencv.hpp>
#include "features.h"

/* ------------------ Histogram Extraction Function ------------------ */
cv::Mat extractColorHist(const cv::Mat& img, int hBins, int sBins) { // ❌ No Default Values Here
    cv::Mat hsv;
    cv::cvtColor(img, hsv, cv::COLOR_BGR2HSV);

    int histSize[] = { hBins, sBins };
    float hRanges[] = { 0, 180 };
    float sRanges[] = { 0, 256 };
    const float* ranges[] = { hRanges, sRanges };
    int channels[] = { 0, 1 };

    cv::Mat hist;
    cv::calcHist(&hsv, 1, channels, cv::Mat(), hist, 2, histSize, ranges);
    cv::normalize(hist, hist, 0, 1, cv::NORM_MINMAX);

    return hist;
}
