"""
1. Two Sum
Easy
Array | Hash Table
---
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


# O(n ^ 2) time | O(1) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            firstNum = nums[i]
            for j in range(i + 1, len(nums)):
                secondNum = nums[j]
                if firstNum + secondNum == target:
                    return [i, j]
        return []


# O(n) time | O(n) space
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memoNums = {}
        for i in range(len(nums)):
            potentailMatch = target - nums[i]
            if potentailMatch in memoNums:
                return [i, memoNums[potentailMatch]]
            else:
                memoNums[nums[i]] = i
        return []
