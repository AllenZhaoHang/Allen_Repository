#include <stdio.h>
#include <stdlib.h>  //this library contains the malloc/free headers

char s1[80] = "**********";
char s2[80] = "@@@@@@@@@@";
int  i3     = -9999999;
FILE* fp;

int main() {

	fp = fopen("ex1.txt","r");

	if(fp != NULL) {
		if(feof(fp) == 0) {
			fscanf(fp, "%s %s %i %*s", s1, s2, &i3);
			printf("the input was: ||%s %s %i||\n", s1, s2, i3);
			fclose(fp);
		}
	}

	return 0;
}
