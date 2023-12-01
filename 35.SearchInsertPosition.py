"""
35. Search Insert Position
Easy

---
Given a sorted array of distinct integers and a target value,
 return the index if the target is found. If not,
   return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

from typing import List


# O(n) time | O(1) space
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            curr = nums[i]
            if curr == target:
                return i

            if target < curr:
                return i

        return len(nums)


# O(n log n) time | O(1) space
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        while start < end:
            mid = (end + start) // 2
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid
        return start
