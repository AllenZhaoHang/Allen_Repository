// File: texture_color.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Implementation of Task 4 - Texture and Color Matching by combining a whole image 
// color histogram with a texture histogram computed from Sobel gradient magnitudes.

#include <iostream>
#include <opencv2/opencv.hpp>
#include <filesystem>
#include <vector>
#include <string>
#include <algorithm>

namespace fs = std::filesystem;

// Compute a whole image RGB histogram.
cv::Mat extractColorHist(const cv::Mat& img, int bins = 16) {
    int histSize[] = { bins, bins, bins };
    float range[] = { 0, 256 };
    const float* ranges[] = { range, range, range };
    int channels[] = { 0, 1, 2 };
    cv::Mat hist;
    cv::calcHist(&img, 1, channels, cv::Mat(), hist, 3, histSize, ranges, true, false);
    cv::normalize(hist, hist, 1, 0, cv::NORM_L1);
    return hist;
}

// Compute a histogram of gradient magnitudes (texture feature) using the Sobel operator.
cv::Mat extractTextureHist(const cv::Mat& img, int bins = 16) {
    cv::Mat gray;
    cv::cvtColor(img, gray, cv::COLOR_BGR2GRAY);
    cv::Mat gradX, gradY;
    cv::Sobel(gray, gradX, CV_32F, 1, 0);
    cv::Sobel(gray, gradY, CV_32F, 0, 1);
    cv::Mat magnitude;
    cv::magnitude(gradX, gradY, magnitude);
    float range[] = { 0, 256 };
    const float* histRange = { range };
    cv::Mat hist;
    cv::calcHist(&magnitude, 1, 0, cv::Mat(), hist, 1, &bins, &histRange, true, false);
    cv::normalize(hist, hist, 1, 0, cv::NORM_L1);
    return hist;
}

// Compare two histograms using intersection.
double compareHistograms(const cv::Mat& hist1, const cv::Mat& hist2) {
    double intersection = cv::compareHist(hist1, hist2, cv::HISTCMP_INTERSECT);
    return 1.0 - intersection;
}

struct Match {
    std::string filename;
    double distance;
};

void runTask4() {
    // Target image: pic.0535.jpg
    std::string targetImagePath = "../ComputerVision/olympus/pic.0535.jpg";
    cv::Mat targetImg = cv::imread(targetImagePath, cv::IMREAD_COLOR);
    if (targetImg.empty()) {
        std::cerr << "Error: Could not read target image " << targetImagePath << std::endl;
        return;
    }
    cv::Mat targetColorHist = extractColorHist(targetImg);
    cv::Mat targetTextureHist = extractTextureHist(targetImg);

    // Database directory containing images.
    std::string databaseDir = "../ComputerVision/olympus/";
    std::vector<Match> matches;

    std::cout << "Processing directory " << databaseDir << std::endl;

    // Loop over all images in the directory (skip the target image).
    for (const auto& entry : fs::directory_iterator(databaseDir)) {
        std::string filePath = entry.path().string();
        if (filePath.find("pic.0535.jpg") != std::string::npos)
            continue;
        cv::Mat img = cv::imread(filePath, cv::IMREAD_COLOR);
        if (img.empty()) continue;
        cv::Mat imgColorHist = extractColorHist(img);
        cv::Mat imgTextureHist = extractTextureHist(img);

        // Compute combined similarity
        double colorDist = compareHistograms(targetColorHist, imgColorHist);
        double textureDist = compareHistograms(targetTextureHist, imgTextureHist);
        double finalDistance = 0.5 * colorDist + 0.5 * textureDist; // Equal weighting

        matches.push_back({ filePath, finalDistance });
    }

    // Sort by increasing distance (lower distance = more similar)
    std::sort(matches.begin(), matches.end(), [](const Match& a, const Match& b) {
        return a.distance < b.distance;
        });

    // Print top 3 matches
    std::cout << "\nTop 3 matches for task 4 pic.0535.jpg:" << std::endl;
    for (int i = 0; i < std::min(3, (int)matches.size()); i++) {
        std::cout << "File Name: " << matches[i].filename << std::endl;
    }
}
