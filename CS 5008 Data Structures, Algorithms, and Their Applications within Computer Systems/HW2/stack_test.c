// Note: This is not an exhaustive test suite, but gives you the idea
//       of some tests you might want to create.
//       Adding more tests and slowly making them more and more complicated
//       as you develop your library is recommended.
//
// Compile this assignment with: gcc -g -Wall stack_test.c -o stack_test
//
// Run with: ./stack_test
//
// This is a way to test your code.
//
// Include parts of the C Standard Library
// These have been written by some other really
// smart engineers.
#include <stdio.h>  // For IO operations
#include <stdlib.h> // for malloc/free

// Our library that we have written.
// Also, by a really smart engineer!
#include "mystack.h"
// Note that we are locating this file
// within the same directory, so we use quotations
// and provide the path to this file which is within
// our current directory.


// A sample test of your program
// You can add as many unit tests as you like
// We will be adding our own to test your program.


// Tests the capacity of a stack
int unitTest1(int status){
    int passed = 0;
    
    stack_t* test_s = create_stack(32);
    if(32==test_s->capacity){
        passed =1;
    }
    
    free_stack(test_s);

    return passed;
}

// Enqueu several items into a stack and test the size
int unitTest2(int status){
    int passed = 0;
    
    stack_t* test_s = create_stack(MAX_DEPTH);
    stack_enqueue(test_s,1);
    stack_enqueue(test_s,2);
    stack_enqueue(test_s,3);
    stack_enqueue(test_s,4);
    stack_enqueue(test_s,5);
    stack_enqueue(test_s,6);
    stack_enqueue(test_s,7);
    stack_enqueue(test_s,8);
    stack_enqueue(test_s,9);
    stack_enqueue(test_s,10);
    
    if(10==stack_size(test_s)){
        passed =1;
    }

    free_stack(test_s);

    return passed;
}

// Tests enqueuing and fully dequeing a stack
int unitTest3(int status){
    int passed = 0;
    
    stack_t* test_s = create_stack(32);
    int i =0;
    for(i=0; i < 32; i++){
        stack_enqueue(test_s,1);
    }
    for(i=0; i < 32; i++){
        stack_dequeue(test_s);
    }
    
    if(0==stack_size(test_s)){
        passed =1;
    }

    free_stack(test_s);

    return passed;
}

// Tests enqueuing and fully dequeing a stack multiple times
int unitTest4(int status){
    int passed = 0;
    
    stack_t* test_s = create_stack(32);
    int i =0;
    for(i=0; i < 32; i++){
       stack_enqueue(test_s,1);
    }
    for(i=0; i < 32; i++){
        stack_dequeue(test_s);
    }
    for(i=0; i < 32; i++){
        stack_enqueue(test_s,1);
    }
    for(i=0; i < 32; i++){
        stack_dequeue(test_s);
    }
    if(0==stack_size(test_s)){
        passed =1;
    }
    
    free_stack(test_s);

    return passed;
}

// Simple enqueu and deque stack test
// Also confirms that a stack is full
int unitTest5(int status){
    int passed = 0;
    
    stack_t* test_s = create_stack(1);
    stack_enqueue(test_s,1);
    if(1==stack_full(test_s)){
        passed = 1;
    }else{
        free_stack(test_s);
        return 0;
    }
    
    stack_dequeue(test_s);
    if(0==stack_full(test_s)){
        passed = 1;
    }else{
        passed = 0;
    }
       
    free_stack(test_s);

    return passed;
}


// TODO: Add tests here
int (*unitTests[])(int)={
    unitTest1,
    unitTest2,
    unitTest3,
    unitTest4,
    unitTest5,
    NULL
};

// ====================================================
// ================== Program Entry ===================
// ====================================================
int main(){
    unsigned int testsPassed = 0;
    // List of Unit Tests to test your data structure
    int counter =0;
    while(unitTests[counter]!=NULL){
	    printf("========unitTest %d========\n",counter);
        if(1==unitTests[counter](1)){
		    printf("passed test\n");
    		testsPassed++;	
	    }else{
		    printf("failed test, missing functionality, or incorrect test\n");
	    }
        counter++;
    }

    printf("%d of %d tests passed\n",testsPassed,counter);

    return 0;
}
