# File: CMakeLists.txt
# Author: Hang Zhao
# Date: 2025-02-02
# Description: CMake build file for Project 2: Content-based Image Retrieval.
# This configuration compiles all task source files, including the new Blue Bin extension.

cmake_minimum_required(VERSION 3.10)
project(CBIR_Project)

set(CMAKE_CXX_STANDARD 17)

# Find OpenCV
find_package(OpenCV REQUIRED)
if (OpenCV_FOUND)
    message(STATUS "OpenCV found: ${OpenCV_VERSION}")
else()
    message(FATAL_ERROR "OpenCV not found!")
endif()

include_directories(${OpenCV_INCLUDE_DIRS})

# Add executable
add_executable(cbir
    main.cpp
    baseline.cpp
    histogram_matching.cpp
    multi_histogram.cpp
    texture_color.cpp
    dnn_embeddings.cpp
    compare_dnn_classic.cpp
    custom_cbir.cpp
    blue_bin_extension.cpp
    csv_util.cpp
    features.cpp
)

# Link OpenCV libraries
target_link_libraries(cbir ${OpenCV_LIBS})
