// File: baseline.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Implementation of Task 1 - Baseline Matching using a 7x7 central patch 
// and Sum-of-Squared-Differences (SSD) as the distance metric.

#include <iostream>
#include <opencv2/opencv.hpp>
#include <filesystem>
#include <vector>
#include <string>
#include <algorithm>

namespace fs = std::filesystem;

// Extract a 7x7 patch from the center of the image.
cv::Mat extractBaselineFeature(const cv::Mat& img) {
    int patchSize = 7;
    int startX = (img.cols - patchSize) / 2;
    int startY = (img.rows - patchSize) / 2;
    cv::Rect roi(startX, startY, patchSize, patchSize);
    return img(roi).clone();
}

// Compute sum-of-squared differences (SSD) between two patches.
double computeSSD(const cv::Mat& f1, const cv::Mat& f2) {
    cv::Mat diff;
    cv::absdiff(f1, f2, diff);
    diff = diff.mul(diff);
    return cv::sum(diff)[0];
}

struct Match {
    std::string filename;
    double distance;
};

void runTask1() {
    // Target image: pic.1016.jpg
    std::string targetImagePath = "../ComputerVision/olympus/pic.1016.jpg";
    cv::Mat targetImg = cv::imread(targetImagePath, cv::IMREAD_GRAYSCALE);
    if (targetImg.empty()) {
        std::cerr << "Error: Could not read target image " << targetImagePath << std::endl;
        return;
    }
    cv::Mat targetFeature = extractBaselineFeature(targetImg);

    // Database directory containing images.
    std::string databaseDir = "../ComputerVision/olympus/";
    std::vector<Match> matches;

    std::cout << "Processing directory " << databaseDir << std::endl;

    // Loop over all images in the directory (skip the target image).
    for (const auto& entry : fs::directory_iterator(databaseDir)) {
        std::string filePath = entry.path().string();
        if (filePath.find("pic.1016.jpg") != std::string::npos)
            continue;
        cv::Mat img = cv::imread(filePath, cv::IMREAD_GRAYSCALE);
        if (img.empty()) continue;
        cv::Mat feature = extractBaselineFeature(img);
        double ssd = computeSSD(targetFeature, feature);
        matches.push_back({ filePath, ssd });
    }

    // Sort by increasing SSD (smaller distance = more similar).
    std::sort(matches.begin(), matches.end(), [](const Match& a, const Match& b) {
        return a.distance < b.distance;
        });

    // Print top 3 matches
    std::cout << "\nTop 3 matches for task 1 pic.1016.jpg:" << std::endl;
    for (int i = 0; i < std::min(3, (int)matches.size()); i++) {
        std::cout << "File Name: " << matches[i].filename << std::endl;
    }
}