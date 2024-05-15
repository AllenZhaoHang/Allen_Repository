// Hang Zhao
// 2/2/2024
// Homework Assignment 3
//
// Compile this assignment with: gcc -g -Wall main.c -o main
// Use this file to implement testing for your
// doubly linked list implementation
//
// Include parts of the C Standard Library
// These have been written by some other really
// smart engineers.
#include <stdio.h>  // For IO operations
#include <stdlib.h> // for malloc/free
// Our library that we have written.
// Also, by a really smart engineer!
#include "my_dll.h"
// Note that we are locating this file
// within the same directory, so we use quotations
// and provide the path to this file which is within
// our current directory.



// ====================================================
// ================== Program Entry ===================
// ====================================================
// Set up and tear down functions for tests
void setUp(void) {}
void tearDown(void) {}

// Test create_dll function
int unitTest1(int status)
{
    int passed = 0;
    dll_t* myDLL = create_dll();
    if (myDLL != NULL && 0 == dll_size(myDLL))
    {
        passed = 1;
    }
    free_dll(myDLL);
    return passed;
}

// Test dll_push_front function
int unitTest2(int status)
{
    int passed = 0;
    dll_t* myDLL = create_dll();
    dll_push_front(myDLL, 42);
    if (1 == dll_size(myDLL)&&42==dll_get(myDLL, 0)){
        passed = 1;
    }

    free_dll(myDLL);
    return passed;
}

// Test dll_push_back function
int unitTest3(int status)
{
    int passed = 0;
    dll_t* myDLL = create_dll();
    dll_push_back(myDLL, 42);
    if (dll_size(myDLL) == 1 && dll_get(myDLL, 0) == 42){
        passed = 1;
    }

    free_dll(myDLL);
    return passed;
}

int (*unitTests[])(int) = {
    unitTest1,
    unitTest2,
    unitTest3,
    NULL};

int main() {
    unsigned int testsPassed = 0;
    // List of Unit Tests to test your data structure
    int counter = 0;
    while (unitTests[counter] != NULL)
    {
        printf("========unitTest %d========\n", counter);
        if (1 == unitTests[counter](1))
        {
            printf("passed test\n");
            testsPassed++;
        }
        else
        {
            printf("failed test, missing functionality, or incorrect test\n");
        }
        counter++;
    }

    printf("%d of %d tests passed\n", testsPassed, counter);

    return 0;
}