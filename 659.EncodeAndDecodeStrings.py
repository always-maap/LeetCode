"""
659. Encode and Decode Strings
Medium

---
Design an algorithm to encode a list of strings to a string.
 The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode


Example1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""

from typing import List


class Solution:
    # O(n) time | O(1) space
    def encode(self, strs: List[str]):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # O(n ^ 2) time | O(l) space
    def decode(self, str: str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            l = int(str[i:j])
            res.append(str[j + 1 : j + 1 + l])
            i = j + 1 + l

        return res
