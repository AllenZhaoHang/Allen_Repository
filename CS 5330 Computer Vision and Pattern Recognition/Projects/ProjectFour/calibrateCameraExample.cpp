/**
 * Author: Hang Zhao
 * Date: 2025.3.6
 * Description:
 *   This program demonstrates how to run camera calibration using OpenCV.
 *   It loads previously saved corner_list and point_list from a YAML file,
 *   checks if there are enough frames (>= 5), then runs cv::calibrateCamera,
 *   prints the resulting camera matrix, distortion coefficients, and final
 *   reprojection error, and saves the results to a separate file.
 */

 #include <opencv2/opencv.hpp>
 #include <iostream>
 #include <vector>
 #include <string>
 
 int main(int argc, char** argv)
 {
     // 1. Load corner_list and point_list from YAML
     //    (Assume they were previously saved in "corner_point_data.yaml")
     std::string inputFilename = "corner_point_data.yaml";
     cv::FileStorage fs(inputFilename, cv::FileStorage::READ);
     if(!fs.isOpened()) {
         std::cerr << "Error: Cannot open " << inputFilename << std::endl;
         return -1;
     }
 
     std::vector<std::vector<cv::Point2f>> corner_list;
     std::vector<std::vector<cv::Vec3f>>   point_list;
 
     // Read arrays from the file
     fs["corner_list"] >> corner_list; // YAML -> corner_list
     fs["point_list"]  >> point_list;  // YAML -> point_list
     fs.release();
 
     std::cout << "Loaded " << corner_list.size() << " sets of corners from "
               << inputFilename << "\n";
 
     // 2. Check if we have enough data to run calibration
     if(corner_list.size() < 5) {
         std::cerr << "Not enough calibration frames (need >= 5). Exiting.\n";
         return 0;
     }
 
     // 3. Prepare image size (you must know the resolution of your calibration images)
     //    Typically, we can assume they were all the same resolution.
     //    If you actually saved the images, you can load one to get .cols / .rows.
     //    Here, let's assume 640x480 for demonstration. Replace with your actual size!
     cv::Size imageSize(640, 480);
 
     // 4. Create matrices/variables needed for calibration
     //    camera_matrix (3x3, CV_64F), distortion_coefficients, rotation vectors, translation vectors
     cv::Mat camera_matrix = cv::Mat::eye(3, 3, CV_64F);   // initialize as identity
     camera_matrix.at<double>(0, 2) = imageSize.width  / 2.0;  // approximate principal point x
     camera_matrix.at<double>(1, 2) = imageSize.height / 2.0;  // approximate principal point y
 
     cv::Mat distCoeffs;  // if we don't want radial distortion at first, can keep it empty
     std::vector<cv::Mat> rvecs, tvecs;
 
     // 5. (Optional) Some calibration flags
     //    e.g. if you want to fix aspect ratio: CV_CALIB_FIX_ASPECT_RATIO
     //    or skip tangential distortion: CV_CALIB_ZERO_TANGENT_DIST
     //    They can be combined with |
     int flags = 0;
     // flags |= cv::CALIB_FIX_ASPECT_RATIO;
     // flags |= cv::CALIB_ZERO_TANGENT_DIST;
 
     // 6. Print initial camera_matrix and distCoeffs
     std::cout << "Initial camera_matrix:\n" << camera_matrix << std::endl;
     std::cout << "Initial distCoeffs size: " << distCoeffs.size() << "\n";
 
     // 7. Run calibration
     //    corner_list is a vector of 2D points
     //    point_list is a vector of 3D points
     //    each entry in corner_list corresponds to the same index in point_list
     double rms = cv::calibrateCamera(
         point_list,           // 3D points in world
         corner_list,          // 2D points in image
         imageSize,            // size of the image used
         camera_matrix,        // input/output camera matrix
         distCoeffs,           // output distortion coefficients
         rvecs,                // output rotations for each view
         tvecs,                // output translations for each view
         flags                 // calibration flags
         // , cv::TermCriteria(...) // can specify termination criteria if desired
     );
 
     // 8. Print results
     std::cout << "Calibration complete.\n";
     std::cout << "Final reprojection error (RMS): " << rms << std::endl;
     std::cout << "camera_matrix:\n" << camera_matrix << std::endl;
     std::cout << "distCoeffs:\n"     << distCoeffs << std::endl;
 
     // 9. Save camera_matrix and distCoeffs to a separate YAML file
     std::string outputFilename = "camera_parameters.yaml";
     cv::FileStorage fsOut(outputFilename, cv::FileStorage::WRITE);
     if(!fsOut.isOpened()) {
         std::cerr << "Error: Cannot open " << outputFilename << " for writing.\n";
         return -1;
     }
 
     fsOut << "image_width"  << imageSize.width;
     fsOut << "image_height" << imageSize.height;
     fsOut << "camera_matrix" << camera_matrix;
     fsOut << "distCoeffs"    << distCoeffs;
     fsOut << "avg_reproj_error" << rms;
 
     // (Optional) also save rvecs and tvecs if you want
     // fsOut << "rvecs" << "[";
     // for (size_t i = 0; i < rvecs.size(); i++)
     //     fsOut << rvecs[i];
     // fsOut << "]";
     // fsOut << "tvecs" << "[";
     // for (size_t i = 0; i < tvecs.size(); i++)
     //     fsOut << tvecs[i];
     // fsOut << "]";
 
     fsOut.release();
     std::cout << "Saved calibration results to " << outputFilename << std::endl;
 
     return 0;
 }
 