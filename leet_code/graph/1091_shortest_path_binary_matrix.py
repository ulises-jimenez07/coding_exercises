"""
Problem: Find the shortest path in a binary matrix from top-left to bottom-right.

Approach:
- Use BFS to explore all 8 directions (horizontal, vertical, and diagonal)
- Mark visited cells in the grid itself to avoid revisiting
- Store distance in each cell as we visit it
- Time complexity: O(n^2) where n is the dimension of the grid
- Space complexity: O(n^2) for the queue in worst case
"""

import unittest
from collections import deque
from typing import List


class Solution:
    """
    This class contains a method to solve the 'Shortest Path in Binary Matrix' problem.
    The goal is to find the shortest clear path from the top-left corner (0, 0) to the
    bottom-right corner (n-1, n-1) in an n x n binary matrix.

    A clear path has the following properties:
    - All visited cells are 0 (clear)
    - All adjacent cells in the path are connected in 8 directions
    - The path length is the number of cells visited
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Finds the shortest clear path in a binary matrix using BFS.

        The algorithm explores all 8 directions (up, down, left, right, and 4 diagonals)
        from each cell, marking visited cells and tracking distances.

        Args:
            grid: An n x n binary matrix where 0 represents a clear cell and 1 represents blocked

        Returns:
            The length of the shortest clear path, or -1 if no path exists
        """
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1

        # All 8 directions: horizontal, vertical, and diagonal
        directions = [(1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (0, 1), (0, -1)]
        queue: deque = deque()

        queue.append((0, 0))
        # Mark as visited by storing distance (path length = 1)
        # This prevents revisiting and serves as our distance tracker
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]

            if (row, col) == (rows - 1, cols - 1):
                return distance

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                # grid[nr][nc] == 0 means unvisited (we mark visited cells with distance > 0)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    # Mark as visited and store distance in one operation
                    grid[nr][nc] = distance + 1
                    queue.append((nr, nc))

        return -1


# -----------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def test_example_case_1(self):
        """
        Test case with a clear diagonal path.
        The shortest path goes from (0,0) to (2,2) diagonally.
        """
        grid = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
        expected = 3
        result = Solution().shortestPathBinaryMatrix(grid)
        self.assertEqual(result, expected, f"Expected path length {expected}, got {result}")

    def test_example_case_2(self):
        """
        Test case with a longer zigzag path.
        """
        grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
        expected = 4
        result = Solution().shortestPathBinaryMatrix(grid)
        self.assertEqual(result, expected, f"Expected path length {expected}, got {result}")

    def test_blocked_start(self):
        """
        Test case where the starting cell is blocked.
        Should return -1 immediately.
        """
        grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = -1
        result = Solution().shortestPathBinaryMatrix(grid)
        self.assertEqual(result, expected, "Should return -1 when start is blocked")

    def test_blocked_end(self):
        """
        Test case where the ending cell is blocked.
        Should return -1 immediately.
        """
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        expected = -1
        result = Solution().shortestPathBinaryMatrix(grid)
        self.assertEqual(result, expected, "Should return -1 when end is blocked")

    def test_no_path_exists(self):
        """
        Test case where no path exists from start to end.
        """
        grid = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
        expected = -1
        result = Solution().shortestPathBinaryMatrix(grid)
        self.assertEqual(result, expected, "Should return -1 when no path exists")

    def test_single_cell(self):
        """
        Test case with a 1x1 grid.
        The start is also the end.
        """
        grid = [[0]]
        expected = 1
        result = Solution().shortestPathBinaryMatrix(grid)
        self.assertEqual(result, expected, "Should return 1 for single clear cell")

    def test_single_cell_blocked(self):
        """
        Test case with a 1x1 blocked grid.
        """
        grid = [[1]]
        expected = -1
        result = Solution().shortestPathBinaryMatrix(grid)
        self.assertEqual(result, expected, "Should return -1 for single blocked cell")

    def test_all_clear_path(self):
        """
        Test case with all cells clear.
        Should find the shortest diagonal path.
        """
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = 3
        result = Solution().shortestPathBinaryMatrix(grid)
        self.assertEqual(result, expected, f"Expected diagonal path length {expected}")


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Boilerplate code to run the tests when the script is executed
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
