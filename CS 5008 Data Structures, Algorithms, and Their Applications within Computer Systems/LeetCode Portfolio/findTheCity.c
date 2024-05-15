// Hang Zhao
// 4/6/2024
// 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance(Medium 2 points)Topics: Dynamic Programming   Graph  Shortest Path
    // https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

    int
    findTheCity(int n, int **edges, int edgesSize, int *edgesColSize, int distanceThreshold)
{
    int si[n][n];
    memset(si, 10001, sizeof(int) * (n * n));
    for (int i = 0; i < n; i++)
    {
        si[i][i] = 0;
    }
    for (int i = 0; i < edgesSize; i++)
    {
        si[edges[i][0]][edges[i][1]] = edges[i][2];
        si[edges[i][1]][edges[i][0]] = edges[i][2];
    }
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                si[i][j] = fmin(si[i][k] + si[k][j], si[i][j]);
            }
        }
    }
    #include <limits.h>

    int index = -1, max = INT_MAX;
    for (int i = 0; i < n; i++)
    {
        int cnt = 0;
        for (int j = 0; j < n; j++)
        {
            if (si[i][j] == 0)
            {
                continue;
            }
            else if (si[i][j] <= distanceThreshold)
            {
                cnt++;
            }
        }
        index = cnt <= max ? i : index;
        max = max > cnt ? cnt : max;
        /*printf("%d\n",index);*/
    }
    return index;
}