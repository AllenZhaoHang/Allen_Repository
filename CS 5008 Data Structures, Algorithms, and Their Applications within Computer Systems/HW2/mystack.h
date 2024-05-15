// Name: Hang Zhao
// Date: 1/26/2024
// HW2 CS5008 Spring 2024 mystack.h
#include <stdio.h>
#include <stdlib.h>

#ifndef MYSTACK_H
#define MYSTACK_H

// Stores the maximum 'depth' of our stack.
// Our implementation enforces a maximum depth of our stack.
// (i.e. capacity cannot exceed MAX_DEPTH for any stack)
#define MAX_DEPTH 32

// Create a node data structure to store data within
// our stack. In our case, we will stores 'integers'
typedef struct node
{
    int data;
    struct node *next;
} node_t;

// Create a stack data structure
// Our stack holds a single pointer to a node, which
// is a linked list of nodes.
typedef struct stack
{
    int count;             // count keeps track of how many items
                           // are in the stack.
    unsigned int capacity; // Stores the maximum size of our stack
    node_t *head;          // head points to a node on the top of our stack.
} stack_t;

// Creates a stack
// Returns a pointer to a newly created stack.
// The stack should be initialized with data on the heap.
// (Think about what the means in terms of memory allocation)
// The stacks fields should also be initialized to default values.
stack_t *create_stack(unsigned int capacity)
{
    stack_t *myStack = (stack_t *)malloc(sizeof(stack_t));
    myStack->count = 0;
    myStack->capacity = capacity;
    myStack->head = NULL;
    return myStack;
}

// Stack Empty
// Check if the stack is empty
// Returns 1 if true (The stack is completely empty)
// Returns 0 if false (the stack has at least one element enqueued)
int stack_empty(stack_t *s)
{
    return (s->count == 0);
}

// Stack Full
// Check if the stack is full
// Returns 1 if true (The Stack is completely full, i.e. equal to capacity)
// Returns 0 if false (the Stack has more space available to enqueue items)
int stack_full(stack_t *s)
{
    return (s->count == s->capacity);
}

// Enqueue a new item
// i.e. push a new item into our data structure
// Returns a -1 if the operation fails (otherwise returns 0 on success).
// (i.e. if the Stack is full that is an error, but does not crash the program).
int stack_enqueue(stack_t *s, int item)
{
    if (stack_full(s))
    {
        return -1; // Operation fails if the stack is full
    }
    node_t *newNode = (node_t *)malloc(sizeof(node_t));
    newNode->data = item;
    newNode->next = s->head;
    s->head = newNode;
    s->count++;
    return 0; // Success
}

// Dequeue an item
// Returns the item at the front of the stack and
// removes an item from the stack.
// Removing from an empty stack should crash the program, call exit(1).
int stack_dequeue(stack_t *s)
{
    if (stack_empty(s))
    {
        printf("Error: Stack is empty\n");
        exit(1);
    }
    int data = s->head->data;
    node_t *temp = s->head;
    s->head = s->head->next;
    free(temp);
    s->count--;
    return data;
}

// Stack Size
// Queries the current size of a stack
// A stack that has not been previously created will crash the program.
// (i.e. A NULL stack cannot return the size)
unsigned int stack_size(stack_t *s)
{
    if (s == NULL)
    {
        printf("Error: Stack not initialized\n");
        exit(1);
    }
    return s->count;
}
// Return the value at the top of the stack (without removing it)
int stack_peek(stack_t *s)
{
    if (s->count == 0)
    {
        // The stack is empty, return a marker value, such as -1
        return -1;
    }
    else
    {
        // Return the value at the top of the stack
        return s->head->data;
    }
}

// Check if two stacks are equal
int stack_equals(stack_t *s1, stack_t *s2)
{
    if (s1->count != s2->count)
    {
        // If the counts of the two stacks are different, they are not equal
        return 0;
    }
    node_t *current1 = s1->head;
    node_t *current2 = s2->head;
    while (current1 != NULL)
    {
        // Compare elements in the stacks one by one
        if (current1->data != current2->data)
        {
            return 0; // If any element is not equal, return not equal
        }
        current1 = current1->next;
        current2 = current2->next;
    }
    return 1; // If all elements are equal, return equal
}

// Free stack
// Removes a stack and ALL of its elements from memory.
// This should be called before the proram terminates.
void free_stack(stack_t *s)
{
    while (s->head != NULL)
    {
        node_t *temp = s->head;
        s->head = s->head->next;
        free(temp);
    }
    free(s);
}

#endif
