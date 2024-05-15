// Hang Zhao
// 3/1/2024
//
// Include our header file for our my_bst.c
#include "my_bst.h"

// Include any other libraries needed
#include <stdio.h>
#include <stdlib.h>

// Function to create a new tree node
bstnode_t *createNode(int data)
{
    bstnode_t *newNode = (bstnode_t *)malloc(sizeof(bstnode_t));
    if (newNode != NULL)
    {
        newNode->data = data;
        newNode->leftChild = NULL;
        newNode->rightChild = NULL;
    }
    return newNode;
}

// Creates a BST
// Returns a pointer to a newly created BST.
// The BST should be initialized with data on the heap.
// The BST fields should also be initialized to default values(i.e. size=0).
bst_t* bst_create(){
    bst_t* myBST= NULL;
    myBST = (bst_t*)malloc(sizeof(bst_t));
    if(myBST == NULL){
        return NULL;
    }
    myBST->size = 0;
    myBST->root = NULL;
    return myBST;
}


// BST Empty
// Check if the BST is empty
// Returns 1 if true (The BST is completely empty)
// Returns 0 if false (the BST has at least one element)
int bst_empty(bst_t* t){
    if(t->size == 0 || t->root == NULL || t == NULL){
        return 1;
    }
    return 0;
}

// Recursive function to add a new node to the BST
// help to recursively visist nodes in the tree and add nodes
int recursive_bst_add(bstnode_t *node, int data)
{
    if (data <= node->data)
    {
        if (node->leftChild == NULL)
        { // Add the new node
            node->leftChild = createNode(data);
            if (node->leftChild == NULL)
            {
                return -1; // Memory allocation failed
            }
            return 1; // Success
        }
        else
        { // Recursively visit the left child
            return recursive_bst_add(node->leftChild, data);
        }
    }
    else
    // data > node->data
    {
        if (node->rightChild == NULL)
        {
            node->rightChild = createNode(data);
            if (node->rightChild == NULL)
            {
                return -1; // Memory allocation failed
            }
            return 1; // Success
        }
        else
        {
            return recursive_bst_add(node->rightChild, data);
        }
    }
}
// Adds a new node containg item to the BST
// The item is added in the correct position in the BST.
//  - If the data is less than or equal to the current node we traverse left
//  - otherwise we traverse right.
// The bst_function returns '1' upon success
//  - bst_add should increment the 'size' of our BST.
// Returns a -1 if the operation fails.
//      (i.e. the memory allocation for a new node failed).
// Your implementation should should run in O(log(n)) time.
//  - A recursive imlementation is suggested.
int bst_add(bst_t *t, int data)
{
    if (t == NULL)
    {
        return -1; // Invalid BST pointer
    }

    if (t->root == NULL)
    {
        t->root = createNode(data);
        if (t->root == NULL)
        {
            return -1; // Memory allocation failed
        }
        t->size = 1; // Initialize size
        return 1;    // Success
    }

    return recursive_bst_add(t->root, data);
}

void printAscending(bstnode_t *node){
    if(node == NULL){
        return;
    }
    printAscending(node->leftChild);
    printf("%d ", node->data);
    printAscending(node->rightChild);
}

void printDescending(bstnode_t *node){
    if(node == NULL){
        return;
    }
    printDescending(node->rightChild);
    printf("%d ", node->data);
    printDescending(node->leftChild);
}

// Prints the tree in ascending order if order = 0, otherwise prints in descending order.
// A BST that is NULL should print "(NULL)"
// It should run in O(n) time.
void bst_print(bst_t *t, int order)
{
    if (NULL == t)
    {
        printf("(NULL)");
    }
    else
    {
        if (order == 0)
        {
            printAscending(t->root);
        }
        else
        {
            printDescending(t->root);
        }
    }
}
int cal_sum(bstnode_t *node)
{
    if (node == NULL)
    {
        return 0;
    }
    return node->data + cal_sum(node->leftChild) + cal_sum(node->rightChild);
}
// Returns the sum of all the nodes in the bst. 
// A BST that is NULL exits the program.
// It should run in O(n) time.
int bst_sum(bst_t *t){
    // A BST that is NULL exits the program.
    if(t == NULL){
        exit(1);
    }
    return cal_sum(t->root);
}

// Recursive function to find the value in the BST
// help to find a value in the tree
int find_value(bstnode_t *node, int value)
{
    if (node == NULL)
    {
        // if the value is not found in the tree return 0
        return 0;
    }
    // if the value is found in the tree return 1
    if (node->data == value)
    {
        return 1;
    }
    // if the value is less than the node value, go to the left child
    if (value < node->data)
    {
        return find_value(node->leftChild, value);
    }
    // if the value is greater than the node value, go to the right child
    else
    {
        return find_value(node->rightChild, value);
    }
}

// Returns 1 if value is found in the tree, 0 otherwise. 
// For NULL tree -- exit the program. 
// It should run in O(log(n)) time.
int bst_find(bst_t * t, int value){
    if(t == NULL){
        exit(1);
    }
    // if more than one value found in the tree return 1, otherwise 0
    return find_value(t->root, value);
}

// Returns the size of the BST
// A BST that is NULL exits the program.
// (i.e. A NULL BST cannot return the size)
unsigned int bst_size(bst_t* t){
    if(t == NULL){
        exit(1);
    }
    return t->size;
}

void free_tree(bstnode_t *node){
    if(node == NULL){
        return;
    }
    free_tree(node->leftChild);
    free_tree(node->rightChild);
    free(node);
}

// Free BST
// Removes a BST and ALL of its elements from memory.
// This should be called before the proram terminates.
void bst_free(bst_t* t){
    // use recusion
    if(t == NULL){
        return;
    }
    free_tree(t->root);
    free(t);
}