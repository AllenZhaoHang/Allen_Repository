#include <stdio.h>

int main() {
   
   // declare an array: 5 sequential locations in memory
   // each holds an integer
   int numbersILike[5];
   int i;

   // first location in the array is location 0: [0]
   numbersILike[0] = 1;
   numbersILike[1] = 17;
   numbersILike[2] = 999;
   numbersILike[3] = 0xFF;  // a hexidecimal constant - base 16
   numbersILike[4] = 100000;

   // print out pairs of numbers as decimals
   for (i=0; i<5; i++) {
      printf("%d> %d\n", i, numbersILike[i]);
   }

   // print out pairs of numbers as hexidecimals
   for (i=0; i<5; i++) {
      printf("%d> %x\n", i, numbersILike[i]);
   }

   return 0;
}
