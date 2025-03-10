/**
 * Author: Hang Zhao
 * Date: 2025.3.6
 * Task 4
 * Description:
 *  This program reads camera calibration parameters from a YAML file,
 *  opens a video stream, detects a checkerboard, and uses solvePnP
 *  to compute the camera's rotation (rvec) and translation (tvec)
 *  relative to the checkerboard. It prints rvec and tvec in real time.
 */

#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
#include <string>

// Utility function to generate the 3D positions of each checkerboard corner
// for a 9x6 board (or modify as needed).
static void createKnownBoardPositions(
    cv::Size boardSize,  // For 9×6, pass (9,6)
    float squareSize,    // e.g., 1.0
    std::vector<cv::Point3f>& objectPoints
) {
    objectPoints.clear();
    // Generate (x, y, 0), row by row
    for (int row = 0; row < boardSize.height; ++row) {
        for (int col = 0; col < boardSize.width; ++col) {
            float x = col * squareSize;
            float y = row * squareSize;
            float z = 0.0f;
            objectPoints.push_back(cv::Point3f(x, y, z));
        }
    }
}

int main(int argc, char** argv)
{
    // 1. Load camera calibration parameters
    std::string calibFile = "camera_parameters.yaml"; // Your calibration file
    cv::FileStorage fs(calibFile, cv::FileStorage::READ);
    if(!fs.isOpened()) {
        std::cerr << "Error: Cannot open calibration file: " << calibFile << std::endl;
        return -1;
    }

    cv::Mat cameraMatrix, distCoeffs;
    fs["camera_matrix"] >> cameraMatrix;
    fs["distCoeffs"]    >> distCoeffs;
    fs.release();

    // Print loaded camera parameters
    std::cout << "Loaded cameraMatrix:\n" << cameraMatrix << std::endl;
    std::cout << "Loaded distCoeffs:\n"   << distCoeffs   << std::endl;

    // 2. Open video capture (0 for default camera)
    cv::VideoCapture cap(0);
    if(!cap.isOpened()) {
        std::cerr << "Error: Cannot open camera or video stream!" << std::endl;
        return -1;
    }

    // Define checkerboard info (9 columns x 6 rows, each square = 1.0 units)
    cv::Size boardSize(9, 6);
    float squareSize = 1.0f;

    // Precompute the 3D corner positions of the checkerboard
    std::vector<cv::Point3f> objectPoints;
    createKnownBoardPositions(boardSize, squareSize, objectPoints);

    // For visualization
    cv::namedWindow("Pose Estimation", cv::WINDOW_AUTOSIZE);

    while(true) {
        cv::Mat frame;
        cap >> frame;
        if(frame.empty()) {
            std::cerr << "Warning: Empty frame. Exiting loop..." << std::endl;
            break;
        }

        // Convert to grayscale
        cv::Mat gray;
        cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);

        // 3. Detect checkerboard corners in the current frame
        std::vector<cv::Point2f> corner_set;
        bool found = cv::findChessboardCorners(
            gray,
            boardSize,
            corner_set,
            cv::CALIB_CB_ADAPTIVE_THRESH + cv::CALIB_CB_NORMALIZE_IMAGE
        );

        if(found) {
            // Refine the corner positions to sub-pixel accuracy
            cv::cornerSubPix(
                gray,
                corner_set,
                cv::Size(11,11),
                cv::Size(-1,-1),
                cv::TermCriteria(cv::TermCriteria::EPS + cv::TermCriteria::COUNT, 30, 0.1)
            );

            // Draw corners for visualization
            cv::drawChessboardCorners(frame, boardSize, corner_set, found);

            // 4. Estimate the camera pose relative to the checkerboard
            cv::Mat rvec, tvec;
            cv::solvePnP(
                objectPoints,        // 3D points in checkerboard coordinate space
                corner_set,          // 2D points in image
                cameraMatrix,
                distCoeffs,
                rvec,
                tvec
            );

            // Print rvec and tvec in real time
            // rvec is a rotation in Rodrigues form
            std::cout << "rvec: " << rvec.t() << "  |  tvec: " << tvec.t() << std::endl;
        }

        // Show result
        cv::imshow("Pose Estimation", frame);

        // Press ESC to exit
        char c = static_cast<char>(cv::waitKey(10));
        if(c == 27) { // ESC
            break;
        }
    }

    cap.release();
    cv::destroyAllWindows();
    return 0;
}
