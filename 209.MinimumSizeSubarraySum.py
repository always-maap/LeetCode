"""
209. Minimum Size Subarray Sum
Medium
Array | Binary Search | Sliding Window | Prefix Sum
---
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous
 subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.
  If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

from typing import List
from sys import maxsize


# O(n ^ 2) time | O(1) space | Time limit Exceeded
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = maxsize
        for i in range(0, len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                if s >= target:
                    answer = min(answer, j - i + 1)
                    break
        return 0 if answer == maxsize else answer


# O(n) time | O(1) space
class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = maxsize
        s = left = 0
        for i in range(0, len(nums)):
            s += nums[i]
            while s >= target:
                answer = min(answer, i + 1 - left)
                s -= nums[left]
                left += 1
        return 0 if answer == maxsize else answer
