// File: histogram_matching.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Implementation of Task 2 - Histogram Matching using a 2D color histogram 
// (in HSV space) and histogram intersection as the distance metric.

#include <iostream>
#include <opencv2/opencv.hpp>
#include <filesystem>
#include <vector>
#include <string>
#include <algorithm>

namespace fs = std::filesystem;

// Compute a 2D histogram (Hue and Saturation channels)
cv::Mat extractColorHistogram(const cv::Mat& img, int hBins = 16, int sBins = 16) {
    cv::Mat hsv;
    cv::cvtColor(img, hsv, cv::COLOR_BGR2HSV);
    int histSize[] = { hBins, sBins };
    float hRanges[] = { 0, 180 };
    float sRanges[] = { 0, 256 };
    const float* ranges[] = { hRanges, sRanges };
    int channels[] = { 0, 1 };
    cv::Mat hist;
    cv::calcHist(&hsv, 1, channels, cv::Mat(), hist, 2, histSize, ranges, true, false);
    cv::normalize(hist, hist, 1, 0, cv::NORM_L1);
    return hist;
}

// Compute histogram intersection distance.
double histogramIntersectionMatching(const cv::Mat& hist1, const cv::Mat& hist2) {
    double sum = 0.0;
    for (int i = 0; i < hist1.rows; i++) {
        for (int j = 0; j < hist1.cols; j++) {
            float val1 = hist1.at<float>(i, j);
            float val2 = hist2.at<float>(i, j);
            sum += std::min(val1, val2);
        }
    }
    return 1.0 - sum; // Convert similarity to distance (lower is better)
}

struct Match {
    std::string filename;
    double distance;
};

void runTask2() {
    // Target image: pic.0164.jpg
    std::string targetImagePath = "../ComputerVision/olympus/pic.0164.jpg";
    cv::Mat targetImg = cv::imread(targetImagePath, cv::IMREAD_COLOR);
    if (targetImg.empty()) {
        std::cerr << "Error: Could not read target image " << targetImagePath << std::endl;
        return;
    }
    cv::Mat targetHist = extractColorHistogram(targetImg);

    // Database directory containing images.
    std::string databaseDir = "../ComputerVision/olympus/";
    std::vector<Match> matches;

    std::cout << "Processing directory " << databaseDir << std::endl;

    // Loop over all images in the directory (skip the target image).
    for (const auto& entry : fs::directory_iterator(databaseDir)) {
        std::string filePath = entry.path().string();
        if (filePath.find("pic.0164.jpg") != std::string::npos)
            continue;
        cv::Mat img = cv::imread(filePath, cv::IMREAD_COLOR);
        if (img.empty()) continue;
        cv::Mat hist = extractColorHistogram(img);
        double histDistance = histogramIntersectionMatching(targetHist, hist);
        matches.push_back({ filePath, histDistance });
    }

    // Sort by increasing distance (lower distance = more similar)
    std::sort(matches.begin(), matches.end(), [](const Match& a, const Match& b) {
        return a.distance < b.distance;
        });

    // Print top 3 matches
    std::cout << "\nTop 3 matches for task 2 pic.0164.jpg:" << std::endl;
    for (int i = 0; i < std::min(3, (int)matches.size()); i++) {
        std::cout << "File Name: " << matches[i].filename << std::endl;
    }
}