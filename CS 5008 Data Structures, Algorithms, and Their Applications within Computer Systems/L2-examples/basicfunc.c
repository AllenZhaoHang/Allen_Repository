#include <stdio.h>

// declare add as a function that takes two ints and returns an int
// like variables, functions must be declared before being used
int add (int x, int y) {
	return x+y;
}

int main() {
   
   // call to add as an argument to printf
   printf("2 + 3 = %d\n",add(2,3));

   return 0;
}
