#include <stdio.h>
#include <stdlib.h>

typedef struct Student {
	int age;
	int id;
	char campus; //B=Boston,F=SF,V=SV,S=Seattle,P=Portland,etc.
} Student_type;

int main() {
	//declare class roster of 3 students
	Student_type myClass[3];

	//now let's add a pointer to a student
	Student_type *thisStudent;

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

	thisStudent = &(myClass[1]);

	printf("Student number %d is %d years old and from campus %c\n",
		thisStudent->id,thisStudent->age,thisStudent->campus);
	
	return 0;
}
