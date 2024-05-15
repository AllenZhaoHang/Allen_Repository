// Hang Zhao
// 4/6/2024
// 148. Sort List(Medium 2 points) Topics：Linked List Two Pointers  Divide and Conquer Sorting Merge Sort
// https://leetcode.com/problems/sort-list/description/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stddef.h>
    // Definition for singly-linked list.
    struct ListNode {
      int val;
      struct ListNode *next;
};
struct ListNode *ListPartition(struct ListNode *head)
{
    struct ListNode *fast = head;
    struct ListNode *slow = head;
    while ((fast = fast->next) && (fast = fast->next))
        slow = slow->next;
    fast = slow->next;
    slow->next = NULL;
    return fast;
}
struct ListNode *MergeSort(struct ListNode *head)
{
    if (!head->next)
        return head;
    struct ListNode *right = MergeSort(ListPartition(head));
    struct ListNode *left = MergeSort(head);
    struct ListNode *tail = head = right->val < left->val ? right : left;
    while (right && left)
    {
        struct ListNode *tmp;
        if (right->val < left->val)
        {
            tmp = right;
            right = right->next;
        }
        else
        {
            tmp = left;
            left = left->next;
        }
        tail = tail->next = tmp;
    }
    tail->next = right ? right : left;
    return head;
}
struct ListNode *sortList(struct ListNode *head)
{
    if (!head)
        return head;
    return MergeSort(head);
}