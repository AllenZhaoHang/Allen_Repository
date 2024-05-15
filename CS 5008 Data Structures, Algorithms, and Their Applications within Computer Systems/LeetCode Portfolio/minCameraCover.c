// Hang Zhao
// 4/6/2024
// 968. Binary Tree Cameras(Medium 2 points) Topics：Dynamic Programming Tree Depth -First Search Binary Tree
// https://leetcode.com/problems/binary-tree-cameras/description/
// Definition for a binary tree node.
    struct TreeNode
{
    int val;
    struct TreeNode *left;
     struct TreeNode *right;
 };

int total;
int dfs968(struct TreeNode *root)
{
    int l = 2;
    int r = 2;
    #include <stddef.h> // Include the header file to define "NULL"

    if (root->left != NULL) // If the left child of the root is not NULL
        l = dfs968(root->left);
    if (root->right != NULL)
        r = dfs968(root->right);

    if (l == 0 || r == 0)
    { // need to install camera
        total += 1;
        return 1;
    }
    else if (l == 1 || r == 1) // already installed camera
        return 2;
    else
        return 0; // need to be covered
}

int minCameraCover(struct TreeNode *root)
{
    total = 0;
    if (root == NULL)
        return total;

    if (dfs968(root) == 0)
        total += 1;
    return total;
}