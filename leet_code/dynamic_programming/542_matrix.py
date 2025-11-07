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
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        distance = [[0 for _ in range(n)] for _ in range(m)]
        q: deque[tuple[int, int]] = deque()

        # Initialize: add all 0 cells to queue
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    distance[i][j] = 10**9
                else:
                    distance[i][j] = 0
                    q.append((i, j))

        # Multi-source BFS from all 0 cells
        while q:
            row, col = q.popleft()
            new_distance = distance[row][col] + 1

            # Check all 4 neighbors
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if self._is_valid(nr, nc, m, n) and distance[nr][nc] > new_distance:
                    distance[nr][nc] = new_distance
                    q.append((nr, nc))

        return distance

    def _is_valid(self, row: int, col: int, m: int, n: int) -> bool:
        return 0 <= row < m and 0 <= col < n


class TestSolution(unittest.TestCase):
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
