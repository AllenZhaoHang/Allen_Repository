/**
 * Author: Hang Zhao
 * Date: 2025.3.6
 * Task 7 Harris Corner Detection
 * Description:
 *   This program detects and visualizes Harris corners in a live video stream.
 *   It allows experimenting with different threshold values to understand how
 *   feature detection works. The detected feature points could be used as anchor
 *   points for placing virtual objects in an AR system.
 */

 #include <opencv2/opencv.hpp>
 #include <iostream>
 
 /** Global variables */
 int threshold_value = 100; // Default threshold for Harris corner detection
 cv::Mat frame, gray, harris_response;
 
 // Callback function to adjust threshold interactively
 void onThresholdChange(int, void*) {
     // Compute Harris corners again with new threshold
     cv::Mat harris_norm, harris_scaled;
     cv::normalize(harris_response, harris_norm, 0, 255, cv::NORM_MINMAX, CV_32FC1);
     cv::convertScaleAbs(harris_norm, harris_scaled);
 
     // Draw corners
     cv::Mat display = frame.clone();
     for (int y = 0; y < harris_norm.rows; y++) {
         for (int x = 0; x < harris_norm.cols; x++) {
             if ((int)harris_norm.at<float>(y, x) > threshold_value) {
                 cv::circle(display, cv::Point(x, y), 3, cv::Scalar(0, 0, 255), -1);
             }
         }
     }
 
     // Show the updated frame with detected corners
     cv::imshow("Harris Corner Detection", display);
 }
 
 int main(int argc, char** argv) {
     // Open the default camera
     cv::VideoCapture cap(0);
     if (!cap.isOpened()) {
         std::cerr << "Error: Cannot open the camera!" << std::endl;
         return -1;
     }
 
     // Create a window
     cv::namedWindow("Harris Corner Detection", cv::WINDOW_AUTOSIZE);
     cv::createTrackbar("Threshold", "Harris Corner Detection", &threshold_value, 255, onThresholdChange);
 
     while (true) {
         cap >> frame;
         if (frame.empty()) {
             std::cerr << "Warning: Empty frame, stopping..." << std::endl;
             break;
         }
 
         // Convert to grayscale
         cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);
 
         // Compute Harris corners
         cv::cornerHarris(gray, harris_response, 2, 3, 0.04);
 
         // Apply the threshold to highlight strong corners
         onThresholdChange(0, 0);
 
         // Exit on ESC key
         char c = static_cast<char>(cv::waitKey(10));
         if (c == 27) { // ESC key
             break;
         }
     }
 
     cap.release();
     cv::destroyAllWindows();
     return 0;
 }
 