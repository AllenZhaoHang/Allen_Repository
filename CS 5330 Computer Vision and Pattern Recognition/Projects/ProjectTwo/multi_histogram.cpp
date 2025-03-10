// File: multi_histogram.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Implementation of Task 3 - Multi-histogram Matching by computing separate 
// histograms for different spatial parts (top and bottom halves) of the image and combining the distances.

#include <iostream>
#include <opencv2/opencv.hpp>
#include <filesystem>
#include <vector>
#include <string>
#include <algorithm>

namespace fs = std::filesystem;

// Extract two RGB histograms: one for the top half and one for the bottom half.
std::vector<cv::Mat> extractMultiHistograms(const cv::Mat& img, int bins = 8) {
    std::vector<cv::Mat> histograms;
    int mid = img.rows / 2;
    cv::Mat topHalf = img(cv::Range(0, mid), cv::Range::all());
    cv::Mat bottomHalf = img(cv::Range(mid, img.rows), cv::Range::all());

    int histSize[] = { bins, bins, bins };
    float range[] = { 0, 256 };
    const float* ranges[] = { range, range, range };
    int channels[] = { 0, 1, 2 };

    cv::Mat topHist, bottomHist;
    cv::calcHist(&topHalf, 1, channels, cv::Mat(), topHist, 3, histSize, ranges, true, false);
    cv::calcHist(&bottomHalf, 1, channels, cv::Mat(), bottomHist, 3, histSize, ranges, true, false);
    cv::normalize(topHist, topHist, 1, 0, cv::NORM_L1);
    cv::normalize(bottomHist, bottomHist, 1, 0, cv::NORM_L1);

    histograms.push_back(topHist);
    histograms.push_back(bottomHist);
    return histograms;
}

// Combine distances between corresponding histograms (equal weighting).
double multiHistogramDistance(const std::vector<cv::Mat>& hist1, const std::vector<cv::Mat>& hist2) {
    double d1 = cv::compareHist(hist1[0], hist2[0], cv::HISTCMP_INTERSECT);
    double d2 = cv::compareHist(hist1[1], hist2[1], cv::HISTCMP_INTERSECT);
    double intersection = (d1 + d2) / 2.0;
    return 1.0 - intersection;
}

struct Match {
    std::string filename;
    double distance;
};

void runTask3() {
    // Target image: pic.0274.jpg
    std::string targetImagePath = "../ComputerVision/olympus/pic.0274.jpg";
    cv::Mat targetImg = cv::imread(targetImagePath, cv::IMREAD_COLOR);
    if (targetImg.empty()) {
        std::cerr << "Error: Could not read target image " << targetImagePath << std::endl;
        return;
    }
    std::vector<cv::Mat> targetHists = extractMultiHistograms(targetImg);

    // Database directory containing images.
    std::string databaseDir = "../ComputerVision/olympus/";
    std::vector<Match> matches;

    std::cout << "Processing directory " << databaseDir << std::endl;

    // Loop over all images in the directory (skip the target image).
    for (const auto& entry : fs::directory_iterator(databaseDir)) {
        std::string filePath = entry.path().string();
        if (filePath.find("pic.0274.jpg") != std::string::npos)
            continue;
        cv::Mat img = cv::imread(filePath, cv::IMREAD_COLOR);
        if (img.empty()) continue;
        std::vector<cv::Mat> imgHists = extractMultiHistograms(img);
        double histDistance = multiHistogramDistance(targetHists, imgHists);
        matches.push_back({ filePath, histDistance });
    }

    // Sort by increasing distance (lower distance = more similar)
    std::sort(matches.begin(), matches.end(), [](const Match& a, const Match& b) {
        return a.distance < b.distance;
        });

    // Print top 3 matches
    std::cout << "\nTop 3 matches for task 3 pic.0274.jpg:" << std::endl;
    for (int i = 0; i < std::min(3, (int)matches.size()); i++) {
        std::cout << "File Name: " << matches[i].filename << std::endl;
    }
}