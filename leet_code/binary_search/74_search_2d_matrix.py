"""
Problem: Search for a target value in a 2D matrix sorted row-wise and column-wise

Approach 1: Two Binary Searches
- First binary search to find the correct row
- Second binary search within that row to find target
- Time complexity: O(log m + log n)
- Space complexity: O(1)

Approach 2: Flattened Binary Search
- Treat the m x n matrix as a virtual 1D array of size m * n
- Map 1D index `i` to 2D coordinates: `r = i // n`, `c = i % n`
- Time complexity: O(log(m * n))
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """
    Solutions for searching a target value in a sorted 2D matrix.
    """

    def searchMatrix(self, matrix, target):
        top = 0
        bot = len(matrix) - 1

        # Find the correct row
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            if matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1

        row = (top + bot) // 2
        if not 0 <= row < len(matrix):
            return False

        # Binary search within the row
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix_v2(self, matrix: List[List[int]], target: int) -> bool:
        """
        Flattened Binary Search Approach.
        This approach treats the 2D matrix as a sorted 1D array by mapping indices.
        """
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        # The matrix can be viewed as a virtual 1D array of size rows * cols.
        # This works because each row is sorted and the first element of
        # each row is greater than the last element of the previous row.
        left, right = 0, rows * cols - 1

        while left <= right:
            # Calculate the middle index in the virtual 1D array
            mid = (left + right) // 2

            # Map the 1D index (mid) back to 2D matrix coordinates (r, c).
            # The formulas are derived from: i = r * n + c (where n = cols)
            #
            # For Row (r):
            # i = r * n + c
            # i - c = r * n
            # (i - c) // n = r
            # i // n - c // n = r
            # Since c < n, c // n = 0, so: r = i // n
            #
            # For Column (c):
            # i = r * n + c
            # i % n = (r * n + c) % n
            # i % n = (r * n % n) + (c % n)
            # Since (r * n % n) = 0 and c < n, so: c = i % n
            r = mid // cols
            c = mid % cols

            if target == matrix[r][c]:
                return True
            if target < matrix[r][c]:
                right = mid - 1
            else:
                left = mid + 1

        return False


class TestSearchMatrix(unittest.TestCase):
    """
    Unit tests for searchMatrix implementations.
    """

    def setUp(self):
        self.solution = Solution()

    def test_empty_matrix(self):
        self.assertFalse(self.solution.searchMatrix([], 5))
        self.assertFalse(self.solution.searchMatrix_v2([], 5))

    def test_target_present(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        for func in [self.solution.searchMatrix, self.solution.searchMatrix_v2]:
            self.assertTrue(func(matrix, 3))
            self.assertTrue(func(matrix, 11))
            self.assertTrue(func(matrix, 60))

    def test_target_absent(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        for func in [self.solution.searchMatrix, self.solution.searchMatrix_v2]:
            self.assertFalse(func(matrix, 13))
            self.assertFalse(func(matrix, 0))
            self.assertFalse(func(matrix, 70))

    def test_single_row_matrix(self):
        matrix = [[1, 3, 5, 7]]
        for func in [self.solution.searchMatrix, self.solution.searchMatrix_v2]:
            self.assertTrue(func(matrix, 3))
            self.assertFalse(func(matrix, 0))

    def test_single_element_matrix(self):
        matrix = [[5]]
        for func in [self.solution.searchMatrix, self.solution.searchMatrix_v2]:
            self.assertTrue(func(matrix, 5))
            self.assertFalse(func(matrix, 3))

    def test_target_first_element(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        for func in [self.solution.searchMatrix, self.solution.searchMatrix_v2]:
            self.assertTrue(func(matrix, 1))
            self.assertTrue(func(matrix, 10))
            self.assertTrue(func(matrix, 23))


if __name__ == "__main__":
    unittest.main()
