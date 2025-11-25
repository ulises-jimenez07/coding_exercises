"""
Problem: Find distance to nearest 0 for each cell in binary matrix.

Approach:
- Use multi-source BFS starting from all 0 cells
- Initialize all 1 cells with infinity distance
- Process all 0 cells simultaneously in BFS queue
- Update neighbors with minimum distance
- Time complexity: O(m * n) visit each cell once
- Space complexity: O(m * n) for queue and distance matrix

Example: [[0,0,0],[0,1,0],[1,1,1]] -> [[0,0,0],[0,1,0],[1,2,1]]
"""

import unittest
from collections import deque
from math import inf
from typing import List


class Solution:
    """Solution for LeetCode 542: 01 Matrix using multi-source BFS."""

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int | float]]:  # pylint: disable=too-many-locals
        rows, cols = len(mat), len(mat[0])
        distances: List[List[int | float]] = [[0 for _ in range(cols)] for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue: deque[tuple[int, int]] = deque()

        # Initialize: add all 0 cells to queue
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    distances[i][j] = inf
                else:
                    queue.append((i, j))

        # Multi-source BFS from all 0 cells
        while queue:
            row, col = queue.popleft()
            new_distance = distances[row][col] + 1

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and distances[nr][nc] > new_distance:
                    distances[nr][nc] = new_distance
                    queue.append((nr, nc))

        return distances


class TestSolution(unittest.TestCase):
    """Unit tests for Solution class."""

    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example_1(self):
        """Test case from LeetCode example 1."""
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(self.solution.updateMatrix(mat), expected)

    def test_leetcode_example_2(self):
        """Test case from LeetCode example 2."""
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        self.assertEqual(self.solution.updateMatrix(mat), expected)

    def test_single_element_matrix(self):
        """Test case for a single-element matrix."""
        mat = [[0]]
        expected = [[0]]
        self.assertEqual(self.solution.updateMatrix(mat), expected)

    def test_matrix_with_no_zeros(self):
        """Test case for a matrix with no zeros. All distances should be inf."""
        mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = [
            [float("inf"), float("inf"), float("inf")],
            [float("inf"), float("inf"), float("inf")],
            [float("inf"), float("inf"), float("inf")],
        ]
        result = self.solution.updateMatrix(mat)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
