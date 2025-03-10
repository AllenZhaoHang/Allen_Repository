// File: csv_util.h
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Utility functions for reading and writing CSV files in a specific format.
// Each line of the CSV file contains a filename in the first column followed by numeric data.
// (Based on Bruce A. Maxwell¡¯s code with minor modifications.)

#ifndef CSV_UTIL_H
#define CSV_UTIL_H

#include <vector>

/*
  Appends a line to a CSV file.
  - filename: the CSV file name.
  - image_filename: the name of the image.
  - image_data: a vector of float features to be written.
  - reset_file: if non-zero, opens the file in write mode (clearing any existing contents).
  Returns 0 on success or a non-zero value in case of error.
*/
int append_image_data_csv(char* filename, char* image_filename, std::vector<float>& image_data, int reset_file = 0);

/*
  Reads a CSV file whose first column is a filename (string) and the remaining columns are float numbers.
  - filename: the CSV file name.
  - filenames: (output) a vector of char* holding each image filename.
  - data: (output) a 2D vector of floats holding the numeric data.
  - echo_file: if non-zero, the file contents are printed as they are read.
  Returns 0 on success or a non-zero value if something goes wrong.
*/
int read_image_data_csv(char* filename, std::vector<char*>& filenames, std::vector<std::vector<float>>& data, int echo_file = 0);

#endif
