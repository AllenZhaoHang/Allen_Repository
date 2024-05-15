// Hang Zhao
// 4/6/2024
// 406. Queue Reconstruction by Height(Medium 2 points) Topics：ArrayBinary Indexed Tree Segment Tree Sorting
// https://leetcode.com/problems/queue-reconstruction-by-height/description/
/**
* Return an array of arrays of size *returnSize.
* The sizes of the arrays are returned as *returnColumnSizes array.
* Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
*/

    int
    cmp(const void *a, const void *b)
{
    int *a1 = *(int **)a;
    int *b1 = *(int **)b;
    if (a1[0] == b1[0])
    {
        return a1[1] - b1[1];
    }
    return b1[0] - a1[0];
}

int **reconstructQueue(int **people, int peopleSize, int *peopleColSize, int *returnSize, int **returnColumnSizes)
{
    qsort(people, peopleSize, sizeof(int *), cmp);
    *returnSize = 0;
    *returnColumnSizes = (int *)calloc(peopleSize, sizeof(int));
    int **res = (int **)calloc(peopleSize, sizeof(int *));
    for (int i = 0; i < peopleSize; ++i)
    {
        (*returnColumnSizes)[i] = 2;
    }
    for (int i = 0; i < peopleSize; ++i)
    {
        int h = people[i][0];
        int k = people[i][1];
        (*returnSize)++;
        for (int j = (*returnSize) - 1; j > k; --j)
        {
            res[j] = res[j - 1];
        }
        int *tmp = (int *)calloc(2, sizeof(int));
        tmp[0] = h;
        tmp[1] = k;
        res[k] = tmp;
    }
    return res;
}
