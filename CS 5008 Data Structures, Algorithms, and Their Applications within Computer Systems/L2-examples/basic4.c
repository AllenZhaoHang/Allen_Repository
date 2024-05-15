#include <stdio.h>

int main() {
   
   int countdown = 10;

   // while loop
   while (countdown > 0) {
      printf("> %d\n", countdown);

      // same as countdown = countdown - 1
      countdown--;
   }

   return 0;
}
