"""
Problem: Rotate a square matrix 90 degrees clockwise in-place

Approach:
- Transpose the matrix (swap across diagonal)
- Reflect horizontally (reverse each row)
- Time complexity: O(n^2)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotates a square matrix 90 degrees clockwise in-place."""

        def transpose(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reflect(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

        transpose(matrix)
        reflect(matrix)


class TestRotate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_3x3_matrix(self):
        """3x3 matrix rotation."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_4x4_matrix(self):
        """4x4 matrix rotation."""
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])

    def test_1x1_matrix(self):
        """Single element matrix."""
        matrix = [[1]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, [[1]])

    def test_2x2_matrix(self):
        """2x2 matrix rotation."""
        matrix = [[1, 2], [3, 4]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, [[3, 1], [4, 2]])

    def test_empty_matrix(self):
        """Empty matrix."""
        matrix = []
        self.solution.rotate(matrix)
        self.assertEqual(matrix, [])


if __name__ == "__main__":
    unittest.main()
