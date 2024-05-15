#include <stdio.h>
#include <stdlib.h>

typedef struct Student {
	int age;
	int id;
	char campus; //B=Boston,F=SF,V=SV,S=Seattle,P=Portland,etc.
} Student_type;

int i;

int main() {
	Student_type myClass[3];

	//initialize it
	myClass[0].age=20;
	myClass[0].id=334455;
	myClass[0].campus='B';

	myClass[1].age=36;
	myClass[1].id=223355;
	myClass[1].campus='P';

	myClass[2].age=28;
	myClass[2].id=112233;
	myClass[2].campus='V';

	for(i=0; i<3; i++) {
		printf("Student number %d is %d years old and from campus %c\n",
		myClass[i].id,myClass[i].age,myClass[i].campus);
	}

	return 0;
}
