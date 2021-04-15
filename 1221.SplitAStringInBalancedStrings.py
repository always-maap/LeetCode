"""
1221. Split a String in Balanced Strings
Easy
String | Greedy
---
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
"""


# O(n) time | O(1) space
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        balanced = 0
        for i in s:
            if i == 'L':
                balanced += 1
            else:
                balanced -= 1
            if balanced == 0:
                counter += 1
                balanced = 0
        return counter
