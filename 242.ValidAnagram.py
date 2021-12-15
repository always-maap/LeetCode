"""
242. Valid Anagram
Easy
Hash Table | String | Sorting
---
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

from collections import Counter


# O(n log n) time | O(1) space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# O(n) time | O(n + m) space
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# O(n) time | O(n + m) space
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}
        for c in range(len(s)):
            s_dict[s[c]] = s_dict.get(s[c], 0) + 1
            t_dict[t[c]] = t_dict.get(t[c], 0) + 1

        for char in s_dict:
            if s_dict[char] != t_dict.get(char, 0):
                return False

        return True
