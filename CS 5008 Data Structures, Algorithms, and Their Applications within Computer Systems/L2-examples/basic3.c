#include <stdio.h>

int main() {
   
   // if statements
   if (0 == 1) {
      printf("0==1 ... wait that isnt true!\n");
      printf("the `==` operator tests for equality\n");
   } else {
      printf("0!=1\n");
      printf("the '!=' operator test for inequality\n");
   }

   int x;
   for (x = 0; x < 10; x = x+1) {
      printf("> %d\n", x);
   }
   return 0;
}
