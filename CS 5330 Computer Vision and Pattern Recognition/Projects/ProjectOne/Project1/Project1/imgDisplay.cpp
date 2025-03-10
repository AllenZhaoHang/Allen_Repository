// Hang Zhao
// 2025/01/23
// Proejct One
// Purpose: Display an image using OpenCV and wait for a key press to exit the program.
#include <opencv2/opencv.hpp>
#include <iostream>
#include <direct.h>
int main() {
    std::cout << "Current Working Directory: " << _getcwd(NULL, 0) << std::endl;
    if (!cv::haveImageReader("robot.jpg")) {
        std::cerr << "Error: PNG format not supported by OpenCV!" << std::endl;
        return -1;
    }
    else {
        std::cout << "PNG format is supported by OpenCV!" << std::endl;
    }

	// read image
    cv::Mat image = cv::imread("C:\\Users\\Lenovo\\Desktop\\NEUCourses\\2025SpringSemester\\CS5330ComputerVision\\ProjectOne\\Project1\\x64\\Debug\\robot.bmp");
    if (image.empty()) {
        std::cerr << "Error: Unable to load image! Check the absolute file path." << std::endl;
        return -1;
    }



	// create a window and display the image
    cv::namedWindow("Image Display", cv::WINDOW_AUTOSIZE);
    cv::imshow("Image Display", image);

	// enter loop and wait for key press
    while (true) {
		char key = cv::waitKey(0); // wait for key press
        if (key == 'q') {
            std::cout << "Exiting program..." << std::endl;
			break; // if press 'q' exit the loop
        }
        else {
            std::cout << "You pressed: " << key << std::endl;
        }
    }

    return 0;
}
