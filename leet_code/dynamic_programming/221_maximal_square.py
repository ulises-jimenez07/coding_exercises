"""
Problem: Find the largest square containing only 1's in a binary matrix and return its area.

Approach:
- Use dynamic programming with a 2D table.
- dp[r][c] represents the side length of the largest square ending at (r, c).
- If matrix[r][c] is '1', dp[r][c] = min(top, left, top-left) + 1.
- Keep track of the maximum side length found.
- Time complexity: O(m*n) where m and n are matrix dimensions.
- Space complexity: O(m*n) for the dp table.

Example:
    Input: matrix = [["1","0","1","0","0"],
                     ["1","0","1","1","1"],
                     ["1","1","1","1","1"],
                     ["1","0","0","1","0"]]
    Output: 4
"""

import unittest
from typing import List


class Solution:
    """Standard solution class for the Maximal Square problem."""

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Calculates the area of the largest square containing only 1's.
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        # dp[i][j] stores the side length of the maximum square ending at (i, j)
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == "1":
                    # Base case: first row or first column
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        # Square length depends on top, left, and diagonal neighbors
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1

                    # Update the record for the maximum side length seen so far
                    if dp[r][c] > max_side:
                        max_side = dp[r][c]

        return max_side * max_side


class TestMaximalSquare(unittest.TestCase):
    """Unit tests for the Maximal Square implementation."""

    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example_1(self):
        """Test with the first LeetCode example."""
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        self.assertEqual(self.solution.maximalSquare(matrix), 4)

    def test_leetcode_example_2(self):
        """Test with the second LeetCode example."""
        matrix = [["0", "1"], ["1", "0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 1)

    def test_leetcode_example_3(self):
        """Test with a single '0' element."""
        matrix = [["0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 0)

    def test_empty_matrix(self):
        """Test with an empty matrix."""
        self.assertEqual(self.solution.maximalSquare([]), 0)
        self.assertEqual(self.solution.maximalSquare([[]]), 0)

    def test_all_zeros(self):
        """Test with a matrix containing only '0's."""
        matrix = [["0", "0"], ["0", "0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 0)

    def test_all_ones(self):
        """Test with a matrix containing only '1's."""
        matrix = [["1", "1"], ["1", "1"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 4)

    def test_single_row_with_one(self):
        """Test with a single row containing a '1'."""
        matrix = [["0", "1", "0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 1)

    def test_single_column_with_one(self):
        """Test with a single column containing a '1'."""
        matrix = [["0"], ["1"], ["0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 1)


if __name__ == "__main__":
    unittest.main()
