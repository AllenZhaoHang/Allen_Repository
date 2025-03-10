/**
 * Author: Hang Zhao
 * Date: 2025.3.7
 * Task 2: Capture and save calibration images
 * Description:
 *  This code lets the user capture specific frames for camera calibration,
 *  and saves both the 2D corner coordinates (corner_list) and the corresponding
 *  3D points (point_list) to a YAML file at the end.
 */

 #include <opencv2/opencv.hpp>
 #include <iostream>
 #include <vector>
 #include <string>
 
 // Utility function to generate the 3D positions of each checkerboard corner
 static void create3DChessboardPoints(
     cv::Size boardSize,  // For 9×6, pass (9,6)
     float squareSize,    // Size of each square in chosen units (e.g., 1.0)
     std::vector<cv::Vec3f>& point_set
 ) {
     point_set.clear();
     // Generate (x, y, 0) for each corner, spaced by squareSize
     for (int row = 0; row < boardSize.height; ++row) {
         for (int col = 0; col < boardSize.width; ++col) {
             float x = col * squareSize;
             float y = row * squareSize;
             float z = 0.0f;
             point_set.push_back(cv::Vec3f(x, y, z));
         }
     }
 }
 
 int main(int argc, char** argv)
 {
     // Open the camera (device 0). You can also open a video file instead.
     cv::VideoCapture cap(0);
     if(!cap.isOpened()) {
         std::cerr << "Error: Cannot open camera!" << std::endl;
         return -1;
     }
 
     // Checkerboard: 9 columns and 6 rows of inner corners
     cv::Size boardSize(9, 6);
     float squareSize = 1.0f; // Adjust if you want real-world mm or other units
 
     // Lists to store 2D corners and matching 3D points for each saved frame
     std::vector<std::vector<cv::Point2f>> corner_list;
     std::vector<std::vector<cv::Vec3f>>   point_list;
 
     // (Optional) store actual images for debugging or future reference
     std::vector<cv::Mat> savedImages;
 
     cv::namedWindow("Calibration", cv::WINDOW_AUTOSIZE);
     std::cout << "Instructions:\n"
               << " - Press 's' to save corners if the checkerboard is found.\n"
               << " - Press ESC to exit.\n";
 
     while(true) {
         cv::Mat frame;
         cap >> frame;
         if(frame.empty()) {
             std::cerr << "Warning: Empty frame, exiting...\n";
             break;
         }
 
         // Convert to grayscale for corner detection
         cv::Mat gray;
         cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);
 
         // Detect corners in the checkerboard
         std::vector<cv::Point2f> corner_set;
         bool found = cv::findChessboardCorners(
             gray,
             boardSize,
             corner_set,
             cv::CALIB_CB_ADAPTIVE_THRESH + cv::CALIB_CB_NORMALIZE_IMAGE
         );
 
         if(found) {
             // Refine corner positions to sub-pixel accuracy
             cv::cornerSubPix(
                 gray,
                 corner_set,
                 cv::Size(11, 11),
                 cv::Size(-1, -1),
                 cv::TermCriteria(cv::TermCriteria::EPS + cv::TermCriteria::COUNT, 30, 0.1)
             );
             // Draw the corners on the display image
             cv::drawChessboardCorners(frame, boardSize, corner_set, found);
         }
 
         cv::imshow("Calibration", frame);
 
         char key = static_cast<char>(cv::waitKey(10));
         if(key == 27) { // ESC
             break;
         }
         else if(key == 's') {
             // Save corners and matching 3D points only if found
             if(found) {
                 std::vector<cv::Vec3f> point_set;
                 create3DChessboardPoints(boardSize, squareSize, point_set);
 
                 corner_list.push_back(corner_set);
                 point_list.push_back(point_set);
 
                 // Optional: save the current frame (copy)
                 savedImages.push_back(frame.clone());
 
                 std::cout << "Saved a set of " << corner_set.size()
                           << " corners. Total saved: " << corner_list.size() << "\n";
             } else {
                 std::cout << "Chessboard not found. Nothing was saved.\n";
             }
         }
     }
 
     // Print final counts
     std::cout << "\nFinal corner_list size: " << corner_list.size() << std::endl;
     std::cout << "Final point_list size: " << point_list.size() << std::endl;
 
     // ------ NEW: Save corner_list and point_list to a YAML file ------
     if (!corner_list.empty()) {
         // You can change the output filename as you wish
         std::string filename = "corner_point_data.yaml";
 
         cv::FileStorage fs(filename, cv::FileStorage::WRITE);
         if (!fs.isOpened()) {
             std::cerr << "Error: Cannot open " << filename << " for writing." << std::endl;
         } else {
             // Write corner_list and point_list
             fs << "corner_list" << "[";
             for (size_t i = 0; i < corner_list.size(); i++) {
                 fs << corner_list[i];
             }
             fs << "]";
 
             fs << "point_list" << "[";
             for (size_t i = 0; i < point_list.size(); i++) {
                 fs << point_list[i];
             }
             fs << "]";
 
             // (Optional) you could also write the saved images, but it's usually large.
             // For example:
             // fs << "images" << "[";
             // for (size_t i = 0; i < savedImages.size(); i++) {
             //     fs << savedImages[i];
             // }
             // fs << "]";
 
             fs.release();
             std::cout << "Data saved to " << filename << std::endl;
         }
     } else {
         std::cout << "No data to save. corner_list is empty.\n";
     }
     // ------ End of NEW Code Section ------
 
     // Cleanup
     cap.release();
     cv::destroyAllWindows();
     return 0;
 }
 