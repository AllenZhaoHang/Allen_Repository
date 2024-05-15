// Compile with: gcc -g selection.c -o selection
// Run with: ./selection

#include <stdio.h> // Include file for standard input/output
#include <stdlib.h> // so we can use atoi()
#include <time.h>   // so we can use time_t and clock_gettime()

#define EXPERIMENT 0 // we will use this for Part 4 of this lab

// =============== Helper Functions ===============
// Swaps two numbers in an array
// Input: The 'address of' an index into an array for positions in an array.
void swap(int* a, int* b){
    // TODO: Swap two integers in an array.
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Returns the minimum integer from a range in an array
// Input: array - An array of integers
//        start - Where to start looking in an array
//        stop - End of where to search. Typically the 'size' of the array.
// Output: The index in an array of the minimum value between a range [start,stop]
int findMinimum(int* array, int start, int stop){
    // TODO: Iterate through a subset of the array and find the minimum value.
    //       Return the index of that minimum value.
    int min = start;
    for(int i = start+1; i < stop; i++){
        if(array[i] < array[min]){
            min = i;
        }
    }
    return min;    
}

// Input: A pointer to an array (i.e. the array itself points to the first index)
//        The size of the array (Because we do not know how big the array is automatically)
void printIntArray(int* array, unsigned int size){
  unsigned int i; // Note: 'unsigned int' is a datatype for storing positive integers.
  for(i = 0 ; i < size ; i++){
    printf("%d ", array[i]);
  }
  printf("\n");
}

// =============== Sort Function ===============
// Provided below is a sort function. I have also
// provided a template for how to document functions
// to help organize your code.
// Name: sort
// Input(s):
//  - 'array' is a pointer to an integer address. 
//     This is the start of some 'contiguous block of memory' that we will sort.
//  - 'size' tells us how big the array of data is we are sorting.
// Output: No value is returned, but 'array' should be modified to store a sorted array of numbers.
void sortIntegers(int* array, unsigned int size){
    // TODO: Implement selection sort
    for(int i = 0; i < size-1; i++){
        int min = findMinimum(array, i, size);
        swap(&array[i], &array[min]);
    }
}



// =============== Main Functions ===============
int main(int argc, char* argv[]){

#if EXPERIMENT==1
  // Some test data sets.
  int dataset1[] = {0,1,2,3,4,5,6,7,8,9,10};
  int dataset2[] = {10,9,8,7,6,5,4,3,2,1,0};
  int dataset3[] = {0,3,2,1,4,7,6,5,8,9,10};
  int dataset4[] = {2,1,1,1,1,1,1,1,1,1,1};
  int dataset5[] = {100,201,52,3223,24,55,623,75,8523,-9,150};
  int dataset6[] = {-1,1,2,-3,4,5,-6,7,8,-9,10};
  
  // Sort our integer array
  sortIntegers(dataset1, 11);
  sortIntegers(dataset2, 11);
  sortIntegers(dataset3, 11);
  sortIntegers(dataset4, 11);
  sortIntegers(dataset5, 11);
  sortIntegers(dataset6, 11);
  
  // Print out an array
  printIntArray(dataset1, 11);
  printIntArray(dataset2, 11);
  printIntArray(dataset3, 11);
  printIntArray(dataset4, 11);
  printIntArray(dataset5, 11);
  printIntArray(dataset6, 11);

#else

  if (argc != 2) {
    printf("One argument expected: ./selection 1000\n");
    return 1;
  }

  // Convert the argument of the program into an integer
  const int size = atoi(argv[1]);
  // Generate a random seed
  time_t t;
  srand((unsigned)time(&t));
  // Allocate memory
  int* random = (int*)malloc(sizeof(int)*size);

  // Populate our test data set
  for(int i = 0 ; i < size ; i++) {
    // Generate random values from 0 to 99
    random[i] = rand()%size; 
  }

  // You can uncomment if you'd like to see the size sorted
  // printf("Before the sort: ");
  // printIntArray(random, size);

  // Setup timers  
  struct timespec begin, end;
  // Get the time before we start
  clock_gettime(CLOCK_MONOTONIC, &begin);
  // Perform the sort
  sortIntegers(random,size);
  // Get the time after we are done
  clock_gettime(CLOCK_MONOTONIC, &end);

  double time_taken = (end.tv_nsec - begin.tv_nsec) / 1000000000.0 +
            (end.tv_sec  - begin.tv_sec);
  printf ("Total time = %f seconds\n", time_taken);

  // Confirm the sort worked
  // printf("After the sort: ");
  // printIntArray(random, size);
  
  // Free our random array
  free(random);

#endif

  return 0;
}
