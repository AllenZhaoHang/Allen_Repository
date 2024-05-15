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
#include <assert.h>
// Our library that we have written.
// Also, by a really smart engineer!
#include "my_graph.h"
// Function prototypes for your unit tests
void test_graph_is_reachable()
{
    printf("Testing graph_is_reachable...\n");
    // Initialize your graph and add nodes and edges for testing
    graph_t *graph = create_graph();
    assert(graph != NULL);

    // Add nodes and edges to the graph
    graph_add_node(graph, 1);
    graph_add_node(graph, 2);
    graph_add_node(graph, 3);
    graph_add_edge(graph, 1, 2);
    graph_add_edge(graph, 2, 3);

    // Perform tests
    assert(graph_is_reachable(graph, 1, 3) == 1);
    assert(graph_is_reachable(graph, 3, 1) == 0);
    assert(graph_is_reachable(graph, 1, 4) == 0); // Non-existing node
    assert(graph_is_reachable(NULL, 1, 3) == -1); // Test for NULL graph

    // Free memory
    free_graph(graph);
}

void test_graph_has_cycle()
{
    printf("Testing graph_has_cycle...\n");
    // Initialize your graph and add nodes and edges for testing
    graph_t *graph = create_graph();
    assert(graph != NULL);

    // Add nodes and edges to the graph
    graph_add_node(graph, 1);
    graph_add_node(graph, 2);
    graph_add_node(graph, 3);
    graph_add_edge(graph, 1, 2);
    graph_add_edge(graph, 2, 3);

    // Perform tests
    assert(graph_has_cycle(graph) == 0); // The graph is acyclic
    graph_add_edge(graph, 3, 1);         // Adding edge to create a cycle
    assert(graph_has_cycle(graph) == 1);
    assert(graph_has_cycle(NULL) == -1); // Test for NULL graph

    // Free memory
    free_graph(graph);
}

void test_graph_print_path()
{
    printf("Testing graph_print_path...\n");
    // Initialize your graph and add nodes and edges for testing
    graph_t *graph = create_graph();
    assert(graph != NULL);

    // Add nodes and edges to the graph
    graph_add_node(graph, 1);
    graph_add_node(graph, 2);
    graph_add_node(graph, 3);
    graph_add_edge(graph, 1, 2);
    graph_add_edge(graph, 2, 3);

    // Perform tests
    assert(graph_print_path(graph, 1, 3) == 1); // Path exists
    assert(graph_print_path(graph, 3, 1) == 0); // No path exists
    assert(graph_print_path(graph, 1, 4) == 0); // Non-existing destination
    assert(graph_print_path(NULL, 1, 3) == -1); // Test for NULL graph

    // Free memory
    free_graph(graph);
}
// my graph unit tests
void test_graph_operations()
{
    // Create a graph
    graph_t *graph = create_graph();
    assert(graph != NULL);

    // Add nodes to the graph
    assert(graph_add_node(graph, 1) == 1);
    assert(graph_add_node(graph, 2) == 1);
    assert(graph_add_node(graph, 3) == 1);
    assert(graph_add_node(graph, 4) == 1);

    // Check the number of nodes in the graph
    assert(graph_num_nodes(graph) == 4);

    // Add edges to the graph
    assert(graph_add_edge(graph, 1, 2) == 1);
    assert(graph_add_edge(graph, 1, 3) == 1);
    assert(graph_add_edge(graph, 2, 3) == 1);
    assert(graph_add_edge(graph, 3, 4) == 1);

    // Check the number of edges in the graph
    assert(graph_num_edges(graph) == 4);

    // Check if edges exist
    assert(contains_edge(graph, 1, 2) == 1);
    assert(contains_edge(graph, 1, 3) == 1);
    assert(contains_edge(graph, 2, 3) == 1);
    assert(contains_edge(graph, 3, 4) == 1);
    assert(contains_edge(graph, 1, 4) == 0);

    // Free the graph
    free_graph(graph);

    printf("All tests passed successfully!\n");
}

// Note that we are locating this file
// within the same directory, so we use quotations
// and provide the path to this file which is within
// our current directory.

int main(int argc, const char * argv[]) {

    // graph_t * graph = create_graph();

    // graph_add_node(graph, 1);
    // graph_add_node(graph, 1);
    // graph_add_node(graph, 2);

    // printf("total nodes: 2==%d\n", graph_num_nodes(graph));

    // // my graph unit tests
    // test_graph_operations();
    // Run the unit tests
    test_graph_is_reachable();
    test_graph_has_cycle();
    test_graph_print_path();

    printf("All tests passed!\n");
    return 0;
}
