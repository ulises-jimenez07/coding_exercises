"""
Problem: Count the number of land cells that cannot reach the edge of the grid.

Approach:
- Use DFS to mark all boundary-connected land cells as visited (sink them)
- Count remaining land cells as enclaves
- Time complexity: O(m * n)
- Space complexity: O(m * n) for recursion stack
"""

import unittest
from typing import List


class Solution:
    """
    Given a 2D array grid of 0s and 1s, returns the number of 'enclaves'.
    An 'enclave' is a land cell (1) that cannot reach the boundary of the grid
    by moving in the four cardinal directions (up, down, left, right).
    """

    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Counts the number of land cells (1) that are not connected to the boundary.

        The approach is to use Depth First Search (DFS) to 'sink' (change to 0)
        all land cells that are connected to the boundary. The remaining '1's
        are the enclaves.

        Args:
            grid: A list of lists representing the grid. 1 is land, 0 is water.

        Returns:
            The total number of enclaves.
        """
        # Store dimensions for easy access in the class methods
        self.n = len(grid)
        self.m = len(grid[0])

        # 1. 'Sink' all land cells connected to the left and right boundaries
        for i in range(self.n):
            self.dfs_core(i, 0, grid)  # Left boundary column (col = 0)
            self.dfs_core(i, self.m - 1, grid)  # Right boundary column (col = m-1)

        # 2. 'Sink' all land cells connected to the top and bottom boundaries
        for j in range(self.m):
            self.dfs_core(0, j, grid)  # Top boundary row (row = 0)
            self.dfs_core(self.n - 1, j, grid)  # Bottom boundary row (row = n-1)

        # 3. Count the remaining land cells (enclaves)
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    count += 1
        return count

    def dfs_core(self, row, col, grid):
        """
        Performs Depth First Search (DFS) to change connected land cells (1) to water (0).
        This effectively 'sinks' the land mass connected to the starting (row, col).

        Args:
            row: The current row index.
            col: The current column index.
            grid: The grid being modified in place.
        """
        # Check boundary conditions and if the cell is land (1)
        if row >= 0 and row < self.n and col >= 0 and col < self.m and grid[row][col] == 1:

            # Change land (1) to water (0) to mark it as visited/sunk
            grid[row][col] = 0

            # Recursively call DFS on all four neighbors
            self.dfs_core(row - 1, col, grid)  # Up
            self.dfs_core(row + 1, col, grid)  # Down
            self.dfs_core(row, col - 1, grid)  # Left
            self.dfs_core(row, col + 1, grid)  # Right


# -----------------------------------------------------------------------------


class TestNumEnclaves(unittest.TestCase):
    """
    Unit tests for the Solution.numEnclaves method.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        """Test case from a typical example with multiple enclaves."""
        grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        expected = 3
        result = self.solution.numEnclaves(grid)
        self.assertEqual(result, expected)

    def test_example_two(self):
        """Test case with clear internal enclaves."""
        grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        expected = 0
        result = self.solution.numEnclaves(grid)
        self.assertEqual(result, expected)

    def test_with_enclaves(self):
        """Test case specifically designed to have enclosed land."""
        grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
        expected = 1
        result = self.solution.numEnclaves(grid)
        self.assertEqual(result, expected)

    def test_no_land(self):
        """Test case with an empty grid (all water)."""
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = 0
        result = self.solution.numEnclaves(grid)
        self.assertEqual(result, expected)

    def test_all_land_connected_to_boundary(self):
        """Test case where all land is connected to the boundary."""
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = 0
        result = self.solution.numEnclaves(grid)
        self.assertEqual(result, expected)

    def test_small_grid_enclave(self):
        """Test case for a minimal grid with an enclave."""
        grid = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        expected = 0
        result = self.solution.numEnclaves(grid)
        self.assertEqual(result, expected)

    def test_small_grid_with_enclave_2(self):
        """Test case for a minimal grid with an enclave."""
        grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = 0
        result = self.solution.numEnclaves(grid)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    # Run all defined tests
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
