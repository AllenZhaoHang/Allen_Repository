// File: main.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Main entry point for Project 2: Content-based Image Retrieval.
// Selects and runs a specific task or extension based on the command-line argument.

#include <iostream>
#include <string>
#include "features.h"

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Usage: ./cbir <task1|task2|task3|task4|task5|task6|task7|bluebin>" << std::endl;
        return 1;
    }

    std::string task = argv[1];
    if (task == "task1") {
        runTask1();
    }
    else if (task == "task2") {
        runTask2();
    }
    else if (task == "task3") {
        runTask3();
    }
    else if (task == "task4") {
        runTask4();
    }
    else if (task == "task5") {
        runTask5();
    }
    else if (task == "task6") {
        runTask6(); 
    }
    else if (task == "task7") {
        runTask7();
    }
    else if (task == "bluebin") {
        runBlueBinRetrieval();
    }
    else {
        std::cout << "Invalid task. Usage: ./cbir <task1|task2|task3|task4|task5|task6|task7|bluebin>" << std::endl;
        return 1;
    }

    return 0;
}
