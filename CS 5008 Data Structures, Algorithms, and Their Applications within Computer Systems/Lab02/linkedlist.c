// Modify this file
// compile with: gcc linkedlist.c -o linkedlist
// Name: Hang Zhao
// Date: 1/26/2024
// Lab02 CS5008 Spring 2024
#include <stdio.h>
#include <stdlib.h>

// Define node_t structure
typedef struct node
{
    int year;
    int wins;
    struct node *next;
} node_t;

// Function to create a new node
node_t *create_node(int year, int wins, node_t *next)
{
    node_t *new_node = (node_t *)malloc(sizeof(node_t));
    if (new_node == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    new_node->year = year;
    new_node->wins = wins;
    new_node->next = next;
    return new_node;
}

// Function to create a linked list and return the head
node_t *create_list()
{
    node_t *head = create_node(2018, 108, NULL);
    head->next = create_node(2017, 93, create_node(2016, 93, create_node(2015, 78, create_node(2014, 71, NULL))));
    return head;
}

// Function to print the linked list
void print_list(node_t *head)
{
    node_t *current = head;
    while (current != NULL)
    {
        printf("%d, %d wins\n", current->year, current->wins);
        current = current->next;
    }
}

// Function to free the linked list
void free_list(node_t *head)
{
    node_t *current = head;
    node_t *next;
    while (current != NULL)
    {
        next = current->next;
        free(current);
        current = next;
    }
}

int main()
{
    // Create a linked list
    node_t *red_sox_data = create_list();

    // Print the linked list
    print_list(red_sox_data);

    // Free the linked list
    free_list(red_sox_data);

    return 0;
}
