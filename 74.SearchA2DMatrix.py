"""
74. Search a 2D Matrix
Medium
Array | Binary Search | Matrix
---
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

from typing import List


# O(n log m) time | O(1) space
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            last_col_val = matrix[row][len(matrix[row]) - 1]
            if target <= last_col_val:
                return self.binarySearch(matrix[row], target)

    def binarySearch(self, arr: List[int], target: int) -> bool:
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == target:
                return True

            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return False


# O(log(m + n)) time | O(1) space
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        start, end = 0, n * m - 1

        while start <= end:
            mid = (start + end) // 2
            mid_value = matrix[mid // m][mid % m]

            if mid_value == target:
                return True

            if mid_value < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
