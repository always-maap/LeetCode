"""
104. Maximum Depth of Binary Tree
Easy
Tree | Depth First Search | Recursion
---
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf
node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# O(n) time | O(1)
class Solution:
    currMaxDepth = 0
    def maxDepth(self, root: TreeNode, currDepth = 0) -> int:
        if not root: return 0
        currDepth += 1
        if not root.left and not root.right:
            if currDepth > self.currMaxDepth:
                self.currMaxDepth = currDepth
        self.maxDepth(root.left, currDepth)
        self.maxDepth(root.right, currDepth)
        return self.currMaxDepth
