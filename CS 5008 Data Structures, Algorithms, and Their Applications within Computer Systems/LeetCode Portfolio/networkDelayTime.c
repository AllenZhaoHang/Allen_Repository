// Hang Zhao
// 4/6/2024
// 743. Network Delay Time(Medium 2 points) Topics：Depth - First Search Breadth - First Search Graph Heap(Priority Queue) Shortest Path
// https://leetcode.com/problems/network-delay-time/description/
    typedef struct Node
{
    int vex, weight;
} Node;

void swapNode(Node *node1, Node *node2)
{
    int temp1 = (*node1).vex;
    int temp2 = (*node1).weight;
    (*node1).vex = (*node2).vex;
    (*node1).weight = (*node2).weight;
    (*node2).vex = temp1;
    (*node2).weight = temp2;
}

void downAdjust(Node *heap, int k, int numSize)
{
    swapNode(&heap[0], &heap[k]);
    for (int i = 2 * k; i <= numSize; i *= 2)
    {
        if (i < numSize && heap[i + 1].weight < heap[i].weight)
        {
            i++;
        }
        if (heap[i].weight >= heap[0].weight)
        {
            break;
        }
        else
        {
            swapNode(&heap[i], &heap[k]);
            k = i;
        }
    }
    swapNode(&heap[0], &heap[k]);
}

void upAdjust(Node *heap, int k)
{
    swapNode(&heap[0], &heap[k]);
    for (int i = k / 2; i > 0; i /= 2)
    { // find the parent node
        if (heap[i].weight < heap[0].weight)
        {
            break;
        }
        else
        {
            swapNode(&heap[i], &heap[k]);
            k = i;
        }
    }
    swapNode(&heap[0], &heap[k]);
}

int networkDelayTime(int **times, int timesSize, int *timesColSize, int n, int k)
{
    const int MAX = 0x3f3f3f3f;
    int g[n][n];
    memset(g, 0x3f, sizeof(g));
    for (int i = 0; i < timesSize; i++)
    {
        int x = times[i][0] - 1, y = times[i][1] - 1;
        g[x][y] = times[i][2];
    }
    Node dist[n + 1];
    for (int i = 1; i <= n; i++)
    { // start from 1
        dist[i].vex = i;
        dist[i].weight = MAX;
    }
    dist[k].weight = 0;
    swapNode(&dist[1], &dist[k]);
    int begin = 0, end = n;
    int ans = 0;
    while (begin != end)
    {
        Node temp = dist[1];
        swapNode(&dist[1], &dist[end]);
        end--;
        downAdjust(dist, 1, end);
        ans = fmax(temp.weight, ans);
        for (int j = 1; j <= end; j++)
        {
            if (g[temp.vex - 1][dist[j].vex - 1] != MAX && dist[j].weight > temp.weight + g[temp.vex - 1][dist[j].vex - 1])
            {
                dist[j].weight = temp.weight + g[temp.vex - 1][dist[j].vex - 1];
                upAdjust(dist, j);
            }
        }
    }
    return ans == MAX ? -1 : ans;
}