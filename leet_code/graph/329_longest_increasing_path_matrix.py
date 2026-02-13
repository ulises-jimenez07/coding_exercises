"""
Problem: Find the length of the longest increasing path in an m x n integer matrix.

Approach:
- Use Depth First Search (DFS) with memoization to avoid redundant calculations.
- For each cell, explore its four neighbors and recursively find the longest path sequence.
- Time complexity: O(m * n) where m and n are the dimensions of the matrix.
- Space complexity: O(m * n) for the memoization table and recursion stack.
"""

import unittest
from typing import List


class Solution:
    """
    This class provides a solution to the Longest Increasing Path in a Matrix problem.
    It uses DFS and memoization to efficiently compute the result.
    """

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Computes the length of the longest increasing path in the given matrix.
        """
        if not matrix or not matrix[0]:
            return 0
        # pylint: disable=attribute-defined-outside-init
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Memoization table to store results of previously visited cells
        self.memo = [[0] * self.cols for _ in range(self.rows)]
        self.matrix = matrix
        max_len = 0

        # Iterate through each cell in the matrix to find the starting point of the longest path
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                max_len = max(max_len, self.dfs(r, c))

        return max_len

    def dfs(self, r: int, c: int) -> int:
        """
        Recursive core for DFS with memoization.
        """
        # Return memoized result if it exists
        if self.memo[r][c] != 0:
            return self.memo[r][c]

        max_path = 1
        # Explore neighbors: Up, Down, Left, Right
        for dr, dc in self.dirs:
            nr, nc = r + dr, c + dc
            # If neighbor is within bounds and has a strictly greater value
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.matrix[r][c] < self.matrix[nr][nc]:
                max_path = max(max_path, 1 + self.dfs(nr, nc))

        # Store the result in the memoization table
        self.memo[r][c] = max_path
        return max_path


# -----------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class method longestIncreasingPath.
    """

    def setUp(self):
        """Initializes the solution instance for each test."""
        self.solution = Solution()

    def test_example1(self):
        """Tests the first example from LeetCode."""
        matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
        expected = 4  # Path: [1, 2, 6, 9]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), expected)

    def test_example2(self):
        """Tests the second example from LeetCode."""
        matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
        expected = 4  # Path: [3, 4, 5, 6]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), expected)

    def test_single_element(self):
        """Tests a matrix with a single element."""
        matrix = [[1]]
        expected = 1
        self.assertEqual(self.solution.longestIncreasingPath(matrix), expected)

    def test_empty_matrix(self):
        """Tests an empty matrix."""
        matrix = []
        expected = 0
        self.assertEqual(self.solution.longestIncreasingPath(matrix), expected)

    def test_empty_inner_list(self):
        """Tests a matrix with an empty inner list."""
        matrix = [[]]
        expected = 0
        self.assertEqual(self.solution.longestIncreasingPath(matrix), expected)

    def test_no_increasing_path(self):
        """Tests a matrix where no path can be longer than 1 (all same values)."""
        matrix = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        expected = 1
        self.assertEqual(self.solution.longestIncreasingPath(matrix), expected)


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # boilerplate code to run the tests when the script is executed
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
