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
    A class to solve the 'Number of Islands' problem.
    The problem is to count the number of islands in a 2D grid.
    An island is surrounded by water ('0') and is formed by connecting
    adjacent lands ('1') horizontally or vertically.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Main method to count the number of islands.

        It iterates through every cell in the grid. If a '1' (land) is found,
        it increments the island count and initiates a Depth First Search (DFS)
        to mark the entire island as visited (by changing '1's to '2's).
        """
        self.grid = grid  # pylint: disable=attribute-defined-outside-init
        count = 0  # Initialize island count
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])

        for row in range(0, rows):
            for col in range(0, cols):
                if self.grid[row][col] == "1":
                    count += 1  # Found a new island
                    self.dfs(row, col)  # Explore and mark the entire island as visited
        return count

    def is_valid(self, row, col):
        """
        Helper function to check if a cell (row, col) is valid to visit.

        A cell is valid if:
        1. It is within the grid boundaries.
        2. It contains '1' (land that hasn't been visited yet).
        """
        # Check boundary conditions for rows
        if row < 0 or row >= len(self.grid):
            return False
        # Check boundary conditions for columns
        if col < 0 or col >= len(self.grid[0]):
            return False
        # Check if it's unvisited land
        if self.grid[row][col] == "1":
            return True
        return False

    def dfs(self, row, col):
        """
        Performs Depth First Search (DFS) starting from (row, col).

        It marks the current land cell as visited ('2') and recursively
        explores all four adjacent cells (up, down, left, right).
        """
        if self.is_valid(row, col):
            # Mark the current cell as visited (e.g., changing '1' to '2')
            self.grid[row][col] = "2"

            # Recursively explore all four adjacent directions
            self.dfs(row - 1, col)  # Up
            self.dfs(row + 1, col)  # Down
            self.dfs(row, col - 1)  # Left
            self.dfs(row, col + 1)  # Right


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
