// Name: Hang Zhao
// Date: 1/26/2024
// HW2 CS5008 Spring 2024 myqueue.h
#include <stdio.h>
#include <stdlib.h>

#ifndef MYQUEUE_H
#define MYQUEUE_H

// The main data structure for the queue
struct queue
{
    unsigned int back;     // The next free position in the queue
                           // (i.e. the end or tail of the line)
    unsigned int front;    // Current 'head' of the queue
                           // (i.e. the front or head of the line)
    unsigned int size;     // How many total elements we currently have enqueued.
    unsigned int capacity; // Maximum number of items the queue can hold
    int *data;             // The 'integer' data our queue holds
};
// Creates a global definition of 'queue_t' so we
// do not have to retype 'struct queue' everywhere.
typedef struct queue queue_t;

// Create a queue
// Returns a pointer to a newly created queue.
// The queue should be initialized with data on
// the heap.
queue_t *create_queue(unsigned int _capacity)
{
    queue_t *myQueue = (queue_t *)malloc(sizeof(queue_t));
    myQueue->back = 0;
    myQueue->front = 0;
    myQueue->size = 0;
    myQueue->capacity = _capacity;
    myQueue->data = (int *)malloc(_capacity * sizeof(int));
    return myQueue;
}

// Queue Empty
// Check if the queue is empty
// Returns 1 if true (The queue is completely empty)
// Returns 0 if false (the queue has at least one element enqueued)
int queue_empty(queue_t *q)
{
    return (q->size == 0);
}

// Queue Full
// Check if the queue is Full
// Returns 1 if true (The queue is completely full)
// Returns 0 if false (the queue has more space available to enqueue items)
int queue_full(queue_t *q)
{
    return (q->size == q->capacity);
}

// Enqueue a new item
// i.e. push a new item into our data structure
// Returns a -1 if the operation fails (otherwise returns 0 on success).
// (i.e. if the queue is full that is an error).
int queue_enqueue(queue_t *q, int item)
{
    if (queue_full(q))
    {
        return -1; // Queue is full
    }
    q->data[q->back] = item;
    q->back = (q->back + 1) % q->capacity; // Wrap around if necessary
    q->size++;
    return 0; // Success
}

// Dequeue an item
// Returns the item at the front of the queue and
// removes an item from the queue.
// Removing from an empty queue should crash the program, call exit(1)
int queue_dequeue(queue_t *q)
{
    if (queue_empty(q))
    {
        fprintf(stderr, "Error: Queue is empty\n");
        exit(1);
    }
    int item = q->data[q->front];
    q->front = (q->front + 1) % q->capacity; // Wrap around if necessary
    q->size--;
    return item;
}

// Queue Size
// Queries the current size of a queue
// A queue that has not been previously created will crash the program.
// (i.e. A NULL queue cannot return the size, call exit(1))
unsigned int queue_size(queue_t *q)
{
    if (q == NULL)
    {
        fprintf(stderr, "Error: Queue is NULL\n");
        exit(1);
    }
    return q->size;
}
// Return the first value in the queue
int queue_peek(queue_t *q)
{
    if (q->size == 0)
    {
        // The queue is empty, return a marker value, such as -1
        return -1;
    }
    else
    {
        // Return the first value in the queue
        return q->data[q->front];
    }
}

// Return the last value in the queue
int queue_back(queue_t *q)
{
    if (q->size == 0)
    {
        // The queue is empty, return a marker value, such as -1
        return -1;
    }
    else
    {
        // Return the last value in the queue
        return q->data[(q->front + q->size - 1) % q->capacity];
    }
}

// Check if two queues are equal
int queue_equals(queue_t *q1, queue_t *q2)
{
    if (q1->size != q2->size)
    {
        // If the sizes of the two queues are different, they are not equal
        return 0;
    }
    for (unsigned int i = 0; i < q1->size; i++)
    {
        // Compare elements in the queues one by one
        if (q1->data[(q1->front + i) % q1->capacity] != q2->data[(q2->front + i) % q2->capacity])
        {
            return 0; // If any element is not equal, return not equal
        }
    }
    return 1; // If all elements are equal, return equal
}

// Free queue
// Removes a queue and all of its elements from memory.
// This should be called before the proram terminates.
void free_queue(queue_t *q)
{
    free(q->data);
    free(q);
}

#endif
