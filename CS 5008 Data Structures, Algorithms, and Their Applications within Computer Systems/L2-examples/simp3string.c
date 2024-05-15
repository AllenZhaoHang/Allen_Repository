#include <stdio.h>
#include <stdlib.h>

int main() {
	// declare string - as array of 10 char -- and initialize it
	char d[10]="Silicon";

	//d[8] and d[9] are still not initialized
	
	printf("Our string is: |%s|\n",d);

	return 0;
}
