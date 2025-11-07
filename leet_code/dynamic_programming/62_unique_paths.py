"""
Problem: Count unique paths from top-left to bottom-right in grid.

Approach:
- Use dynamic programming with 2D array
- dp[i][j] = number of ways to reach cell (i,j)
- Initialize first row and column to 1 (only one way each)
- Each cell = sum of paths from top and left
- Time complexity: O(m * n) fill entire grid
- Space complexity: O(m * n) for dp array

Example: 3x7 grid -> 28 unique paths
"""

import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0] * n for _ in range(m)]

        # Initialize first column: only one way down
        for i in range(m):
            ways[i][0] = 1

        # Initialize first row: only one way right
        for j in range(n):
            ways[0][j] = 1

        # Fill dp table: paths = paths from above + paths from left
        for i in range(1, m):
            for j in range(1, n):
                ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

        return ways[m - 1][n - 1]


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case for a 3x7 grid."""
        self.assertEqual(self.solution.uniquePaths(3, 7), 28)

    def test_example_2(self):
        """Test case for a 3x2 grid."""
        self.assertEqual(self.solution.uniquePaths(3, 2), 3)

    def test_square_grid(self):
        """Test case for a square grid (3x3)."""
        self.assertEqual(self.solution.uniquePaths(3, 3), 6)

    def test_single_row_grid(self):
        """Test case for a grid with a single row."""
        self.assertEqual(self.solution.uniquePaths(1, 5), 1)

    def test_single_column_grid(self):
        """Test case for a grid with a single column."""
        self.assertEqual(self.solution.uniquePaths(5, 1), 1)

    def test_large_grid(self):
        """Test case for a larger grid (10x10)."""
        self.assertEqual(self.solution.uniquePaths(10, 10), 48620)


if __name__ == "__main__":
    unittest.main()
