#include "my_dll.h"
#include <stdlib.h>
#include <assert.h>
// Hang Zhao
// 3/18/2024
// Create a graph data structure
typedef struct graph
{
    int numNodes;
    int numEdges;
    dll_t *nodes; // an array of nodes storing all of our nodes.
} graph_t;

typedef struct graph_node
{
    int data;
    dll_t *inNeighbors;
    dll_t *outNeighbors;
} graph_node_t;

// Creates a graph
graph_t *create_graph()
{
    graph_t *myGraph = (graph_t *)malloc(sizeof(graph_t));
    if (myGraph == NULL)
        return NULL;

    myGraph->nodes = create_dll();
    if (myGraph->nodes == NULL)
    {
        free(myGraph);
        return NULL;
    }

    myGraph->numEdges = 0;
    myGraph->numNodes = 0;
    return myGraph;
}
//////////////////////////////////////////////////
// Define a structure to represent the visited nodes list
typedef struct
{
    dll_t *visitedNodes; // DLL to store visited nodes
} visited_list_t;

// Create a function to initialize the visited nodes list
visited_list_t *create_visited_list()
{
    visited_list_t *visitedList = (visited_list_t *)malloc(sizeof(visited_list_t));
    if (visitedList == NULL)
    {
        return NULL; // Memory allocation failed
    }

    visitedList->visitedNodes = create_dll();
    if (visitedList->visitedNodes == NULL)
    {
        free(visitedList);
        return NULL; // Memory allocation failed
    }

    return visitedList;
}

// Function to add a node to the visited list
void add_visited_node(dll_t *visitedList, int nodeData)
{
    if (visitedList == NULL)
    {
        return;
    }

    // Check if the node is already in the visited list
    // You need to manually traverse the list to check for duplicates
    node_t *current = visitedList->head;
    while (current != NULL)
    {
        if (*(int *)current->data == nodeData)
        {
            return; // Node already visited
        }
        current = current->next;
    }

    // Add the node to the visited list
    int *data = (int *)malloc(sizeof(int));
    if (data == NULL)
    {
        // Memory allocation failed
        return;
    }
    *data = nodeData;
    dll_push_back(visitedList, data);
}
// Function to check if a node has been visited
int is_node_visited(dll_t *visitedList, int nodeData)
{
    if (visitedList == NULL)
    {
        return 0; // Visited list not initialized
    }

    // Check if the node is in the visited list
    node_t *current = visitedList->head;
    while (current != NULL)
    {
        if (*(int *)current->data == nodeData)
        {
            return 1; // Node is visited
        }
        current = current->next;
    }

    return 0; // Node is not visited
}

/////////////////////////////////////////////////
// Returns the node pointer if the node exists.
graph_node_t *find_node(graph_t *g, int value)
{
    if (g == NULL)
    {
        return NULL;
    }

    // Traverse the list of nodes in the graph
    node_t *current = g->nodes->head;
    while (current != NULL)
    {
        graph_node_t *node = (graph_node_t *)current->data;
        if (node->data == value)
        {
            return node; // Node found
        }
        current = current->next;
    }

    return NULL; // Node not found
}

// Creates a graph node
graph_node_t *create_graph_node(int value)
{
    graph_node_t *graph_node = (graph_node_t *)malloc(sizeof(graph_node_t));
    if (graph_node == NULL)
        return NULL;

    graph_node->data = value;
    graph_node->inNeighbors = create_dll();
    graph_node->outNeighbors = create_dll();

    return graph_node;
}

// Adds a node to the graph
int graph_add_node(graph_t *g, int value)
{
    if (g == NULL)
        return -1;

    if (find_node(g, value) != NULL)
        return 0; // Node already exists

    graph_node_t *newNode = create_graph_node(value);
    if (newNode == NULL)
        return -1; // Memory allocation failed

    dll_push_back(g->nodes, newNode);
    g->numNodes++;

    return 1; // Success
}

// Removes a specified node from the DLL.
// Assumes the DLL is non-empty and that the node exists in the DLL.
void remove_dll_item(dll_t *t, graph_node_t *nodeToRemove)
{
    if (t == NULL || nodeToRemove == NULL)
    {
        return; // Invalid parameters
    }

    // Find the node in the DLL
    node_t *current = t->head;
    while (current != NULL)
    {
        if (current->data == nodeToRemove)
        {
            break; // Node found
        }
        current = current->next;
    }

    // If node not found, return
    if (current == NULL)
    {
        return;
    }

    // Node found, adjust pointers
    if (current == t->head)
    {
        t->head = current->next;
    }
    else
    {
        current->previous->next = current->next;
    }

    if (current == t->tail)
    {
        t->tail = current->previous;
    }
    else
    {
        current->next->previous = current->previous;
    }

    // Free memory allocated for the node
    free(current);
    t->count--;
}

// Returns 1 on success
// Returns 0 on failure ( or if the node doesn't exist )
// Returns -1 if the graph is NULL.
// Removes a node from the graph
int graph_remove_node(graph_t *g, int value)
{
    if (g == NULL)
        return -1;

    graph_node_t *nodeToRemove = find_node(g, value);
    if (nodeToRemove == NULL)
        return 0; // Node doesn't exist

    // Remove all edges involving this node
    node_t *current = g->nodes->head;
    while (current != NULL)
    {
        graph_node_t *node = (graph_node_t *)current->data;
        int index = 0;
        node_t *outCurrent = node->outNeighbors->head;
        while (outCurrent != NULL)
        {
            if (outCurrent->data == nodeToRemove)
            {
                // dll_remove(node->outNeighbors, index); // Remove the edge
                // g->numEdges--;                         // Decrement edge count
                graph_remove_edge(g, node->data, value);
                break;                                 // Break since each node can only appear once in the outNeighbors
            }
            outCurrent = outCurrent->next;
            index++;
        }
        current = current->next;
    }

    // Now, handle the node's outNeighbors and inNeighbors
    while (!dll_empty(nodeToRemove->outNeighbors))
    {
        graph_node_t *outNeighbor = (graph_node_t *)dll_pop_front(nodeToRemove->outNeighbors);
        // For each outNeighbor, we need to remove nodeToRemove from its inNeighbors
        current = outNeighbor->inNeighbors->head;
        int pos = 0;
        while (current != NULL)
        {
            if (current->data == nodeToRemove)
            {
                dll_remove(outNeighbor->inNeighbors, pos); // Remove the edge
                break;                                     // Break since each node can only appear once in the inNeighbors
            }
            current = current->next;
            pos++;
        }
    }

    // Since inNeighbors are just references, no need to remove nodeToRemove from others' outNeighbors
    free_dll(nodeToRemove->outNeighbors); // Free the outNeighbors list
    free_dll(nodeToRemove->inNeighbors);  // Free the inNeighbors list

    // Finally, remove the node from the graph's list of nodes
    current = g->nodes->head;
    int pos = 0;
    while (current != NULL)
    {
        if (((graph_node_t *)current->data)->data == value)
        {
            dll_remove(g->nodes, pos); // Remove the node
            free(nodeToRemove);        // Free the node structure
            g->numNodes--;             // Decrement node count
            return 1;                  // Success
        }
        current = current->next;
        pos++;
    }
    return 0;
}

// Adds an edge between two nodes in the graph
int graph_add_edge(graph_t *g, int source, int destination)
{
    if (g == NULL)
        return -1;

    graph_node_t *sourceNode = find_node(g, source);
    graph_node_t *destinationNode = find_node(g, destination);

    if (sourceNode == NULL || destinationNode == NULL)
        return 0; // Nodes don't exist

    // Check if the edge already exists
    // node_t *current = sourceNode->outNeighbors->head;
    // while (current != NULL)
    // {
    //     graph_node_t *neighbor = (graph_node_t *)current->data;
    //     if (neighbor == destinationNode)
    //     {
    //         return 0; // Edge already exists
    //     }
    //     current = current->next;
    // }
    if (contains_edge(g, source, destination))
    {
        return 0; // Edge already exists
    }

    // Add the edge
    dll_push_back(sourceNode->outNeighbors, destinationNode);
    dll_push_back(destinationNode->inNeighbors, sourceNode);
    g->numEdges++;

    return 1; // Success
}

// Returns 1 on success
// Returns 0 on failure ( or if the source or destination nodes don't exist, or the edge doesn't exists )
// Returns -1 if the graph is NULL.
int graph_remove_edge(graph_t *g, int source, int destination)
{
    // TODO: Implement me!
    // The function removes an edge from source to destination but not the other way.
    // Make sure you remove destination from the out neighbors of source.
    // Make sure you remove source from the in neighbors of destination.
    if (g == NULL)
        return -1;

    graph_node_t *sourceNode = find_node(g, source);
    graph_node_t *destinationNode = find_node(g, destination);
    if (sourceNode == NULL || destinationNode == NULL)
        return 0;
    // Remove the edge if it exists
    if (contains_edge(g, source, destination))
    {
        dll_remove_by_data(sourceNode->outNeighbors, destinationNode);
        dll_remove_by_data(destinationNode->inNeighbors, sourceNode);
        g->numEdges--;
        return 1; // Success
    }

    return 0; // Edge doesn't exist
    // int removed = 0;

    // // Find index of destinationNode in sourceNode's outNeighbors to remove
    // int index = 0;
    // node_t *current = sourceNode->outNeighbors->head;
    // while (current != NULL)
    // {
    //     if (current->data == destinationNode)
    //     {
    //         dll_remove(sourceNode->outNeighbors, index);
    //         removed = 1; // Mark as removed
    //         break;
    //     }
    //     current = current->next;
    //     index++;
    // }

    // // Similar approach to find sourceNode in destinationNode's inNeighbors
    // index = 0;
    // current = destinationNode->inNeighbors->head;
    // while (current != NULL)
    // {
    //     if (current->data == sourceNode)
    //     {
    //         dll_remove(destinationNode->inNeighbors, index);
    //         removed &= 1; // Ensure it was removed from both lists
    //         break;
    //     }
    //     current = current->next;
    //     index++;
    // }

    // if (removed)
    // {
    //     g->numEdges--;
    //     return 1;
    // }

    // return 0;
}

// Checks if an edge exists between two nodes in the graph
int contains_edge(graph_t *g, int source, int destination)
{
    if (g == NULL)
        return -1;

    graph_node_t *sourceNode = find_node(g, source);
    graph_node_t *destinationNode = find_node(g, destination);

    if (sourceNode == NULL || destinationNode == NULL)
        return 0; // Nodes don't exist

    // Check if the edge exists
    node_t *current = sourceNode->outNeighbors->head;
    while (current != NULL)
    {
        graph_node_t *neighbor = (graph_node_t *)current->data;
        if (neighbor == destinationNode)
            return 1; // Edge exists
        current = current->next;
    }

    return 0; // Edge doesn't exist
}

// Returns the in neighbors of a node in the graph
dll_t *getInNeighbors(graph_t *g, int value)
{
    graph_node_t *node = find_node(g, value);
    if (node == NULL)
        return NULL; // Node doesn't exist

    return node->inNeighbors;
}

// Returns the number of in neighbors of a node in the graph
int getNumInNeighbors(graph_t *g, int value)
{
    dll_t *inNeighbors = getInNeighbors(g, value);
    if (inNeighbors == NULL)
        return -1; // Node doesn't exist

    return inNeighbors->count;
}

// Returns the out neighbors of a node in the graph
dll_t *getOutNeighbors(graph_t *g, int value)
{
    graph_node_t *node = find_node(g, value);
    if (node == NULL)
        return NULL; // Node doesn't exist

    return node->outNeighbors;
}

// Returns the number of out neighbors of a node in the graph
int getNumOutNeighbors(graph_t *g, int value)
{
    dll_t *outNeighbors = getOutNeighbors(g, value);
    if (outNeighbors == NULL)
        return -1; // Node doesn't exist

    return outNeighbors->count;
}

// Returns the number of nodes in the graph
int graph_num_nodes(graph_t *g)
{
    if (g == NULL)
        return -1;

    return g->numNodes;
}

// Returns the number of edges in the graph
int graph_num_edges(graph_t *g)
{
    if (g == NULL)
        return -1;

    return g->numEdges;
}

// Free graph
void free_graph(graph_t *g)
{
    if (g == NULL)
        return;

    // Free each node and its neighbors
    node_t *current = g->nodes->head;
    while (current != NULL)
    {
        graph_node_t *node = (graph_node_t *)current->data;
        free_dll(node->inNeighbors);
        free_dll(node->outNeighbors);
        free(node);
        current = current->next;
    }

    // Free the list of nodes
    free_dll(g->nodes);

    // Free the graph itself
    free(g);
}