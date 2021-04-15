"""
704. Binary Search
Easy
Binary Search
---
Share
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search
target in nums. If target exists, then return its index, otherwise return -1.


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
import math


# O(log n) time | O(log n) space
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = math.floor((start + end) / 2)
        while start <= end and nums[mid] != target:
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
            mid = math.floor((start + end) / 2)
        return mid if nums[mid] == target else -1
