/**
 * Author: Hang Zhao
 * Date: 2025.3.6
 * Task 6: Augmented Reality (AR) with a 3D cup
 * Description:
 *   This code reads camera calibration parameters from "camera_parameters.yaml",
 *   detects a 9×6 checkerboard in real-time video, estimates the camera pose (rvec, tvec)
 *   via solvePnP, and projects a custom "cup" model using projectPoints.
 *   The cup is formed by 3D line segments approximating a cylinder and floats above the board.
 */

 #include <opencv2/opencv.hpp>
 #include <iostream>
 #include <vector>
 #include <string>
 
 /**
  * Creates a simple wireframe cup model in 3D.
  * We approximate the cup as a cylinder with 8 points:
  * 4 points for the bottom circle, 4 for the top circle.
  */
 static std::vector<cv::Point3f> createCup3D()
 {
     std::vector<cv::Point3f> cup;
 
     // Adjust radius and height as desired.
     float radius = 2.0f;
     float height = 5.0f;
 
     // Position the cup so its bottom circle is at z=0, roughly around (3, 3).
     // You can move or scale these values if you want the cup placed elsewhere.
     // Bottom circle: 4 points
     cup.push_back(cv::Point3f(3.0f + radius, 3.0f,         0.0f));  // index 0
     cup.push_back(cv::Point3f(3.0f,         3.0f + radius, 0.0f));  // index 1
     cup.push_back(cv::Point3f(3.0f - radius, 3.0f,         0.0f));  // index 2
     cup.push_back(cv::Point3f(3.0f,         3.0f - radius, 0.0f));  // index 3
 
     // Top circle: 4 points, raised by 'height' in z.
     cup.push_back(cv::Point3f(3.0f + radius, 3.0f,         height)); // index 4
     cup.push_back(cv::Point3f(3.0f,         3.0f + radius, height)); // index 5
     cup.push_back(cv::Point3f(3.0f - radius, 3.0f,         height)); // index 6
     cup.push_back(cv::Point3f(3.0f,         3.0f - radius, height)); // index 7
 
     return cup;
 }
 
 /**
  * Generates 3D coordinates for a 9×6 checkerboard (inner corners).
  * Each square is assumed to be 'squareSize' units in width/height.
  */
 static void createChessboard3D(
     cv::Size boardSize,
     float squareSize,
     std::vector<cv::Point3f>& objectPoints
 ) {
     objectPoints.clear();
     for(int row = 0; row < boardSize.height; ++row) {
         for(int col = 0; col < boardSize.width; ++col) {
             objectPoints.push_back(cv::Point3f(col * squareSize, row * squareSize, 0.0f));
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
 
     std::cout << "[Info] Loaded cameraMatrix:\n" << cameraMatrix << std::endl;
     std::cout << "[Info] Loaded distCoeffs:\n"   << distCoeffs   << std::endl;
 
     // 2. Open the camera (device index 0).
     cv::VideoCapture cap(0);
     if(!cap.isOpened()) {
         std::cerr << "Error: Cannot open camera (index 0)!" << std::endl;
         return -1;
     }
 
     // Checkerboard settings: 9×6 corners, each square has size 1.0 (in arbitrary units).
     cv::Size boardSize(9, 6);
     float squareSize = 1.0f;
 
     // Generate 3D points for the checkerboard.
     std::vector<cv::Point3f> board3D;
     createChessboard3D(boardSize, squareSize, board3D);
 
     // Generate the 3D cup model.
     std::vector<cv::Point3f> cup3D = createCup3D();
 
     cv::namedWindow("Cup AR", cv::WINDOW_AUTOSIZE);
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
         bool found = cv::findChessboardCorners(
             gray,
             boardSize,
             corners2D,
             cv::CALIB_CB_ADAPTIVE_THRESH + cv::CALIB_CB_NORMALIZE_IMAGE
         );
 
         if(found) {
             // Refine corner locations to sub-pixel accuracy.
             cv::cornerSubPix(
                 gray,
                 corners2D,
                 cv::Size(11,11),
                 cv::Size(-1,-1),
                 cv::TermCriteria(cv::TermCriteria::EPS + cv::TermCriteria::COUNT, 30, 0.1)
             );
 
             // Draw detected corners for visualization.
             cv::drawChessboardCorners(frame, boardSize, corners2D, found);
 
             // 4. Use solvePnP to get camera pose (rvec, tvec) relative to the board.
             cv::Mat rvec, tvec;
             cv::solvePnP(
                 board3D,   // 3D points of the checkerboard
                 corners2D, // 2D image points (detected corners)
                 cameraMatrix,
                 distCoeffs,
                 rvec,
                 tvec
             );
 
             // 5. Project the cup model onto the image plane.
             std::vector<cv::Point2f> projectedCup;
             cv::projectPoints(
                 cup3D,     // The 3D cup points
                 rvec,
                 tvec,
                 cameraMatrix,
                 distCoeffs,
                 projectedCup
             );
 
             // Draw the wireframe cup (8 points total).
             // Connect the bottom circle, the top circle, and vertical lines:
             // Bottom: 0->1->2->3->0, Top: 4->5->6->7->4, and 0->4,1->5,2->6,3->7.
             if(projectedCup.size() == cup3D.size()) {
                 // Bottom circle (yellow lines)
                 cv::line(frame, projectedCup[0], projectedCup[1], cv::Scalar(0,255,255), 2);
                 cv::line(frame, projectedCup[1], projectedCup[2], cv::Scalar(0,255,255), 2);
                 cv::line(frame, projectedCup[2], projectedCup[3], cv::Scalar(0,255,255), 2);
                 cv::line(frame, projectedCup[3], projectedCup[0], cv::Scalar(0,255,255), 2);
 
                 // Top circle (green lines)
                 cv::line(frame, projectedCup[4], projectedCup[5], cv::Scalar(0,255,0), 2);
                 cv::line(frame, projectedCup[5], projectedCup[6], cv::Scalar(0,255,0), 2);
                 cv::line(frame, projectedCup[6], projectedCup[7], cv::Scalar(0,255,0), 2);
                 cv::line(frame, projectedCup[7], projectedCup[4], cv::Scalar(0,255,0), 2);
 
                 // Vertical connections (blue lines)
                 cv::line(frame, projectedCup[0], projectedCup[4], cv::Scalar(255,0,0), 2);
                 cv::line(frame, projectedCup[1], projectedCup[5], cv::Scalar(255,0,0), 2);
                 cv::line(frame, projectedCup[2], projectedCup[6], cv::Scalar(255,0,0), 2);
                 cv::line(frame, projectedCup[3], projectedCup[7], cv::Scalar(255,0,0), 2);
 
                 // Optional: draw circles at each projected vertex
                 for(size_t i = 0; i < projectedCup.size(); i++){
                     cv::circle(frame, projectedCup[i], 4, cv::Scalar(255, 0, 255), -1);
                 }
             }
         }
 
         // Show the result in the window.
         cv::imshow("Cup AR", frame);
 
         // Press ESC to exit
         char c = static_cast<char>(cv::waitKey(10));
         if(c == 27) {
             break;
         }
     }
 
     cap.release();
     cv::destroyAllWindows();
     return 0;
 }
 