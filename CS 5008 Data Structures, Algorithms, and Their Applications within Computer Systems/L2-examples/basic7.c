#include <stdio.h>

int main() {
   char grade = 'D';

   switch (grade) {
   case ('A'):
      printf("Awesome grade\n");
      break;
   case ('B'):
      printf("Very good\n");
   case ('C'):
      printf("Good\n");
      break;
   case ('D'):
      printf("You passed\n");
      break;
   case ('F'):
      printf("Try again\n");
      break;
   default:
      printf("Invalid input\n");
   }

   printf("Your grade was: %c\n", grade)'

   return 0;
}
