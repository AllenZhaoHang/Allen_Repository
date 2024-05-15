// Compile with: gcc -Wall print_pascal.c
// Run with: ./a.out

#include <stdio.h>

// This is a simple implementation of the Pascal Triangle
// that you would find quickly using a Google search.
// This particular version was modified from:
// https://www.programiz.com/c-programming/examples/pyramid-pattern
//
// We are providing it to you so that you can use it to
// help you determine what the expected results of your
// dynamic programming solutions should be
int main() {
   long long coef = 1;
   int rows, i, j;
   printf("Enter the number of rows: ");
   scanf("%d", &rows);
   for (i = 0; i < rows; i++) {
      for (j = 0; j <= i; j++) {
         if (j == 0 || i == 0)
            coef = 1;
         else
            coef = coef * (i - j + 1) / j;
         printf("%llu ", coef);
      }
      printf("\n");
   }
   return 0;
}
