"""
Problem: Traverse a 2D matrix in spiral order

Approach:
- Use four boundaries (top, bottom, left, right) and direction tracking
- Process one layer at a time, shrinking boundaries after each direction
- Time complexity: O(m*n)
- Space complexity: O(1) excluding output
"""

import unittest
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Traverses a 2D matrix in spiral order."""
        m = len(matrix)
        n = len(matrix[0])

        output = []

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        direction = 0

        while top <= bottom and left <= right:
            match direction:
                case 0:  # Left to right
                    for i in range(left, right + 1):
                        output.append(matrix[top][i])
                    top += 1
                    direction = 1
                case 1:  # Top to bottom
                    for i in range(top, bottom + 1):
                        output.append(matrix[i][right])
                    right -= 1
                    direction = 2
                case 2:  # Right to left
                    for i in range(right, left - 1, -1):
                        output.append(matrix[bottom][i])
                    bottom -= 1
                    direction = 3
                case 3:  # Bottom to top
                    for i in range(bottom, top - 1, -1):
                        output.append(matrix[i][left])
                    left += 1
                    direction = 0

        return output


class TestSpiralOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_3x3_matrix(self):
        """3x3 matrix."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_4x4_matrix(self):
        """4x4 matrix."""
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_1x5_matrix(self):
        """1x5 matrix."""
        matrix = [[1, 2, 3, 4, 5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_5x1_matrix(self):
        """5x1 matrix."""
        matrix = [[1], [2], [3], [4], [5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_2x3_matrix(self):
        """2x3 matrix."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [1, 2, 3, 6, 5, 4]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_3x2_matrix(self):
        """3x2 matrix."""
        matrix = [[1, 2], [3, 4], [5, 6]]
        expected = [1, 2, 4, 6, 5, 3]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_single_element_matrix(self):
        """Single element matrix."""
        matrix = [[1]]
        expected = [1]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_empty_matrix(self):
        """Empty matrix."""
        matrix = [[]]
        expected = []
        self.assertEqual(self.solution.spiralOrder(matrix), expected)


if __name__ == "__main__":
    unittest.main()
