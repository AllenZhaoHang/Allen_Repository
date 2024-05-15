// Task: Implement the divide-and-conquer algorithm 
// for calculating mixed-up-ness score

// =================== Libraries ==================
#include <stdio.h> // Include file for standard input/output

// =============== Helper Functions ===============
// TODO: Implement your helper functions here
// Function to merge two sorted subarrays and count inversions
int merge(int arr[], int left, int mid, int right)
{
  int temp[right - left + 1];
  int i = left, j = mid + 1;
  int k = 0;
  int inversions = 0; // Variable to store the number of inversions

  // Merge the two subarrays into a temporary array
  while (i <= mid && j <= right)
  {
    if (arr[i] <= arr[j])
    {
      temp[k++] = arr[i++];
    }
    else
    {
      // If arr[i] is greater than arr[j], it forms inversions with all elements after arr[i] to arr[mid]
      inversions += (mid - i + 1);
      temp[k++] = arr[j++];
    }
  }

  // Copy the remaining elements of the left subarray
  while (i <= mid)
  {
    temp[k++] = arr[i++];
  }

  // Copy the remaining elements of the right subarray
  while (j <= right)
  {
    temp[k++] = arr[j++];
  }

  // Copy the merged elements back to the original array
  for (i = left, k = 0; i <= right; i++, k++)
  {
    arr[i] = temp[k];
  }

  return inversions;
}

// Function to perform merge sort and count inversions
int mergeSort(int arr[], int left, int right)
{
  int inversions = 0;
  if (left < right)
  {
    int mid = left + (right - left) / 2;

    // Recursive calls to sort the left and right subarrays
    inversions += mergeSort(arr, left, mid);
    inversions += mergeSort(arr, mid + 1, right);

    // Merge the sorted subarrays and count inversions
    inversions += merge(arr, left, mid, right);
  }
  return inversions;
}

// Provided below is a mixed-up-ness score.
// Name: mixedupness
// Input(s):
//    (1) 'array' is a pointer to an integer address. 
//         This is the start of some 'contiguous block of memory' that we will sort.
//    (2) 'size' tells us how big the array of data is we are sorting.
// Output: The mixedupness score of the original array
int mixedupness(int* array, unsigned int size){
  int inversions = mergeSort(array, 0, size - 1);
  return inversions;
}


// Input: A pointer to an array (i.e. the array itself points to the first index)
//        The size of the array (Because we do not know how big the array is automatically)
void printIntArray(int* array, unsigned int size){
  unsigned int i; // Note: 'unsigned int' is a datatype for storing positive integers.
  for(i = 0; i < size; i=i+1){
    printf("%d ",array[i]);
  }
  printf("\n");
}

int main(){
  // Some test data sets.
  int dataset1[] = {0,1,2,3,4,5,6,7,8,9,10};
  int dataset2[] = {100,87,65,10,54,42,27,37};
  int dataset3[] = {0,3,2,1,4,7,6,5,8,9,10};
  int dataset4[] = {10,9,8,7,6,5,4,3,2,1,0};
  int dataset5[] = {100,201,52,3223,24,55,623,75,8523,-9,150};
  int dataset6[] = {-1,1,2,-3,4,5,-6,7,8,-9,10};

  // Print out an array
  printf("dataset 1: ");
  printIntArray(dataset1, 11);
  printf("dataset 2: ");
  printIntArray(dataset2, 8);
  printf("dataset 3: ");
  printIntArray(dataset3, 11);
  printf("dataset 4: ");
  printIntArray(dataset4, 11);
  printf("dataset 5: ");
  printIntArray(dataset5, 11);
  printf("dataset 6: ");
  printIntArray(dataset6, 11);
  printf("\n");
  
  // TODO: Change these so that they print 
  // both the expected score and the calculated score
  printf("dataset 1 expected = %d, actual = %d\n", 0, mixedupness(dataset1, 11));
  printf("dataset 2 expected = %d, actual = %d\n", 23, mixedupness(dataset2, 8));
  printf("dataset 3 expected = %d, actual = %d\n", 6, mixedupness(dataset3, 11));
  printf("dataset 4 expected = %d, actual = %d\n", 55, mixedupness(dataset4, 11));
  printf("dataset 5 expected = %d, actual = %d\n", 27, mixedupness(dataset5, 11));
  printf("dataset 6 expected = %d, actual = %d\n", 18, mixedupness(dataset6, 11));

  return 1;
}
