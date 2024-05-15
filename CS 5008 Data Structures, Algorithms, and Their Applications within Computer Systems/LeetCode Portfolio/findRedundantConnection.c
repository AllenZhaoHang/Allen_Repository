// Hang Zhao
// 4/6/2024
// 684. Redundant Connection(Medium 2 points) Topics: Depth - First Search Breadth - First Search Union Find Graph
// https://leetcode.com/problems/redundant-connection/description/
#include <stddef.h>
    int
    Findfather(int *father, int num)
{
    if (father[num] == num)
    {
        return father[num];
    }
    return Findfather(father, father[num]);
}

void Union(int *father, int a, int b)
{
    father[Findfather(father, a)] = Findfather(father, b);
}

int *findRedundantConnection(int **edges, int edgesSize, int *edgesColSize, int *returnSize)
{
    int father[edgesSize + 1];
    int i;
    for (i = 1; i <= edgesSize; i++)
    {
        father[i] = i;
    }
    for (i = 0; i < edgesSize; i++)
    {
        int a = edges[i][0];
        int b = edges[i][1];
        if (Findfather(father, a) != Findfather(father, b))
        {
            Union(father, a, b);
        }
        else
        {
            *returnSize = 2;
            return edges[i];
        }
    }
    return NULL;
}