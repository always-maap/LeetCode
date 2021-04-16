"""
152. Maximum Product Subarray
Medium
Array | Dynamic Programming
---
Share
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
 and return the product.
It is guaranteed that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


# O(n) time | O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]  # max from previous iteration
        prev_min = nums[0]  # min from previous iteration
        max_to_n = nums[0]  # max this iteration
        min_to_n = nums[0]  # min this iteration
        res = nums[0]

        for i in nums[1:]:
            max_to_n = max(max(prev_max * i, prev_min * i), i)
            min_to_n = min(min(prev_max * i, prev_min * i), i)
            prev_max = max_to_n
            prev_min = min_to_n
            res = max(res, max_to_n)
        return res


# O(n) time | O(1) space
class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        current = 1
        for i in nums:
            current *= i
            res = max(res, current)
        current = 1
        for i in reversed(nums):
            current *= i
            res = max(res, current)
        return res
