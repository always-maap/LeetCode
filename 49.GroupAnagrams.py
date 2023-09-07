"""
49. Group Anagrams
Medium
Array | Hash Table | String | Sorting
---
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

import collections
from typing import List


# O(m log n) time | O(m) space
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for i in range(len(strs)):
            curr = strs[i]
            sorted_s = "".join(sorted(curr))

            if dict.get(sorted_s):
                dict[sorted_s].append(curr)
            else:
                dict[sorted_s] = [curr]

        return dict.values()


# O(m n) time | O(m) space
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            dict[tuple(count)].append(s)

        return dict.values()
