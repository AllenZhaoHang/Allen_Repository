// Hang Zhao
// 3/1/2024
//
// =================== Support Code =================
// Binary Search Tree ( BST ).
//
// - Implement each of the functions to create a working BST.
// - Do not change any of the function declarations
//   - (i.e. bst_t* bst_create() should not have additional arguments)
// - You should not have any 'printf' statements in your BST functions other than the bst_print function. 
//   - (You may consider using these printf statements to debug, but they should be removed from your final version)
// - You may add any helper functions that you think you need (if any, or otherwise for debugging)
// ==================================================
#ifndef MYBST_H
#define MYBST_H

// Create a node data struct to store data within
// our BST. In our case, we will stores 'integers'
typedef struct bstnode{
    int data;               // data each node holds
    struct bstnode* leftChild; // pointer to left child (if any)
    struct bstnode* rightChild;// pointer to right child (if any)
} bstnode_t;

// Our BST data structure
// Our BST holds a pointer to the root node in our BST.
typedef struct bst{
    unsigned int size;  // Size keeps track of how many items are in the BST.
                        // Size should be incremented when we add.
    bstnode_t* root;    // root points to the root node in our BST.
} bst_t;

// Function declarations.
// When we declare the functions in the .h file
// it is a 'promise' to the compiler that the code
// for the function will be found somewhere.
//
// In our case, when we link in the my_bst.c file, then
// the implementations of the functions will be found.
bst_t* bst_create();
int bst_empty(bst_t* t);
int bst_add(bst_t* t, int item);
void bst_print(bst_t *t, int order);
int bst_sum(bst_t *t);
int bst_find(bst_t * t, int value);
unsigned int bst_size(bst_t* t);
void bst_free(bst_t* t);

#endif
