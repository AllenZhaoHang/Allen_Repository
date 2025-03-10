// File: dnn_embeddings.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Implementation of Task 5 ¨C Deep Network Embeddings matching.
// This version uses the provided CSV utility functions to load 512-dimensional embedding vectors
// from a CSV file. The cosine distance is computed to compare embeddings.

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <filesystem>
#include "csv_util.h"  // Use the CSV utility functions

namespace fs = std::filesystem;

// Structure to hold DNN features.
struct DNNFeature {
    std::string filename;
    std::vector<float> features;
};

// Load DNN features from a CSV file using the CSV utility.
std::vector<DNNFeature> loadDNNFeatures(const std::string& csvFile) {
    std::vector<char*> filenames;
    std::vector<std::vector<float>> data;
    int ret = read_image_data_csv(const_cast<char*>(csvFile.c_str()), filenames, data, 0);
    std::vector<DNNFeature> dnnFeatures;
    if (ret != 0) {
        std::cerr << "Error reading CSV file: " << csvFile << std::endl;
        return dnnFeatures;
    }
    for (size_t i = 0; i < filenames.size(); i++) {
        DNNFeature feat;
        feat.filename = filenames[i];
        feat.features = data[i];
        dnnFeatures.push_back(feat);
        delete[] filenames[i]; // Free memory allocated by read_image_data_csv.
    }
    return dnnFeatures;
}

// Compute cosine distance between two embedding vectors.
float cosineDistance(const std::vector<float>& v1, const std::vector<float>& v2) {
    float dot = 0.0f, norm1 = 0.0f, norm2 = 0.0f;
    for (size_t i = 0; i < v1.size(); i++) {
        dot += v1[i] * v2[i];
        norm1 += v1[i] * v1[i];
        norm2 += v2[i] * v2[i];
    }
    if (norm1 == 0 || norm2 == 0)
        return 1.0f;
    float cosine = dot / (std::sqrt(norm1) * std::sqrt(norm2));
    return 1.0f - cosine;
}

struct DNNMatch {
    std::string filename;
    float distance;
};

void runDNNTaskForTarget(const std::string& targetFilename, const std::vector<DNNFeature>& dnnFeatures) {
    // Find the target feature in the CSV data.
    auto it = std::find_if(dnnFeatures.begin(), dnnFeatures.end(), [&](const DNNFeature& f) {
        return f.filename.find(targetFilename) != std::string::npos;
        });

    if (it == dnnFeatures.end()) {
        std::cerr << "Error: Target image " << targetFilename << " not found in CSV." << std::endl;
        return;
    }

    std::vector<float> targetFeature = it->features;

    // Compute cosine distance to all other images.
    std::vector<DNNMatch> matches;
    for (const auto& feat : dnnFeatures) {
        if (feat.filename.find(targetFilename) != std::string::npos)
            continue;
        float dist = cosineDistance(targetFeature, feat.features);
        matches.push_back({ feat.filename, dist });
    }

    std::sort(matches.begin(), matches.end(), [](const DNNMatch& a, const DNNMatch& b) {
        return a.distance < b.distance;
        });

    // Print output to match the exact format in the provided image.
    std::cout << "\nTop 3 matches for task 5 " << targetFilename << ":" << std::endl;
    for (int i = 0; i < std::min(3, (int)matches.size()); i++) {
        std::cout << "File Name: ../ComputerVision/olympus/" << fs::path(matches[i].filename).filename().string() << std::endl;
    }
}

void runTask5() {
    std::string csvFile = "dnn_features.csv";
    std::vector<DNNFeature> dnnFeatures = loadDNNFeatures(csvFile);

    if (dnnFeatures.empty()) {
        std::cerr << "Error: Unable to load DNN embeddings from " << csvFile << std::endl;
        return;
    }

    std::cout << "Processing directory ../ComputerVision/olympus" << std::endl;

    // Run matching for required images.
    runDNNTaskForTarget("pic.0893.jpg", dnnFeatures);
    runDNNTaskForTarget("pic.0164.jpg", dnnFeatures);
}