// File: custom_cbir.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Implementation of Task 7 - Custom CBIR using texture-based matching for Image 1 (Stuffed Animal on Grass) 
// and color + DNN embedding matching for Image 2 (Red Statue in Dark Leaves).

#include <iostream>
#include <vector>
#include <opencv2/opencv.hpp>
#include <filesystem>
#include <cmath>
#include "repos/ProjectTwo/ProjectTwo/csv_util.h"

namespace fs = std::filesystem;

/* ------------------ Feature Extraction Functions ------------------ */

// Compute Sobel-based texture histogram (Used for Image 1: 0928)
cv::Mat computeTextureHistogram(const cv::Mat& image) {
    cv::Mat gray, grad_x, grad_y, abs_grad_x, abs_grad_y, gradient;

    cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);
    cv::Sobel(gray, grad_x, CV_32F, 1, 0, 3);
    cv::Sobel(gray, grad_y, CV_32F, 0, 1, 3);

    cv::convertScaleAbs(grad_x, abs_grad_x);
    cv::convertScaleAbs(grad_y, abs_grad_y);
    cv::addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0, gradient);

    int histSize = 16;
    float range[] = { 0, 256 };
    const float* histRange = { range };
    cv::Mat hist;
    cv::calcHist(&gradient, 1, 0, cv::Mat(), hist, 1, &histSize, &histRange);
    cv::normalize(hist, hist, 0, 1, cv::NORM_MINMAX);

    return hist;
}

// Compute HSV histogram for color-based matching (Used for Image 2: 1015)
cv::Mat computeHSVHistogram(const cv::Mat& image) {
    cv::Mat hsv;
    cv::cvtColor(image, hsv, cv::COLOR_BGR2HSV);

    int hBins = 16, sBins = 16;
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

// Compute histogram intersection similarity
double histogramIntersection(const cv::Mat& hist1, const cv::Mat& hist2) {
    return cv::compareHist(hist1, hist2, cv::HISTCMP_INTERSECT);
}

// Compute cosine similarity for DNN embeddings
double cosineSimilarity(const std::vector<float>& vec1, const std::vector<float>& vec2) {
    double dot = 0.0, norm1 = 0.0, norm2 = 0.0;
    for (size_t i = 0; i < vec1.size(); i++) {
        dot += vec1[i] * vec2[i];
        norm1 += vec1[i] * vec1[i];
        norm2 += vec2[i] * vec2[i];
    }
    return 1.0 - (dot / (sqrt(norm1) * sqrt(norm2)));
}

/* ------------------ Retrieval Function ------------------ */

void runTask7() {
    std::string databaseDir = "../ComputerVision/olympus/";
    std::string targetFile1 = "pic.0928.jpg"; // Image 1
    std::string targetFile2 = "pic.1015.jpg"; // Image 2

    std::cout << "Processing directory " << databaseDir << std::endl;

    cv::Mat targetImage1 = cv::imread(databaseDir + targetFile1);
    cv::Mat targetImage2 = cv::imread(databaseDir + targetFile2);

    if (targetImage1.empty() || targetImage2.empty()) {
        std::cerr << "Error: Could not read target images." << std::endl;
        return;
    }

    // Extract features for Image 1 (Texture-Based)
    cv::Mat targetTextureHist = computeTextureHistogram(targetImage1);

    // Extract features for Image 2 (Color + DNN-Based)
    cv::Mat targetColorHist = computeHSVHistogram(targetImage2);

    // Read deep embeddings from CSV
    char filename[] = "dnn_features.csv";
    std::vector<char*> filenames;
    std::vector<std::vector<float>> embeddings;
    read_image_data_csv(filename, filenames, embeddings);

    std::vector<std::pair<std::string, double>> results1; // Image 1 results
    std::vector<std::pair<std::string, double>> results2; // Image 2 results

    for (const auto& entry : fs::directory_iterator(databaseDir)) {
        std::string filePath = entry.path().string();
        cv::Mat img = cv::imread(filePath);

        if (img.empty()) continue;

        // Compute texture similarity for Image 1
        cv::Mat imgTextureHist = computeTextureHistogram(img);
        double textureSim = histogramIntersection(targetTextureHist, imgTextureHist);
        results1.push_back({ filePath, textureSim });

        // Compute color + DNN similarity for Image 2
        cv::Mat imgColorHist = computeHSVHistogram(img);
        double colorSim = histogramIntersection(targetColorHist, imgColorHist);

        // Find corresponding DNN feature
        std::vector<float> imgEmbedding;
        for (size_t i = 0; i < filenames.size(); i++) {
            if (filePath.find(filenames[i]) != std::string::npos) {
                imgEmbedding = embeddings[i];
                break;
            }
        }
        double dnnSim = cosineSimilarity(embeddings[0], imgEmbedding);  // Compare with target embedding
        double finalSim2 = 0.5 * colorSim + 0.5 * dnnSim;
        results2.push_back({ filePath, finalSim2 });
    }

    // Sort and display results
    std::sort(results1.begin(), results1.end(), [](const auto& a, const auto& b) { return a.second > b.second; });
    std::sort(results2.begin(), results2.end(), [](const auto& a, const auto& b) { return a.second > b.second; });

    std::cout << "\nTop 5 matches for task 7 " << targetFile1 << ":" << std::endl;
    for (int i = 0; i < 5; i++)
        std::cout << "File Name: ../ComputerVision/olympus/" << fs::path(results1[i].first).filename().string() << std::endl;

    std::cout << "\nTop 5 matches for task 7 " << targetFile2 << ":" << std::endl;
    for (int i = 0; i < 5; i++)
        std::cout << "File Name: ../ComputerVision/olympus/" << fs::path(results2[i].first).filename().string() << std::endl;
}