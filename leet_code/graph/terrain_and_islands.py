"""
Problem: Terrain and Islands
Count connected components of land ('X') in a 2D terrain grid.

Approach:
- Scan the grid for unvisited land cells
- Run DFS from each land cell and mark all connected land as water
- Count each DFS launch as one island
- Time complexity: O(rows * cols)
- Space complexity: O(rows * cols) in the worst case recursion stack
"""

import unittest


class Solution:
    """DFS solution for counting islands in a terrain grid."""

    def countIslands(self, grid):
        """Return the number of connected groups of 'X' cells."""
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == ".":
                return

            grid[row][col] = "."
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(row + dr, col + dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "X":
                    islands += 1
                    dfs(row, col)

        return islands


class TestTerrainAndIslands(unittest.TestCase):
    """Unit tests for Solution.countIslands."""

    def setUp(self):
        self.solution = Solution()

    def test_empty_grid(self):
        self.assertEqual(self.solution.countIslands([]), 0)

    def test_single_island(self):
        grid = [
            ["X", "X", "."],
            ["X", ".", "."],
            [".", ".", "."],
        ]

        self.assertEqual(self.solution.countIslands(grid), 1)

    def test_multiple_islands(self):
        grid = [
            ["X", "X", ".", "."],
            [".", ".", "X", "."],
            ["X", ".", ".", "X"],
        ]

        self.assertEqual(self.solution.countIslands(grid), 4)

    def test_diagonal_cells_are_separate(self):
        grid = [
            ["X", "."],
            [".", "X"],
        ]

        self.assertEqual(self.solution.countIslands(grid), 2)

    def test_all_water(self):
        grid = [
            [".", "."],
            [".", "."],
        ]

        self.assertEqual(self.solution.countIslands(grid), 0)


if __name__ == "__main__":
    unittest.main()
