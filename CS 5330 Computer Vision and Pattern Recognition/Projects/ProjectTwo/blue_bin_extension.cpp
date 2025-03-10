// File: blue_bin_extension.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: CBIR system for detecting blue trash bins using color histograms, shape filtering, and DNN embeddings.

#include <iostream>
#include <vector>
#include <opencv2/opencv.hpp>
#include <filesystem>
#include <cmath>
#include "csv_util.h"

namespace fs = std::filesystem;

/* ------------------ Feature Extraction ------------------ */

// Compute the blue-focused HSV histogram
cv::Mat computeBlueHistogram(const cv::Mat& image) {
    cv::Mat hsv;
    cv::cvtColor(image, hsv, cv::COLOR_BGR2HSV);

    // Define blue color range
    cv::Scalar lower_blue(100, 50, 50);
    cv::Scalar upper_blue(140, 255, 255);
    cv::Mat mask;
    cv::inRange(hsv, lower_blue, upper_blue, mask);

    // Compute histogram
    int histSize = 16;
    float range[] = { 0, 180 };
    const float* histRange = { range };
    cv::Mat hist;
    cv::calcHist(&hsv, 1, 0, mask, hist, 1, &histSize, &histRange);
    cv::normalize(hist, hist, 0, 1, cv::NORM_MINMAX);

    return hist;
}

// Extract contour-based shape features
cv::Vec2f computeShapeFeatures(const cv::Mat& image) {
    cv::Mat gray, edges;
    cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);
    cv::Canny(gray, edges, 50, 150);

    std::vector<std::vector<cv::Point>> contours;
    cv::findContours(edges, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    float maxArea = 0;
    float aspectRatio = 0;

    for (const auto& contour : contours) {
        cv::Rect boundingBox = cv::boundingRect(contour);
        float area = boundingBox.area();
        if (area > maxArea) {
            maxArea = area;
            aspectRatio = float(boundingBox.width) / boundingBox.height;
        }
    }
    return cv::Vec2f(maxArea, aspectRatio);
}

// Compute histogram intersection similarity
double histogramIntersectionBlue(const cv::Mat& hist1, const cv::Mat& hist2) {
    return cv::compareHist(hist1, hist2, cv::HISTCMP_INTERSECT);
}

// Compute cosine similarity for DNN embeddings
double cosineSimilarityBlue(const std::vector<float>& vec1, const std::vector<float>& vec2) {
    double dot = 0.0, norm1 = 0.0, norm2 = 0.0;
    for (size_t i = 0; i < vec1.size(); i++) {
        dot += vec1[i] * vec1[i];
        norm1 += vec1[i] * vec1[i];
        norm2 += vec2[i] * vec2[i];
    }
    return 1.0 - (dot / (sqrt(norm1) * sqrt(norm2)));
}

/* ------------------ Retrieval Function ------------------ */

void runBlueBinRetrieval() {
    std::string databaseDir = "../ComputerVision/olympus/";
    std::string targetFile = "pic.0287.jpg";  // Example target image

    std::cout << "Processing directory " << databaseDir << std::endl;

    cv::Mat targetImage = cv::imread(databaseDir + targetFile);
    if (targetImage.empty()) {
        std::cerr << "Error: Could not read target image." << std::endl;
        return;
    }

    // Extract features for the target image
    cv::Mat targetHist = computeBlueHistogram(targetImage);
    cv::Vec2f targetShape = computeShapeFeatures(targetImage);

    // Read deep embeddings from CSV
    std::vector<char*> filenames;
    std::vector<std::vector<float>> embeddings;
    char filename[] = "dnn_features.csv";
    read_image_data_csv(filename, filenames, embeddings);

    std::vector<std::pair<std::string, double>> results;

    for (const auto& entry : fs::directory_iterator(databaseDir)) {
        std::string filePath = entry.path().string();
        cv::Mat img = cv::imread(filePath);
        if (img.empty()) continue;

        // Compute color similarity
        cv::Mat imgHist = computeBlueHistogram(img);
        double colorSim = histogramIntersectionBlue(targetHist, imgHist);

        // Compute shape similarity
        cv::Vec2f imgShape = computeShapeFeatures(img);
        double shapeSim = 1.0 - (std::abs(targetShape[0] - imgShape[0]) / (targetShape[0] + 1e-6));  // Normalize

        // Find corresponding DNN feature
        std::vector<float> imgEmbedding;
        for (size_t i = 0; i < filenames.size(); i++) {
            if (filePath.find(filenames[i]) != std::string::npos) {
                imgEmbedding = embeddings[i];
                break;
            }
        }
        double dnnSim = cosineSimilarityBlue(embeddings[0], imgEmbedding);

        // Compute final weighted similarity
        double finalSim = (0.5 * colorSim) + (0.3 * shapeSim) + (0.2 * dnnSim);
        results.push_back({ filePath, finalSim });
    }

    // Sort results by similarity
    std::sort(results.begin(), results.end(), [](const auto& a, const auto& b) { return a.second > b.second; });

    // Print top 5 matches in correct format
    std::cout << "\nTop 5 matches for extension task " << targetFile << ":" << std::endl;
    for (int i = 0; i < 5; i++)
        std::cout << "File Name: ../ComputerVision/olympus/" << fs::path(results[i].first).filename().string() << std::endl;
}