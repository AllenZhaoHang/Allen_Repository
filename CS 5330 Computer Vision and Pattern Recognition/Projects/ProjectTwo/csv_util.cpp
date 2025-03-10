// File: csv_util.cpp
// Author: Hang Zhao
// Date: 2025-02-02
// Description: Implementation of utility functions for reading and writing CSV files.
// Based on Bruce A. Maxwell¡¯s original code for CS 5330 Computer Vision (Spring 2021).
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include "csv_util.h"
#include "opencv2/opencv.hpp"  // retained if any OpenCV types/functions are needed

// Helper function to read a string from a CSV file until a comma or end-of-line.
int getstring( FILE *fp, char os[] ) {
  int p = 0;
  int eol = 0;
  for(;;) {
    char ch = fgetc( fp );
    if( ch == ',' ) {
      break;
    }
    else if( ch == '\n' || ch == EOF ) {
      eol = 1;
      break;
    }
    os[p] = ch;
    p++;
  }
  os[p] = '\0';
  return eol;
}

// Helper function to read one float value from a CSV file.
int getfloat(FILE *fp, float *v) {
  char s[256];
  int p = 0;
  int eol = 0;
  for(;;) {
    char ch = fgetc( fp );
    if( ch == ',' ) {
      break;
    }
    else if(ch == '\n' || ch == EOF) {
      eol = 1;
      break;
    }
    s[p] = ch;
    p++;
  }
  s[p] = '\0';
  *v = static_cast<float>(atof(s));
  return eol;
}

int append_image_data_csv( char *filename, char *image_filename, std::vector<float> &image_data, int reset_file ) {
  char buffer[256];
  char mode[8];
  FILE *fp;

  strcpy(mode, "a");
  if( reset_file ) {
    strcpy( mode, "w" );
  }
  
  fp = fopen( filename, mode );
  if(!fp) {
    printf("Unable to open output file %s\n", filename );
    return -1;
  }

  // Write the filename and the feature vector to the CSV file.
  strcpy(buffer, image_filename);
  fwrite(buffer, sizeof(char), strlen(buffer), fp );
  for(size_t i = 0; i < image_data.size(); i++) {
    char tmp[256];
    sprintf(tmp, ",%.4f", image_data[i] );
    fwrite(tmp, sizeof(char), strlen(tmp), fp );
  }
  fwrite("\n", sizeof(char), 1, fp);
  fclose(fp);
  return 0;
}

int read_image_data_csv( char *filename, std::vector<char *> &filenames, std::vector<std::vector<float>> &data, int echo_file ) {
  FILE *fp;
  float fval;
  char img_file[256];

  fp = fopen(filename, "r");
  if( !fp ) {
    printf("Unable to open feature file %s\n", filename);
    return -1;
  }

  printf("Reading %s\n", filename);
  while(true) {
    std::vector<float> dvec;
    if( getstring( fp, img_file ) )
      break;
    // Read all feature values for the current line.
    while(true) {
      int eol = getfloat(fp, &fval);
      dvec.push_back(fval);
      if(eol)
        break;
    }
    data.push_back(dvec);
    char *fname = new char[strlen(img_file)+1];
    strcpy(fname, img_file);
    filenames.push_back(fname);
    if(feof(fp))
      break;
  }
  fclose(fp);
  printf("Finished reading CSV file\n");

  if(echo_file) {
    for(size_t i = 0; i < data.size(); i++) {
      for(size_t j = 0; j < data[i].size(); j++) {
        printf("%.4f  ", data[i][j] );
      }
      printf("\n");
    }
    printf("\n");
  }

  return 0;
}
