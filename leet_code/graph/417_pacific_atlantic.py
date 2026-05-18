"""
Module providing a solution for the Pacific Atlantic Water Flow problem.
"""

import unittest
from typing import (
    List,
    Set,
    Tuple,
)


class Solution:
    """
    Class that solves the Pacific Atlantic Water Flow problem.
    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Finds all cells that can flow to both the Pacific and Atlantic oceans.
        """
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Sets to track which cells can reach each ocean
        atlantic: Set[Tuple[int, int]] = set()
        pacific: Set[Tuple[int, int]] = set()

        def dfs(r, c, reachable, prev_height):
            """
            Traverses the grid to find cells reachable from the ocean.
            """
            # Check bounds, height requirement, and if already visited
            if 0 <= r < rows and 0 <= c < cols and heights[r][c] >= prev_height and (r, c) not in reachable:
                reachable.add((r, c))
                # Explore all four possible directions
                for dr, dc in directions:
                    dfs(r + dr, c + dc, reachable, heights[r][c])

        # Run DFS from all cells adjacent to the top (Pacific) and bottom (Atlantic) edges
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # Run DFS from all cells adjacent to the left (Pacific) and right (Atlantic) edges
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        # Return intersection of cells reachable by both oceans
        return [list(cell) for cell in pacific & atlantic]


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def setUp(self):
        """
        Initializes the Solution instance before each test.
        """
        self.solution = Solution()

    def test_example_case(self):
        """
        Tests the standard LeetCode example case.
        """
        heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        result = self.solution.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_single_element(self):
        """
        Tests a grid with only one element.
        """
        heights = [[1]]
        expected = [[0, 0]]
        result = self.solution.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_empty_grid(self):
        """
        Tests an empty grid edge case.
        """
        heights = []
        expected = []
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(result, expected)

    def test_all_same_height(self):
        """
        Tests a grid where all elements have the same height.
        """
        heights = [[2, 2], [2, 2]]
        expected = [[0, 0], [0, 1], [1, 0], [1, 1]]
        result = self.solution.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
