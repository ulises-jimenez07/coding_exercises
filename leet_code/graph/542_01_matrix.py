"""
Problem: 01 Matrix / Minimum Distance to Nearest Car
Given a matrix where:
  0 = empty cell
  1 = car
  -1 = wall (impassable)

Return a matrix of the same dimensions where each cell contains the minimum distance
to the nearest car. Walls are excluded (their distance stays -1).

This generalizes LeetCode 542 - 01 Matrix (which uses 0/1 without walls).

Approach: Multi-Source BFS
- All cars are the "sources" — initialize the BFS queue with all car positions at distance 0.
- BFS spreads outward simultaneously from all sources. The first time any empty cell is
  reached, it is via the shortest path from the nearest car.
- Walls block traversal and keep their distance as -1.

Complexity:
- Time:  O(M × N)
- Space: O(M × N)
"""

import unittest
from collections import deque
from typing import List

EMPTY = 0
CAR = 1
WALL = -1


class Solution:
    """BFS-based solution for minimum distance to nearest car."""

    def minDistanceToCar(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Returns a matrix where each cell contains the minimum distance to the nearest car.
        Walls remain -1. Car cells are 0 (distance to themselves).
        """
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        queue: deque = deque()

        dist = [[-1] * cols for _ in range(rows)]

        # Multi-source BFS: start from every car at distance 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == CAR:
                    dist[r][c] = 0
                    queue.append((r, c))
                # Walls stay -1, so we don't need an explicit 'elif' here

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] == EMPTY and dist[nr][nc] == -1:
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr, nc))

        return dist


class TestMinDistanceToCar(unittest.TestCase):
    """Unit tests for Solution.minDistanceToCar."""

    def setUp(self):
        self.solution = Solution()

    def test_example_no_walls(self):
        """
        Input:
        0 0 0
        0 1 0
        1 0 0

        Cars at (1,1) and (2,0).
        Expected distances:
        2 1 2
        1 0 1
        0 1 2
        """
        matrix = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
        ]
        expected = [
            [2, 1, 2],
            [1, 0, 1],
            [0, 1, 2],
        ]
        self.assertEqual(self.solution.minDistanceToCar(matrix), expected)

    def test_single_car(self):
        """Single car in top-left, no walls."""
        matrix = [
            [1, 0],
            [0, 0],
        ]
        expected = [
            [0, 1],
            [1, 2],
        ]
        self.assertEqual(self.solution.minDistanceToCar(matrix), expected)

    def test_wall_blocks_path(self):
        """
        Wall separates two empty cells from the car — those cells are unreachable (-1).
        1 -1 0
        """
        matrix = [[1, -1, 0]]
        result = self.solution.minDistanceToCar(matrix)
        self.assertEqual(result[0][0], 0)  # car
        self.assertEqual(result[0][1], -1)  # wall
        self.assertEqual(result[0][2], -1)  # unreachable

    def test_all_walls_except_car(self):
        """Every cell is a wall except the car itself."""
        matrix = [
            [1, -1],
            [-1, -1],
        ]
        expected = [
            [0, -1],
            [-1, -1],
        ]
        self.assertEqual(self.solution.minDistanceToCar(matrix), expected)

    def test_no_cars(self):
        """No cars in the matrix — all non-wall cells remain -1."""
        matrix = [
            [0, 0],
            [0, 0],
        ]
        expected = [
            [-1, -1],
            [-1, -1],
        ]
        self.assertEqual(self.solution.minDistanceToCar(matrix), expected)

    def test_all_cars(self):
        """Every cell is a car — all distances are 0."""
        matrix = [
            [1, 1],
            [1, 1],
        ]
        expected = [
            [0, 0],
            [0, 0],
        ]
        self.assertEqual(self.solution.minDistanceToCar(matrix), expected)

    def test_single_cell_car(self):
        """Single-cell matrix containing a car."""
        self.assertEqual(self.solution.minDistanceToCar([[1]]), [[0]])

    def test_single_cell_empty(self):
        """Single-cell matrix that is empty (no car nearby)."""
        self.assertEqual(self.solution.minDistanceToCar([[0]]), [[-1]])

    def test_multiple_cars_choose_nearest(self):
        """Cell picks the closest car, not the first found."""
        # Cars at both ends; middle cell is equidistant
        matrix = [[1, 0, 0, 0, 1]]
        result = self.solution.minDistanceToCar(matrix)
        self.assertEqual(result, [[0, 1, 2, 1, 0]])

    def test_empty_matrix(self):
        """Empty input returns empty output."""
        self.assertEqual(self.solution.minDistanceToCar([]), [])


if __name__ == "__main__":
    unittest.main()
