// File: compare_dnn_classic.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Task 6 - Compare DNN embeddings vs. Classic Features (HSV + Texture).
// This version reuses existing functions from Task 5 (DNN Matching) and Task 4 (Classic Features Matching).

#include <iostream>
#include <vector>
#include <string>
#include <filesystem>
#include <opencv2/opencv.hpp>
#include "csv_util.h"  // CSV reader utility

namespace fs = std::filesystem;

// Reuse from dnn_embeddings.cpp (Task 5)
struct DNNFeature {
    std::string filename;
    std::vector<float> features;
};

// Reusing functions from Task 5 for DNN embeddings matching
extern std::vector<DNNFeature> loadDNNFeatures(const std::string& csvFile);
extern void runDNNTaskForTarget(const std::string& targetFilename, const std::vector<DNNFeature>& dnnFeatures);

// Reusing functions from Task 4 for Classic Features (Color & Texture)
extern cv::Mat extractColorHist(const cv::Mat& img, int hBins, int sBins);
extern cv::Mat extractTextureHist(const cv::Mat& img, int bins);
extern double compareHistograms(const cv::Mat& hist1, const cv::Mat& hist2);

// Compare Classic Features (Color & Texture)
void runClassicTaskForTarget(const std::string& targetFilename, const std::string& databaseDir) {
    std::string targetPath = databaseDir + targetFilename;
    cv::Mat targetImg = cv::imread(targetPath, cv::IMREAD_COLOR);
    if (targetImg.empty()) {
        std::cerr << "Error: Could not read target image " << targetPath << std::endl;
        return;
    }

    cv::Mat targetColorHist = extractColorHist(targetImg, 16, 16);
    cv::Mat targetTextureHist = extractTextureHist(targetImg, 16);

    std::vector<std::pair<std::string, double>> matches;

    // Loop over all images in the directory
    for (const auto& entry : fs::directory_iterator(databaseDir)) {
        std::string filePath = entry.path().string();
        if (filePath.find(targetFilename) != std::string::npos)
            continue;
        cv::Mat img = cv::imread(filePath, cv::IMREAD_COLOR);
        if (img.empty()) continue;

        cv::Mat imgColorHist = extractColorHist(img, 16, 16);
        cv::Mat imgTextureHist = extractTextureHist(img, 16);
        double colorDist = compareHistograms(targetColorHist, imgColorHist);
        double textureDist = compareHistograms(targetTextureHist, imgTextureHist);
        double finalDist = 0.5 * colorDist + 0.5 * textureDist;

        matches.push_back({ filePath, finalDist });
    }

    // Sort by increasing distance
    std::sort(matches.begin(), matches.end(), [](const auto& a, const auto& b) {
        return a.second < b.second;
        });

    // Print output
    std::cout << "\nTop 3 matches for task 6 " << targetFilename << " (Classic Features):" << std::endl;
    for (int i = 0; i < std::min(3, (int)matches.size()); i++) {
        std::cout << "File Name: ../ComputerVision/olympus/" << fs::path(matches[i].first).filename().string() << std::endl;
    }
}

// Run both DNN and Classic Matching for comparison
void runTask6() {
    std::string csvFile = "dnn_features.csv";
    std::string databaseDir = "../ComputerVision/olympus/";

    std::vector<DNNFeature> dnnFeatures = loadDNNFeatures(csvFile);
    if (dnnFeatures.empty()) {
        std::cerr << "Error: Unable to load DNN embeddings from " << csvFile << std::endl;
        return;
    }

    std::cout << "Processing directory " << databaseDir << std::endl;

    // Compare for two example images
    std::vector<std::string> targetImages = { "pic.0746.jpg", "pic.0328.jpg" };
    for (const auto& target : targetImages) {
        runDNNTaskForTarget(target, dnnFeatures);
        runClassicTaskForTarget(target, databaseDir);
    }
}