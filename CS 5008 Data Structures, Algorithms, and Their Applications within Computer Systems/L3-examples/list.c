#include <stdio.h>
#include <stdlib.h>

//define the node type
typedef struct nd {
	int data;
	struct nd* next;
} node;

//declare head of list and a temporary pointer
node* head = NULL;
node* temp = NULL;

//define a function to create a new node when you give it a data parameter
node* newNode(int d) {
	node* temp;

	temp = (node*)malloc(sizeof(node));
	temp->data = d;
        temp->next = NULL;

	return temp;
}

//add a node (given in paramter) to the front of the list
void addInFront(node* n) {
	if (n != NULL) {
		n->next = head;
		head = n;
	} else {
		printf("Error: attempt to add a null node\n");
	}

	return;
}

//remove the node at the front of the list and return it
node* removeFromFront() {
	node* n = NULL;

	if (head != NULL) {
		n = head;
		head = head->next;
		n->next = NULL;
	} else {
		n = NULL;
		printf("Error: attempt to remove a null node\n");
	}

	return n;
}

int main () {

	//add 3 nodes to the list with values 1, 2, 3
	temp = newNode(1);
	addInFront(temp);
	printf("added %d\n",1);
                                 
	temp = newNode(2);
	addInFront(temp);
	printf("added %d\n",2);

	temp = newNode(3);
	addInFront(temp);
	printf("added %d\n\n",3);

	//remove each of the nodes you added, printing their data values
	temp = removeFromFront();
	printf("removed %d\n", temp->data);
                                                                
	temp = removeFromFront();
	printf("removed %d\n", temp->data);
                                                      
	temp = removeFromFront();
	printf("removed %d\n", temp->data);

	return 0;
}

