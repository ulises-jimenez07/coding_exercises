"""
Problem: Count the number of islands in a 2D grid of land ('1') and water ('0').

Approach:
- Use DFS to traverse and mark each island when found
- Count each new island discovery
- Time complexity: O(m * n)
- Space complexity: O(m * n) for recursion stack in worst case
"""

import unittest
from typing import List


class Solution:
    """
    A class to solve the 'Number of Islands' problem using DFS.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        # pylint: disable=attribute-defined-outside-init
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "1":
                    islands += 1
                    self.dfs(r, c)
        return islands

    def dfs(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == "1":
            self.grid[row][col] = "0"
            for dr, dc in self.directions:
                self.dfs(row + dr, col + dc)


# -----------------------------------------------------------------------------


class TestNumIslands(unittest.TestCase):
    """
    Unit tests for the Solution class's numIslands method.
    """

    def setUp(self):
        self.solution = Solution()

    def test_single_island(self):
        """Test case with a single, large island."""
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        expected = 1
        result = self.solution.numIslands(grid)
        self.assertEqual(result, expected)

    def test_multiple_islands(self):
        """Test case with multiple distinct islands."""
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        expected = 3
        result = self.solution.numIslands(grid)
        self.assertEqual(result, expected)

    def test_no_islands(self):
        """Test case with an entirely water-filled grid."""
        grid = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
        expected = 0
        result = self.solution.numIslands(grid)
        self.assertEqual(result, expected)

    def test_empty_grid(self):
        """Test case with an empty grid."""
        grid = []
        expected = 0
        result = self.solution.numIslands(grid)
        self.assertEqual(result, expected)

    def test_island_on_edge(self):
        """Test case with islands touching the grid boundaries."""
        grid = [["1", "0", "0"], ["0", "0", "0"], ["0", "0", "1"]]
        expected = 2
        result = self.solution.numIslands(grid)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
