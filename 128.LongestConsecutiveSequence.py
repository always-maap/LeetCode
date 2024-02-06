"""
128. Longest Consecutive Sequence
Medium
Array | Hash Table | Union Find
---
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


# O(n) time | O(n) space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        curr_max = 0
        for n in nums:
            if (n - 1) not in nums_set:
                l = 0
                while (n + l) in nums_set:
                    l += 1
                curr_max = max(curr_max, l)

        return curr_max
