cmake_minimum_required(VERSION 3.10)
project(Project4AR)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 11)

# Find OpenCV
find_package(OpenCV REQUIRED)

# Include directories for OpenCV
include_directories(${OpenCV_INCLUDE_DIRS})

# Add executable files
add_executable(detectCorners detectCorners.cpp)
add_executable(detectCalibrationImages detectCalibrationImages.cpp)
add_executable(calibrateCameraExample calibrateCameraExample.cpp)
# add_executable(estimatePose estimatePose.cpp)
# add_executable(project3DPoints project3DPoints.cpp)
add_executable(cupAR cupAR.cpp)
add_executable(detect_features detect_features.cpp)
add_executable(ar_two_cups ar_two_cups.cpp)
add_executable(ar_3d_pointcloud ar_3d_pointcloud.cpp)
# Link OpenCV, OpenGL, and FreeGLUT libraries
target_link_libraries(detectCorners ${OpenCV_LIBS})
target_link_libraries(detectCalibrationImages ${OpenCV_LIBS})
target_link_libraries(calibrateCameraExample ${OpenCV_LIBS})
# target_link_libraries(estimatePose ${OpenCV_LIBS} OpenGL::GL ${FREEGLUT_LIBRARY})
# target_link_libraries(project3DPoints ${OpenCV_LIBS} OpenGL::GL ${FREEGLUT_LIBRARY})
target_link_libraries(cupAR ${OpenCV_LIBS})
target_link_libraries(detect_features ${OpenCV_LIBS})
target_link_libraries(ar_two_cups ${OpenCV_LIBS})
target_link_libraries(ar_3d_pointcloud ${OpenCV_LIBS})