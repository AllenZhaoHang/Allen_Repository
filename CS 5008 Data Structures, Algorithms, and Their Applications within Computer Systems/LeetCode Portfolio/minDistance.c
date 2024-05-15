// Hang Zhao
// 4/6/2024
// 72. Edit Distance Medium 2 points Topics：String Dynamic Programming
// https://leetcode.com/problems/edit-distance/description/
#include <stdint.h>
    int
    mymin(int a, int b)
{
    return a < b ? a : b;
}

int minDistance(char *word1, char *word2)
{
    int len1 = strlen(word1);
    int len2 = strlen(word2);
    uint64_t dp[len1 + 1][len2 + 1];
    for (int i = 0; i <= len2; i++)
    {
        dp[0][i] = i;
    }
    for (int j = 1; j <= len1; j++)
    {
        dp[j][0] = j;
    }
    for (int i = 1; i <= len1; i++)
    {
        for (int j = 1; j <= len2; j++)
        {
            if (word1[i - 1] == word2[j - 1])
            {
                dp[i][j] = dp[i - 1][j - 1];
            }
            else
            {
                dp[i][j] = mymin(dp[i][j - 1], mymin(dp[i - 1][j], dp[i - 1][j - 1])) + 1;
            }
        }
    }
    return dp[len1][len2];
}