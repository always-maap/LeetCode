"""
206. Reverse Linked List
Easy
Linked List
---
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time | O(1) space | Iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev


# O(n) time | O(n) space | recursive
class Solution2:
    def reverseList(self, head: ListNode, prev: ListNode = None) -> ListNode:
        if not head:
            return prev
        next_temp = head.next
        head.next = prev
        return self.reverseList(next_temp, head)
