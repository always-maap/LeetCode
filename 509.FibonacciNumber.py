"""
509. Fibonacci Number
Easy
Array
---
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:
0 ≤ N ≤ 30.
"""


# O(2^n) time | O(n) space
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)


# O(n) time | O(n) space
class Solution:
    def fib(self, N: int) -> int:
        memo = {0: 0, 1: 1}
        for i in range(2, N + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[N]


# O(n) time | O(1) space
class Solution:
    def fib(self, N: int) -> int:
        lastTwo = [0, 1]
        counter = 2
        while counter <= N:
            nextFib = lastTwo[0] + lastTwo[1]
            lastTwo[0] = lastTwo[1]
            lastTwo[1] = nextFib
            counter += 1
        return lastTwo[1] if N > 0 else lastTwo[0]
