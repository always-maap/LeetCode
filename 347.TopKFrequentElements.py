"""
347. Top K Frequent Elements
Medium
Array | Hash Table | Divide and Conquer | Sorting | Heap(Priority Queue) | Bucket Sort | Counting | Quickselect
---
Companies
Given an integer array nums and an integer k, return the k most frequent elements.
 You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List


# O(n log n) time | O(n) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 0

        sorted_dict_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_dict_list[i][0])

        return res


# O(n) time | O(n) space
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in dict.items():
            buckets[freq].append(num)

        res = []
        for i in buckets[::-1]:
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res

        return res
