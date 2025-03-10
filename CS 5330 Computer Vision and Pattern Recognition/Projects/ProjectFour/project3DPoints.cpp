/**
 * Author: Hang Zhao
 * Date: 2025.3.6
 * Task 5
 * Description:
 *   This program loads camera calibration parameters, detects a checkerboard,
 *   estimates the camera pose (rvec, tvec) via solvePnP, then uses projectPoints
 *   to render a simple 3D axes on the target. The axes appear in real time
 *   as the camera or the board moves.
 */

#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
#include <string>

// Generate 3D points of a 9×6 checkerboard (adjust as needed).
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

// Create a small set of 3D axes lines: origin, X, Y, Z directions
static void createAxesPoints(std::vector<cv::Point3f>& axesPoints, float length = 3.0f)
{
    axesPoints.clear();
    // The first point is the origin (0,0,0)
    axesPoints.push_back(cv::Point3f(0, 0, 0));
    // Then three points along the X, Y, Z axes
    axesPoints.push_back(cv::Point3f(length, 0, 0));  // X
    axesPoints.push_back(cv::Point3f(0, length, 0));  // Y
    axesPoints.push_back(cv::Point3f(0, 0, length));  // Z
}

int main(int argc, char** argv)
{
    // 1. Load previously saved camera intrinsics (camera_matrix, distCoeffs)
    std::string calibFile = "camera_parameters.yaml";
    cv::FileStorage fs(calibFile, cv::FileStorage::READ);
    if (!fs.isOpened()) {
        std::cerr << "Error: Cannot open calibration file " << calibFile << std::endl;
        return -1;
    }

    cv::Mat cameraMatrix, distCoeffs;
    fs["camera_matrix"] >> cameraMatrix;
    fs["distCoeffs"]    >> distCoeffs;
    fs.release();

    std::cout << "Loaded cameraMatrix:\n" << cameraMatrix << std::endl;
    std::cout << "Loaded distCoeffs:\n"   << distCoeffs   << std::endl;

    // 2. Open camera or video
    cv::VideoCapture cap(0);
    if (!cap.isOpened()) {
        std::cerr << "Error: Cannot open camera!" << std::endl;
        return -1;
    }

    // Checkerboard settings: 9 columns x 6 rows, each square = 1.0 (arbitrary units)
    cv::Size boardSize(9, 6);
    float squareSize = 1.0f;

    // Precompute the 3D corners of the checkerboard
    std::vector<cv::Point3f> board3D;
    createChessboard3D(boardSize, squareSize, board3D);

    // Also prepare a simple set of 3D axes for demonstration
    std::vector<cv::Point3f> axes3D;
    createAxesPoints(axes3D, 3.0f); // length of each axis line

    cv::namedWindow("Project 3D Points", cv::WINDOW_AUTOSIZE);

    while (true) {
        cv::Mat frame;
        cap >> frame;
        if (frame.empty()) {
            std::cerr << "Warning: Empty frame.\n";
            break;
        }

        // Convert to grayscale for corner detection
        cv::Mat gray;
        cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);

        // 3. Detect checkerboard corners
        std::vector<cv::Point2f> corner_set;
        bool found = cv::findChessboardCorners(
            gray,
            boardSize,
            corner_set,
            cv::CALIB_CB_ADAPTIVE_THRESH + cv::CALIB_CB_NORMALIZE_IMAGE
        );

        if (found) {
            // Refine corner positions
            cv::cornerSubPix(
                gray,
                corner_set,
                cv::Size(11, 11),
                cv::Size(-1, -1),
                cv::TermCriteria(cv::TermCriteria::EPS + cv::TermCriteria::COUNT, 30, 0.1)
            );

            // Draw the detected corners
            cv::drawChessboardCorners(frame, boardSize, corner_set, found);

            // 4. Solve PnP to get rvec and tvec
            cv::Mat rvec, tvec;
            cv::solvePnP(
                board3D,       // 3D corners in object space
                corner_set,    // 2D corners in image
                cameraMatrix,
                distCoeffs,
                rvec,
                tvec
            );

            // 5. Use projectPoints to get 2D locations of our 3D axes
            std::vector<cv::Point2f> axes2D;
            cv::projectPoints(
                axes3D,       // 3D axes points
                rvec,
                tvec,
                cameraMatrix,
                distCoeffs,
                axes2D
            );

            // We expect axes2D to have 4 points: origin, X-end, Y-end, Z-end
            if (axes2D.size() == 4) {
                // Draw lines for the axes on top of the frame
                // origin -> X (red), origin -> Y (green), origin -> Z (blue)
                cv::Point2f origin = axes2D[0];

                // X axis
                cv::line(frame, origin, axes2D[1], cv::Scalar(0,0,255), 2);
                // Y axis
                cv::line(frame, origin, axes2D[2], cv::Scalar(0,255,0), 2);
                // Z axis
                cv::line(frame, origin, axes2D[3], cv::Scalar(255,0,0), 2);
            }

            // (Optional) Project a few corners or a small 3D object similarly
            // e.g., if you want to project an entire cube or marker outline
        }

        // Display result
        cv::imshow("Project 3D Points", frame);

        char key = static_cast<char>(cv::waitKey(10));
        if (key == 27) { // ESC
            break;
        }
    }

    cap.release();
    cv::destroyAllWindows();
    return 0;
}
