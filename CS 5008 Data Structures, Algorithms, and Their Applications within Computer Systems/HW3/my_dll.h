// =================== Support Code =================
// Doubly Linked List ( DLL ).
//
//
//
// - Implement each of the functions to create a working DLL.
// - Do not change any of the function declarations
//   - (i.e. dll_t* create_dll() should not have additional arguments)
// - You should not have any 'printf' statements in your DLL functions.
//   - (You may consider using these printf statements to debug,
//     but they should be removed from your final version)
//   - (You may write helper functions to help you debug your code such as print_list etc)
// ==================================================
#ifndef MYDLL_H
#define MYDLL_H
#include <stddef.h>
#include <stdlib.h>
// Create a node data structure to store data within
// our DLL. In our case, we will stores 'integers'
typedef struct node
{
    int data;
    struct node *next;
    struct node *previous;
} node_t;

// Create a DLL data structure
// Our DLL holds a pointer to the first node in our DLL called head,
// and a pointer to the last node in our DLL called tail.
typedef struct DLL
{
    int count;    // count keeps track of how many items are in the DLL.
    node_t *head; // head points to the first node in our DLL.
    node_t *tail; // tail points to the last node in our DLL.
} dll_t;

// Creates a DLL
// Returns a pointer to a newly created DLL.
// The DLL should be initialized with data on the heap.
// (Think about what the means in terms of memory allocation)
// The DLLs fields should also be initialized to default values.
// Returns NULL if we could not allocate memory.
dll_t *create_dll()
{
    #include <stddef.h>
    dll_t *myDLL = (dll_t *)malloc(sizeof(dll_t));
    if (myDLL == NULL)
    {
        return NULL; // Memory allocation failed
    }

    myDLL->count = 0;
    myDLL->head = NULL;
    myDLL->tail = NULL;

    return myDLL;
}

// DLL Empty
// Check if the DLL is empty
// Returns -1 if the dll is NULL.
// Returns 1 if true (The DLL is completely empty)
// Returns 0 if false (the DLL has at least one element enqueued)
int dll_empty(dll_t *t)
{
    if (t == NULL)
    {
        return -1; // DLL is NULL
    }
    return (t->count == 0) ? 1 : 0;
}

// push a new item to the front of the DLL ( before the first node in the list).
// Returns -1 if DLL is NULL.
// Returns 1 on success
// Returns 0 on failure ( i.e. we couldn't allocate memory for the new node)
// (i.e. the memory allocation for a new node failed).
int dll_push_front(dll_t *t, int item)
{
    if (t == NULL)
    {
        return -1; // DLL is NULL
    }

    node_t *newNode = (node_t *)malloc(sizeof(node_t));
    if (newNode == NULL)
    {
        return 0; // Memory allocation failed
    }

    newNode->data = item;
    newNode->next = t->head;
    newNode->previous = NULL;

    if (t->count == 0)
    {
        t->tail = newNode; // If the DLL is empty, set tail to the new node
    }
    else
    {
        t->head->previous = newNode;
    }

    t->head = newNode;
    t->count++;
    return 1; // Success
}

// push a new item to the end of the DLL (after the last node in the list).
// Returns -1 if DLL is NULL.
// Returns 1 on success
// Returns 0 on failure ( i.e. we couldn't allocate memory for the new node)
// (i.e. the memory allocation for a new node failed).
int dll_push_back(dll_t *t, int item)
{
    if (t == NULL)
    {
        return -1; // DLL is NULL
    }

    node_t *newNode = (node_t *)malloc(sizeof(node_t));
    if (newNode == NULL)
    {
        return 0; // Memory allocation failed
    }

    newNode->data = item;
    newNode->next = NULL;
    newNode->previous = t->tail;

    if (t->count == 0)
    {
        t->head = newNode; // If the DLL is empty, set head to the new node
    }
    else
    {
        t->tail->next = newNode;
    }

    t->tail = newNode;
    t->count++;
    return 1; // Success
}

// Returns the first item in the DLL and also removes it from the list.
// Returns -1 if the DLL is NULL.
// Returns 0 on failure, i.e. there is noting to pop from the list.
// Assume no negative numbers in the list or the number zero.
int dll_pop_front(dll_t *t)
{
    if (t == NULL || t->count == 0)
    {
        return -1; // DLL is NULL or empty
    }

    node_t *temp = t->head;
    int data = temp->data;

    t->head = temp->next;
    if (t->head != NULL)
    {
        t->head->previous = NULL;
    }
    else
    {
        t->tail = NULL; // If the DLL becomes empty
    }

    free(temp);
    t->count--;
    return data;
}

// Returns the last item in the DLL, and also removes it from the list.
// Returns a -1 if the DLL is NULL.
// Returns 0 on failure, i.e. there is noting to pop from the list.
// Assume no negative numbers in the list or the number zero.
int dll_pop_back(dll_t *t)
{
    if (t == NULL || t->count == 0)
    {
        return -1; // DLL is NULL or empty
    }

    node_t *temp = t->tail;
    int data = temp->data;

    t->tail = temp->previous;
    if (t->tail != NULL)
    {
        t->tail->next = NULL;
    }
    else
    {
        t->head = NULL; // If the DLL becomes empty
    }

    free(temp);
    t->count--;
    return data;
}

// Inserts a new node before the node at the specified position.
// Returns -1 if the list is NULL
// Returns 1 on success
// Retruns 0 on failure:
//  * we couldn't allocate memory for the new node
//  * we tried to insert at a negative location.
//  * we tried to insert past the size of the list
//   (inserting at the size should be equivalent as calling push_back).
int dll_insert(dll_t *t, int pos, int item)
{
    if (t == NULL || pos < 0 || pos > t->count)
    {
        return -1; // Invalid parameters
    }

    if (pos == 0)
    {
        return dll_push_front(t, item); // Insert at the beginning
    }

    if (pos == t->count)
    {
        return dll_push_back(t, item); // Insert at the end
    }

    node_t *newNode = (node_t *)malloc(sizeof(node_t));
    if (newNode == NULL)
    {
        return 0; // Memory allocation failed
    }

    newNode->data = item;

    node_t *current = t->head;
    for (int i = 0; i < pos - 1; i++)
    {
        current = current->next;
    }

    newNode->next = current->next;
    newNode->previous = current;
    current->next->previous = newNode;
    current->next = newNode;

    t->count++;
    return 1; // Success
}

// Returns the item at position pos starting at 0 ( 0 being the first item )
// Returns -1 if the list is NULL
//  (does not remove the item)
// Returns 0 on failure:
//  * we tried to get at a negative location.
//  * we tried to get past the size of the list
// Assume no negative numbers in the list or the number zero.
int dll_get(dll_t *t, int pos)
{
    if (t == NULL || pos < 0 || pos >= t->count)
    {
        return -1; // Invalid parameters
    }

    node_t *current = t->head;
    for (int i = 0; i < pos; i++)
    {
        current = current->next;
    }

    return current->data;
}

// Removes the item at position pos starting at 0 ( 0 being the first item )
// Returns -1 if the list is NULL
// Returns 0 on failure:
//  * we tried to remove at a negative location.
//  * we tried to remove get past the size of the list
// Assume no negative numbers in the list or the number zero.
int dll_remove(dll_t *t, int pos)
{
    if (t == NULL || pos < 0 || pos >= t->count)
    {
        return -1; // Invalid parameters
    }

    if (pos == 0)
    {
        return dll_pop_front(t); // Remove from the beginning
    }

    if (pos == t->count - 1)
    {
        return dll_pop_back(t); // Remove from the end
    }

    node_t *current = t->head;
    for (int i = 0; i < pos; i++)
    {
        current = current->next;
    }

    current->previous->next = current->next;
    current->next->previous = current->previous;

    int data = current->data;
    free(current);
    t->count--;

    return data;
}

// DLL Size
// Returns -1 if the DLL is NULL.
// Queries the current size of a DLL
int dll_size(dll_t *t)
{
    if (t == NULL)
    {
        return -1; // DLL is NULL
    }

    return t->count;
}

// Free DLL
// Removes a DLL and all of its elements from memory.
// This should be called before the proram terminates.
void free_dll(dll_t *t)
{
    if (t == NULL)
    {
        return; // DLL is NULL
    }

    while (t->head != NULL)
    {
        dll_pop_front(t);
    }

    free(t);
}

#endif