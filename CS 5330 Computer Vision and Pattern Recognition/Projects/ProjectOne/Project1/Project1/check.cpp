#include <iostream>
#include <fstream>

int min() {
    std::ifstream file("robot.bmp");
    if (file.good()) {
        std::cout << "File exists!" << std::endl;
    }
    else {
        std::cerr << "File does not exist in the working directory!" << std::endl;
    }
    return 0;
}
