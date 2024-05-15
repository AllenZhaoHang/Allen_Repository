// Compile with: gcc -g bubblesort.c -o bubblesort
// Run with: ./bubblesort

// C-Standard Libraries
#include <stdio.h> // Include file for standart input/output
#include <stdlib.h>
#include <time.h> // Time functions 

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

// Name:    printIntArray
// Desc:    Prints out an integer array
// param(1):A pointer to an array (i.e. the array 
//          itself points to the first index)
// param(2) The size of the array (Because we do 
//          not know how big the array is automatically)
void printIntArray(int* array, unsigned int size){
    // Note: 'unsigned int' is a datatype for storing positive integers.
    unsigned int i;
    for(i = 0; i < size; i=i+1){
        printf("%d ",array[i]);
    }
    printf("\n");
}


// =============== Sort Function ===============
// Name: bubblesort
// Desc: O(n^2) comparison sort
// param(1): 'array' is a pointer to an integer address. 
//           This is the start of some 'contiguous block of memory' 
//           that we will sort.
// param(2)  'size' tells us how big the array of 
//           data is we are sorting.
// Output:   No value is returned, but 'array' should 
//           be modified to store a sorted array of size.
void bubblesort(int* array, unsigned int size){
    for(int i=0; i < size-1; i++){
        for(int j=0; j < size-i-1; j++){
            // Compare adjacent items
            if(array[j] > array[j+1]){
                swap(&array[j],&array[j+1]);
            }
        }
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
  bubblesort(dataset1, 11);
  bubblesort(dataset2, 11);
  bubblesort(dataset3, 11);
  bubblesort(dataset4, 11);
  bubblesort(dataset5, 11);
  bubblesort(dataset6, 11);
  
  // Print out an array
  printIntArray(dataset1, 11);
  printIntArray(dataset2, 11);
  printIntArray(dataset3, 11);
  printIntArray(dataset4, 11);
  printIntArray(dataset5, 11);
  printIntArray(dataset6, 11);

#else

  if (argc != 2) {
    printf("One argument expected: ./bubblesort 1000\n");
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
  #include <time.h>

  clock_gettime(CLOCK_MONOTONIC, &begin);
  // Perform the sort
  bubblesort(random, size);
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
