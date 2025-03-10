/**
 * Hang Zhao
 * 2025.3.5
 * Task 1: Detect and refine chessboard corners
 * This file demonstrates how to detect and refine chessboard corners
 * using OpenCV functions: findChessboardCorners, cornerSubPix, and drawChessboardCorners.
 */

 #include <opencv2/opencv.hpp>
 #include <iostream>
 #include <vector>
 
 int main(int argc, char** argv)
 {
     // Open the default camera (device index 0)
     cv::VideoCapture cap(0);
     if (!cap.isOpened()) {
         std::cerr << "Error: Cannot open camera!" << std::endl;
         return -1;
     }
 
     // Number of inner corners per row and column in your checkerboard
     // For example: a 9×6 checkerboard has 9 internal corners horizontally and 6 vertically
     cv::Size patternSize(9, 6);
 
     // Window for showing results
     cv::namedWindow("Checkerboard Detection", cv::WINDOW_AUTOSIZE);
 
     while (true) {
         cv::Mat frame;
         cap >> frame;
         if (frame.empty()) {
             std::cerr << "Warning: Empty frame grabbed. Exiting..." << std::endl;
             break;
         }
 
         // Convert to grayscale because findChessboardCorners works on 8-bit images
         cv::Mat gray;
         cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);
 
         // Prepare a vector to store the detected corners
         std::vector<cv::Point2f> corner_set;
 
         // Try to find the checkerboard corners
         bool patternFound = cv::findChessboardCorners(
             gray,
             patternSize,
             corner_set,
             // Flags: use adaptive threshold, normalize image, and fast check
             cv::CALIB_CB_ADAPTIVE_THRESH + cv::CALIB_CB_NORMALIZE_IMAGE + cv::CALIB_CB_FAST_CHECK
         );
 
         if (patternFound) {
             // Refine corner locations for better accuracy
             cv::cornerSubPix(
                 gray,
                 corner_set,
                 cv::Size(11, 11),   // winSize
                 cv::Size(-1, -1),   // zeroZone
                 cv::TermCriteria(cv::TermCriteria::EPS + cv::TermCriteria::COUNT, 30, 0.1)
             );
 
             // Draw the refined corners on the original frame
             // The last parameter indicates whether the full pattern was found
             cv::drawChessboardCorners(frame, patternSize, corner_set, patternFound);
 
             // Print some debug info, e.g. number of corners detected, first corner location
             std::cout << "Number of corners detected: " << corner_set.size() << std::endl;
             if (!corner_set.empty()) {
                 std::cout << "First corner: ("
                           << corner_set[0].x << ", "
                           << corner_set[0].y << ")" << std::endl;
             }
         }
 
         // Show the result
         cv::imshow("Checkerboard Detection", frame);
 
         // Press ESC to exit
         char key = static_cast<char>(cv::waitKey(10));
         if (key == 27) { // ESC
             break;
         }
     }
 
     cap.release();
     cv::destroyAllWindows();
     return 0;
 }
 