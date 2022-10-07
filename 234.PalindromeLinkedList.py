"""
234. Palindrome Linked List
Easy
Linked List | Two Pointers | Stack | Recursion
---
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time | O(1) space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle
        walker = runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next

        # reverse second half
        rev = None
        curr = walker
        while curr != None:
            nextTemp = curr.next
            curr.next = rev
            rev = curr
            curr = nextTemp

        # check two half
        while rev and rev.val == head.val:
            head = head.next
            rev = rev.next

        return not rev
