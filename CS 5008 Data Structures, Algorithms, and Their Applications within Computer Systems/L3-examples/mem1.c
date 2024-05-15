#include <stdio.h>
#include <stdlib.h>  //this library contains the malloc/free headers

int main() {
	//declare ptr to int and get memory for it
	int* newInt = (int*)malloc(sizeof(int));
	
	//assign a value to it
	*newInt = 5;

	printf("My new int has value %d\n", *newInt);

	free(newInt);  //releases memory we no longer need

	return 0;
}

