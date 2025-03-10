#include <opencv2/opencv.hpp>
#include <iostream>

int in() {
    std::cout << cv::getBuildInformation() << std::endl;
    return 0;
}
