#include <stdio.h>
#include <stdlib.h>  //this library contains the malloc/free headers

int main() {
	//declare ptr to array of 4 int and get memory for it
	int* newArray = (int*)malloc(4*sizeof(int));
	int i;

	//assign a value to it
	newArray[0] = 5;
	newArray[1] = 10;
	newArray[2] = 15;
	newArray[3] = 20;

	for(i=0; i<4; i++) {
		printf("newArray[%d] has value %d\n", i, newArray[i]);
	}

	free(newArray);  //releases memory we no longer need

	return 0;
}

