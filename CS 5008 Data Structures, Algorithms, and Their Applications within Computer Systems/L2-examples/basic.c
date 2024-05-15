#include <stdio.h>

int main() {
   
   // declare x as an integer and initialize it to 5
   int x = 5;
   printf("first x: %d\n",x);

   {
   // declare x as a new integer inside this scope and initialize it to 10
   int x = 10;
   printf("second x: %d\n",x);
   }

   //go back to the first x
   printf("third x: %d\n",x);

   //assign a new value to x
   x = 7;
   printf("fourth x: %d\n",x);

   return 0;
}
