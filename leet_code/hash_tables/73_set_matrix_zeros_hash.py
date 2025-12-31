"""Module for setting matrix rows and columns to zero."""

import unittest
from typing import List


class Solution:
    """Set entire row and column to zero if any cell contains zero."""

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Modify matrix in-place: set row/column to zero if any cell is zero."""
        rows, cols = len(matrix), len(matrix[0])

        # Track which rows and columns contain zeros
        zero_rows, zero_cols = set(), set()

        # First pass: identify all rows and columns with zeros
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # Second pass: set all cells in marked rows/columns to zero
        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0


class TestSetMatrixZeros(unittest.TestCase):
    """Unit tests for the Set Matrix Zeros solution."""

    def test_single_zero(self):
        """Case with single zero in matrix."""
        solution = Solution()
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_multiple_zeros(self):
        """Case with multiple zeros."""
        solution = Solution()
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

    def test_zero_in_first_row_col(self):
        """Case with zero in first row and column."""
        solution = Solution()
        matrix = [[1, 0, 3]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0]])

    def test_all_zeros(self):
        """Case where entire matrix becomes zeros."""
        solution = Solution()
        matrix = [[1, 1], [1, 0]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, [[1, 0], [0, 0]])


if __name__ == "__main__":
    unittest.main()
