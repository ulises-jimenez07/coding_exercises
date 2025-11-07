"""
Problem: Set entire rows and columns to zero if any element is zero, in-place

Approach:
- Use first row and column as markers for which rows/cols to zero
- Track separately if first row/col themselves need zeroing
- Time complexity: O(m*n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Sets entire rows and columns to zero if any element is zero, in-place."""
        first_row_has_zero = False
        first_col_has_zero = False

        rows = len(matrix)
        if rows == 0:
            return
        cols = len(matrix[0])
        if cols == 0:
            return

        # Check if first row has zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # Check if first column has zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Basic case."""
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_multiple_zeros(self):
        """Multiple zeros."""
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_zero_in_first_row_only(self):
        """Zero in first row."""
        matrix = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
        expected = [[0, 0, 0], [1, 0, 1], [1, 0, 1]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_zero_in_first_col_only(self):
        """Zero in first column."""
        matrix = [[1, 1, 1], [0, 1, 1], [1, 1, 1]]
        expected = [[0, 1, 1], [0, 0, 0], [0, 1, 1]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_zero_at_0_0(self):
        """Zero at [0][0]."""
        matrix = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 1], [0, 1, 1]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_empty_matrix(self):
        """Empty matrix."""
        matrix = []
        expected = []
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_single_element_matrix(self):
        """Single element."""
        matrix = [[5]]
        expected = [[5]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_single_element_zero_matrix(self):
        """Single element with zero."""
        matrix = [[0]]
        expected = [[0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_zero_in_first_row_and_first_col(self):
        """Zeros in first row and column."""
        matrix = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)


if __name__ == "__main__":
    unittest.main()
