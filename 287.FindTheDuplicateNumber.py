"""
287. Find the Duplicate Number
Medium
Array | Two Pointers | Binary Search | Bit Manipulation
---
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

from typing import List

# O(n log n) time | O(n) space | Not Acceptable
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]


# O(n) time | O(n) space | Not Acceptable
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)


# O(n) time | O(1) space | Not Acceptable
class Solution3:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = -1
        for num in nums:
            curr = abs(num)
            if nums[curr] < 0:
                duplicate = curr
                break
            nums[curr] *= -1

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate


# O(n) time | O(n) space | Not Acceptable
class Solution4:
    def findDuplicate(self, nums: List[int]) -> int:
        def store(nums: List[int], curr: int) -> int:
            if curr == nums[curr]:
                return curr
            next = nums[curr]
            nums[curr] = curr
            return store(nums, next)

        return store(nums, 0)


# O(n) time | O(1) space | Not Acceptable
class Solution5:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[nums[0]] != nums[0]:
            nums[0], nums[nums[0]] = nums[nums[0]], nums[0]
        return nums[0]
