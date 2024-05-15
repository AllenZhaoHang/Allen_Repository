// Hang Zhao
// 3/29/2024
// Lab09
//
// Compile with: gcc -Wall pascal.c -o pascal
// Run with: ./pascal 32

#include <stdio.h>
#include <stdlib.h>

#define LARGEST_TRIANGLE 33
// Function to calculate the binomial coefficient using memoization
int binomialCoeff(int n, int k, int **memo)
{
   if (k == 0 || k == n)
   {
      return 1;
   }
   if (memo[n][k] != -1)
   {
      return memo[n][k];
   }
   memo[n][k] = binomialCoeff(n - 1, k - 1, memo) + binomialCoeff(n - 1, k, memo);
   return memo[n][k];
}
// calculate and return the i-th row of Pascal's Triangle
// rowIndex = the index of the row that should be calculated
// returnSize = the size of the row that was calculated
// returns a pointer to an array of size `returnSize`,
//    assume that the caller calls free on the returned array
//
// coincidentally, this problem is the same as one of the problems
// on LeetCode: https://leetcode.com/problems/pascals-triangle-ii/
int *getRow(int rowIndex, int *returnSize)
{
   *returnSize = rowIndex + 1; // The size of the n-th row is n+1

   // Allocate memory for the row
   int *row = (int *)malloc((*returnSize) * sizeof(int));
   if (row == NULL)
   {
      return NULL;
   }

   // Allocate memory for the memoization table
   int **memo = (int **)malloc((rowIndex + 1) * sizeof(int *));
   for (int i = 0; i <= rowIndex; i++)
   {
      memo[i] = (int *)malloc((i + 1) * sizeof(int));
      if (memo[i] == NULL)
      {
         // Free the allocated memory and return NULL if allocation fails
         for (int j = 0; j < i; j++)
         {
            free(memo[j]);
         }
         free(memo);
         free(row);
         return NULL;
      }
      for (int j = 0; j <= i; j++)
      {
         memo[i][j] = -1; // Initialize the memoization table with -1
      }
   }

   // Calculate the n-th row using the memoization table
   for (int i = 0; i <= rowIndex; i++)
   {
      row[i] = binomialCoeff(rowIndex, i, memo);
   }

   // Free the memoization table memory
   for (int i = 0; i <= rowIndex; i++)
   {
      free(memo[i]);
   }
   free(memo);

   return row;
}

int main(int argc, char* argv[]) {
   // Make sure that there is one argument
   if (argc != 2) {
      printf("One argument expected: ./pascal 42\n");
      return 1;
   }

   // Convert the argument of the program into an integer
   // and make sure that it is between 0 and LARGEST_TRIANGLE - 1
   const int row = atoi(argv[1]);
   if (row < 0 || row > LARGEST_TRIANGLE - 1) {
      printf("row must between 0 and %d (inclusive)\n", LARGEST_TRIANGLE - 1);
      return 1;
   }

   int size = 0;
   int* row_values = getRow(row, &size);
   int i;

   printf("Row %d of Pascal's Triangle\n", row);
   for(i = 0 ; i < size ; i++) {
      printf("%d ", row_values[i]);
   }
   printf("\n");

   // free the memory that was returned from function
   free(row_values);
   return 0;
}
