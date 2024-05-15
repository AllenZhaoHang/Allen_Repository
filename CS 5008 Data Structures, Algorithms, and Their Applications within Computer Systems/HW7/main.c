// Hang Zhao
// 3/18/2024
//
// Compile this assignment with: gcc -Wall main.c -o main
//
// Include parts of the C Standard Library
// These have been written by some other really
// smart engineers.
#include <stdio.h>  // For IO operations
#include <stdlib.h> // for malloc/free

// Our library that we have written.
// Also, by a really smart engineer!
#include "my_graph.h"
// Test the creation of a graph
int unitTest1(int status)
{
    int passed = 0;
    graph_t *graph = create_graph();
    if (graph != NULL && graph_num_nodes(graph) == 0 && graph_num_edges(graph) == 0)
    {
        passed = 1;
    }
    free_graph(graph);
    return passed;
}

// Test adding a node to the graph
int unitTest2(int status)
{
    int passed = 0;
    graph_t *graph = create_graph();
    graph_add_node(graph, 1);
    graph_add_node(graph, 2);
    if (graph_num_nodes(graph) == 2)
    {
        passed = 1;
    }
    free_graph(graph);
    return passed;
}

// Test adding and removing a node
int unitTest3(int status)
{
    int passed = 0;
    graph_t *graph = create_graph();
    graph_add_node(graph, 1);
    graph_add_node(graph, 2);
    graph_remove_node(graph, 1);
    if (graph_num_nodes(graph) == 1)
    {
        passed = 1;
    }
    free_graph(graph);
    return passed;
}

// Test adding an edge between two nodes
int unitTest4(int status)
{
    int passed = 0;
    graph_t *graph = create_graph();
    graph_add_node(graph, 1);
    graph_add_node(graph, 2);
    graph_add_edge(graph, 1, 2);
    if (graph_num_edges(graph) == 1 && contains_edge(graph, 1, 2) == 1)
    {
        passed = 1;
    }
    free_graph(graph);
    return passed;
}

// Test removing an edge between two nodes
int unitTest5(int status)
{
    int passed = 0;
    graph_t *graph = create_graph();
    graph_add_node(graph, 1);
    graph_add_node(graph, 2);
    graph_add_edge(graph, 1, 2);
    graph_remove_edge(graph, 1, 2);
    if (graph_num_edges(graph) == 0 && contains_edge(graph, 1, 2) == 0)
    {
        passed = 1;
    }
    free_graph(graph);
    return passed;
}

int unitTest6(int status)
{
    int passed = 0;
    graph_t* graph = create_graph();
    graph_add_node(graph, 1);
    graph_add_node(graph, 4);
    graph_add_node(graph, 2);
    graph_add_node(graph, 3);
    printf("numbers of nodes after add:  %d\n", graph->numNodes);

    graph_add_edge(graph, 1, 2);
    graph_add_edge(graph, 1, 1);
    graph_add_edge(graph, 3, 2);
    graph_add_edge(graph, 4, 2);
    graph_add_edge(graph, 2, 4);
    printf("numbers of edges after add:  %d\n", graph->numEdges);

    graph_remove_node(graph, 1);
    printf("number of edges after remove node 1:  %d\n", graph->numEdges);
    graph_remove_node(graph, 2);
    printf("number of edges after remove node 2:  %d\n", graph->numEdges);
    printf("number of nodes after remove node 2:  %d\n", graph->numNodes);

    if (graph->numEdges == 0 && graph->numNodes == 2)
    {
        passed = 1;
    }
    free_graph(graph);
    return passed;
}
int (*unitTests[])(int) = {
    unitTest1,
    unitTest2,
    unitTest3,
    unitTest4,
    unitTest5,
    unitTest6,
    NULL};

int main(int argc, const char *argv[])
{

    graph_t *graph = create_graph();

    graph_add_node(graph, 1);
    graph_add_node(graph, 1);
    graph_add_node(graph, 2);

    printf("total nodes: 2==%d\n", graph_num_nodes(graph));

    unsigned int testsPassed = 0;
    int counter = 0;
    while (unitTests[counter] != NULL)
    {
        printf("========unitTest %d========\n", counter + 1);
        if (1 == unitTests[counter](1))
        {
            printf("passed test\n");
            testsPassed++;
        }
        else
        {
            printf("failed test, missing functionality, or incorrect test\n");
        }
        counter++;
    }

    printf("%d of %d tests passed\n", testsPassed, counter);
    return 0;
    }