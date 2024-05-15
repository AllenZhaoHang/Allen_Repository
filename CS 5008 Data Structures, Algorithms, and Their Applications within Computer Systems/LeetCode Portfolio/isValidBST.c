// Hang Zhao
// 4/6/2024
// 98. Validate Binary Search Tree(Medium 2 points) Topics： Tree Depth -First Search Binary Search Tree Binary Tree
// https://leetcode.com/problems/validate-binary-search-tree/description/

// Definition for a binary tree node.
#include <stddef.h>
#include <stdbool.h>
    struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
 };
 bool back(struct TreeNode *root, long *lower)
 {
     if (root == NULL)
         return true;
     if (!back(root->left, lower))
         return false;
     if (root->val <= *lower)
         return false;
     *lower = root->val;
     if (!back(root->right, lower))
         return false;
     return true;
 }
 bool isValidBST(struct TreeNode *root)
 {
     long long b = -2147483649;
     long long *a;
     a = &b;
     return back(root, a);
 }