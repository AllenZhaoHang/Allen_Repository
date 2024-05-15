// Hang Zhao
// 4/6/2024
// 207. Course Schedule(Medium 2 points)Topics : Depth - First Search Breadth - First Search Graph Topological Sort
// https://leetcode.com/problems/course-schedule/description/
#include <stdbool.h>

    bool
    canFinish(int numCourses, int **prerequisites, int prerequisitesSize, int *prerequisitesColSize)
{
    if (prerequisitesSize == 0)
    {
        return true;
    }
    int *ans = malloc(sizeof(int) * numCourses);
    int i = 0;
    for (i = 0; i < numCourses; i++) // intialize the array
    {
        ans[i] = 0;
    }
    int m = prerequisitesSize;
    int j = 0;
    int res = 0;
    for (i = 0; i < prerequisitesSize; i++) // update the array
    {
        ans[prerequisites[i][0]]++;
    }
    for (i = 0; i < numCourses; i++)
    {
        if (ans[i] == 0) // find the course that I can learn
        {
            res++;                 // I can learn one course
            if (res == numCourses) // I can learn all the courses
            {
                return true;
            }
            for (j = 0; j < prerequisitesSize; j++) // update the array
            {
                if (prerequisites[j][1] == i)
                {
                    ans[prerequisites[j][0]]--;
                }
            }
            ans[i]--; // I have learned this course
            i = -1;
        }
    }
    return false;
}