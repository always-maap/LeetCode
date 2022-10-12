"""
113. Path Sum II
Medium
Backtracking | Tree | Depth-First Search | Binary Tree
---
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values
 in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n ^ 2) time | O(H) space
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def checkSum(root: TreeNode, sum: int, path: List[int]) -> bool:
            if not root:
                return

            path.append(root.val)
            sum -= root.val

            if root.right == None and root.left == None:
                if sum == 0:
                    res.append(path.copy())
            else:
                checkSum(root.left, sum, path) or checkSum(
                    root.right, sum, path)
            path.pop()

        res = []
        checkSum(root, targetSum, [])
        return res
