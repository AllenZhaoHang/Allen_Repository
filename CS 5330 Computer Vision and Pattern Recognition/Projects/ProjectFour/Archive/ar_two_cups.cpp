/**
 * Author: Hang Zhao
 * Date: 2025.3.6
 * Extension one: Augmented Reality (AR) with two 3D cups
 * Description:
 *   This code reads camera calibration parameters from "camera_parameters.yaml",
 *   detects a 9×6 checkerboard in real-time video, estimates the camera pose (rvec, tvec)
 *   via solvePnP, and projects **two custom "cups"** using projectPoints.
 *   The cups are approximated as wireframe cylinders and are displayed above the board.
 */

 #include <opencv2/opencv.hpp>
 #include <iostream>
 #include <vector>
 #include <string>
 
 /**
  * Creates a simple wireframe cup model in 3D.
  * Each cup consists of 8 points forming a cylinder (4 bottom, 4 top).
  * The cup is positioned at (x_offset, y_offset).
  */
 static std::vector<cv::Point3f> createCup3D(float x_offset, float y_offset)
 {
     std::vector<cv::Point3f> cup;
     float radius = 2.0f;
     float height = 5.0f;
 
     // Bottom circle: 4 points
     cup.push_back(cv::Point3f(x_offset + radius, y_offset,         0.0f));  // 0
     cup.push_back(cv::Point3f(x_offset,         y_offset + radius, 0.0f));  // 1
     cup.push_back(cv::Point3f(x_offset - radius, y_offset,         0.0f));  // 2
     cup.push_back(cv::Point3f(x_offset,         y_offset - radius, 0.0f));  // 3
 
     // Top circle: 4 points (shifted in height)
     cup.push_back(cv::Point3f(x_offset + radius, y_offset,         height)); // 4
     cup.push_back(cv::Point3f(x_offset,         y_offset + radius, height)); // 5
     cup.push_back(cv::Point3f(x_offset - radius, y_offset,         height)); // 6
     cup.push_back(cv::Point3f(x_offset,         y_offset - radius, height)); // 7
 
     return cup;
 }
 
 /**
  * Generates 3D coordinates for a 9×6 checkerboard (inner corners).
  * Each square is assumed to be 'squareSize' units in width/height.
  */
 static void createChessboard3D(cv::Size boardSize, float squareSize, std::vector<cv::Point3f>& objectPoints)
 {
     objectPoints.clear();
     for(int row = 0; row < boardSize.height; ++row) {
         for(int col = 0; col < boardSize.width; ++col) {
             objectPoints.push_back(cv::Point3f(col * squareSize, row * squareSize, 0.0f));
         }
     }
 }
 
 /** Function to draw a wireframe cup */
 void drawCup(cv::Mat& frame, const std::vector<cv::Point2f>& projectedCup)
 {
     if(projectedCup.size() == 8) {
         // Bottom circle (yellow)
         cv::line(frame, projectedCup[0], projectedCup[1], cv::Scalar(0,255,255), 2);
         cv::line(frame, projectedCup[1], projectedCup[2], cv::Scalar(0,255,255), 2);
         cv::line(frame, projectedCup[2], projectedCup[3], cv::Scalar(0,255,255), 2);
         cv::line(frame, projectedCup[3], projectedCup[0], cv::Scalar(0,255,255), 2);
 
         // Top circle (green)
         cv::line(frame, projectedCup[4], projectedCup[5], cv::Scalar(0,255,0), 2);
         cv::line(frame, projectedCup[5], projectedCup[6], cv::Scalar(0,255,0), 2);
         cv::line(frame, projectedCup[6], projectedCup[7], cv::Scalar(0,255,0), 2);
         cv::line(frame, projectedCup[7], projectedCup[4], cv::Scalar(0,255,0), 2);
 
         // Vertical connections (blue)
         cv::line(frame, projectedCup[0], projectedCup[4], cv::Scalar(255,0,0), 2);
         cv::line(frame, projectedCup[1], projectedCup[5], cv::Scalar(255,0,0), 2);
         cv::line(frame, projectedCup[2], projectedCup[6], cv::Scalar(255,0,0), 2);
         cv::line(frame, projectedCup[3], projectedCup[7], cv::Scalar(255,0,0), 2);
 
         // Draw small circles at each projected vertex
         for(size_t i = 0; i < projectedCup.size(); i++){
             cv::circle(frame, projectedCup[i], 4, cv::Scalar(255, 0, 255), -1);
         }
     }
 }
 
 int main(int argc, char** argv)
 {
     // 1. Load camera calibration parameters.
     std::string calibFile = "camera_parameters.yaml";
     cv::FileStorage fs(calibFile, cv::FileStorage::READ);
     if(!fs.isOpened()) {
         std::cerr << "Error: Cannot open " << calibFile << std::endl;
         return -1;
     }
 
     cv::Mat cameraMatrix, distCoeffs;
     fs["camera_matrix"] >> cameraMatrix;
     fs["distCoeffs"]    >> distCoeffs;
     fs.release();
 
     // 2. Open the camera (device index 0).
     cv::VideoCapture cap(0);
     if(!cap.isOpened()) {
         std::cerr << "Error: Cannot open camera (index 0)!" << std::endl;
         return -1;
     }
 
     // Checkerboard settings: 9×6 corners, each square has size 1.0.
     cv::Size boardSize(9, 6);
     float squareSize = 1.0f;
 
     // Generate 3D points for the checkerboard.
     std::vector<cv::Point3f> board3D;
     createChessboard3D(boardSize, squareSize, board3D);
 
     // Create two cups at different positions.
     std::vector<cv::Point3f> cup1 = createCup3D(2.0f, 3.0f); // First cup
     std::vector<cv::Point3f> cup2 = createCup3D(6.0f, 3.0f); // Second cup
 
     cv::namedWindow("Two Cups AR", cv::WINDOW_AUTOSIZE);
     std::cout << "[Info] Press ESC to exit.\n";
 
     while(true) {
         cv::Mat frame;
         cap >> frame;
         if(frame.empty()) {
             std::cerr << "[Warning] Empty frame, stopping...\n";
             break;
         }
 
         // Convert to grayscale for corner detection.
         cv::Mat gray;
         cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);
 
         // 3. Detect checkerboard corners.
         std::vector<cv::Point2f> corners2D;
         bool found = cv::findChessboardCorners(gray, boardSize, corners2D);
 
         if(found) {
             cv::cornerSubPix(gray, corners2D, cv::Size(11,11), cv::Size(-1,-1),
                              cv::TermCriteria(cv::TermCriteria::EPS + cv::TermCriteria::COUNT, 30, 0.1));
 
             cv::drawChessboardCorners(frame, boardSize, corners2D, found);
 
             // 4. Get pose (rvec, tvec) of the checkerboard
             cv::Mat rvec, tvec;
             cv::solvePnP(board3D, corners2D, cameraMatrix, distCoeffs, rvec, tvec);
 
             // 5. Project and draw both cups.
             std::vector<cv::Point2f> projectedCup1, projectedCup2;
             cv::projectPoints(cup1, rvec, tvec, cameraMatrix, distCoeffs, projectedCup1);
             cv::projectPoints(cup2, rvec, tvec, cameraMatrix, distCoeffs, projectedCup2);
 
             drawCup(frame, projectedCup1);
             drawCup(frame, projectedCup2);
         }
 
         cv::imshow("Two Cups AR", frame);
 
         if(cv::waitKey(10) == 27) break;
     }
 
     cap.release();
     cv::destroyAllWindows();
     return 0;
 }
 