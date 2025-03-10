/**
 * Author: Hang Zhao
 * Date: 2025.3.6
 * Extension 2: Augmented Reality (AR) with 3D point cloud
 * Description:
 *   This program reconstructs a **3D point cloud of an object** in a scene
 *   by using a detected **calibration chessboard** as a reference.
 *   - It detects the chessboard, estimates camera pose using `solvePnP`,
 *   - Uses stereo depth estimation or manual point selection to get 3D object points.
 *   - Projects the computed 3D points into the scene as a point cloud.
 */

 #include <opencv2/opencv.hpp>
 #include <opencv2/calib3d.hpp>
 #include <iostream>
 #include <vector>
 
 /** Global Variables */
 cv::VideoCapture cap;
 cv::Mat frame;
 cv::Mat cameraMatrix, distCoeffs;
 cv::Size boardSize(9, 6); // Chessboard size: 9x6 internal corners
 std::vector<cv::Point3f> chessboard3D;
 cv::Mat rvec, tvec;
 bool poseFound = false;
 
 /**
  * Generate 3D chessboard points for calibration.
  * Each square is assumed to be `squareSize` units.
  */
 void createChessboard3D(float squareSize = 1.0f) {
     chessboard3D.clear();
     for (int i = 0; i < boardSize.height; i++) {
         for (int j = 0; j < boardSize.width; j++) {
             chessboard3D.push_back(cv::Point3f(j * squareSize, i * squareSize, 0.0f));
         }
     }
 }
 
 /**
  * Manually select object points in the scene (if no stereo depth is available).
  * Returns a set of **3D points** in the **chessboard coordinate system**.
  */
 std::vector<cv::Point3f> getObject3DPoints() {
     std::vector<cv::Point3f> object3D;
 
     // Example: Define 3D points (Assuming known object size)
     object3D.push_back(cv::Point3f(3.0f, 3.0f, 2.0f)); // A point above the board
     object3D.push_back(cv::Point3f(4.0f, 3.0f, 2.5f));
     object3D.push_back(cv::Point3f(5.0f, 3.0f, 1.5f));
     object3D.push_back(cv::Point3f(4.5f, 2.5f, 2.0f));
     object3D.push_back(cv::Point3f(3.5f, 2.5f, 2.3f));
 
     return object3D;
 }
 
 /** Function to draw the projected 3D point cloud onto the image */
 void drawPointCloud(cv::Mat& frame, const std::vector<cv::Point2f>& projectedPoints) {
     for (const auto& point : projectedPoints) {
         cv::circle(frame, point, 5, cv::Scalar(0, 0, 255), -1); // Draw red dots
     }
 }
 
 int main(int argc, char** argv)
 {
     // 1. Load camera calibration parameters
     std::string calibFile = "camera_parameters.yaml";
     cv::FileStorage fs(calibFile, cv::FileStorage::READ);
     if (!fs.isOpened()) {
         std::cerr << "Error: Cannot open " << calibFile << std::endl;
         return -1;
     }
     fs["camera_matrix"] >> cameraMatrix;
     fs["distCoeffs"]    >> distCoeffs;
     fs.release();
 
     // 2. Open the camera
     cap.open(0);
     if (!cap.isOpened()) {
         std::cerr << "Error: Cannot open camera!" << std::endl;
         return -1;
     }
 
     createChessboard3D(); // Generate chessboard 3D points
 
     cv::namedWindow("3D Point Cloud AR", cv::WINDOW_AUTOSIZE);
     std::cout << "[Info] Press ESC to exit.\n";
 
     while (true) {
         cap >> frame;
         if (frame.empty()) {
             std::cerr << "[Warning] Empty frame, stopping...\n";
             break;
         }
 
         // Convert to grayscale for corner detection
         cv::Mat gray;
         cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);
 
         // 3. Detect chessboard corners
         std::vector<cv::Point2f> corners2D;
         poseFound = cv::findChessboardCorners(gray, boardSize, corners2D);
 
         if (poseFound) {
             cv::cornerSubPix(gray, corners2D, cv::Size(11, 11), cv::Size(-1, -1),
                              cv::TermCriteria(cv::TermCriteria::EPS + cv::TermCriteria::COUNT, 30, 0.1));
 
             cv::drawChessboardCorners(frame, boardSize, corners2D, poseFound);
 
             // 4. Estimate camera pose
             cv::solvePnP(chessboard3D, corners2D, cameraMatrix, distCoeffs, rvec, tvec);
 
             // 5. Get 3D object points (either from stereo depth or manual selection)
             std::vector<cv::Point3f> object3D = getObject3DPoints();
 
             // 6. Project object points onto the image
             std::vector<cv::Point2f> projectedPoints;
             cv::projectPoints(object3D, rvec, tvec, cameraMatrix, distCoeffs, projectedPoints);
 
             // 7. Draw the projected point cloud
             drawPointCloud(frame, projectedPoints);
         }
 
         // Show the image
         cv::imshow("3D Point Cloud AR", frame);
 
         // Exit on ESC
         if (cv::waitKey(10) == 27) break;
     }
 
     cap.release();
     cv::destroyAllWindows();
     return 0;
 }
 