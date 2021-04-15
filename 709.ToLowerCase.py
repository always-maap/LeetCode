"""
709. To Lower Case
Easy
String
---
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "here"
Output: "here"

Example 3:
Input: "LOVELY"
Output: "lovely"
"""


# O(n) time | O(1) space
class Solution:
    def toLowerCase(self, str: str) -> str:
        lower = ''
        for i in str:
            char_ascii = ord(i)
            if char_ascii >= 65 and char_ascii <= 90:
                lower += chr(char_ascii + 32)
            else:
                lower += i
        return lower
