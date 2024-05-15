// Hang Zhao
// 4/6/2024
// 1339 Maximum Product of Split Binary Tree---Medium (2 points) Topics：Tree Depth -First Search Binary Tree
// leetcode.com/problems/maximum-product-of-splitted-binary-tree/
// Definition for a binary tree node.
    struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
 };
 
typedef struct TreeNode TreeNode;

const int KMOD = 1E9 + 7;
long total;

// function declaration
long sum(TreeNode *);
long postOrder(TreeNode *, long *);

int maxProduct(TreeNode *root)
{
    total = sum(root);
    long ans = 0;
    postOrder(root, &ans);
    return ans % KMOD;
}

long sum(TreeNode *root)
{
    return root ? root->val + sum(root->left) + sum(root->right) : 0;
}

long postOrder(TreeNode *root, long *ans)
{
    if (!root)
        return 0;
    const long ls = postOrder(root->left, ans);
    const long rs = postOrder(root->right, ans);
    *ans = fmax(*ans, fmax(ls * (total - ls), rs * (total - rs)));
    return root->val + ls + rs;
}