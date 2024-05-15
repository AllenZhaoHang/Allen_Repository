#include <stdio.h>
#include <stdlib.h>

int main() {
	// declare string - as array of 10 char
	char d[10];

	d[0]='S';
	d[1]='i';
	d[2]='l';
	d[3]='i';
	d[4]='c';
	d[5]='o';
	d[6]='n';
	d[7]='\0';  	//final char is NUL (0) which terminates the
			//string and d[8] and d[9] are not initialized
	
	printf("Our string is: |%s|\n",d);

	return 0;
}
