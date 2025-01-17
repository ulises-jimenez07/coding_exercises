import unittest
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates a square matrix 90 degrees clockwise in-place.

        The rotation is performed by first transposing the matrix (swapping rows and columns)
        and then reflecting the matrix horizontally (reversing each row).

        Args:
            matrix: The square matrix to rotate.

        Do not return anything, modify matrix in-place instead.
        """

        def transpose(matrix):
            """Transposes the matrix in-place."""
            n = len(matrix)
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reflect(matrix):
            """Reflects the matrix horizontally in-place."""
            n = len(matrix)
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

        transpose(matrix)  # Transpose the matrix
        reflect(matrix)  # Reflect the matrix horizontally


class TestRotate(unittest.TestCase):
    def test_rotate_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_rotate_2(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_rotate_3(self):
        matrix = [[1]]
        expected = [[1]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_rotate_4(self):
        matrix = [[1, 2], [3, 4]]
        expected = [[3, 1], [4, 2]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)

    # Additional test cases for more comprehensive coverage

    def test_empty_matrix(self):
        matrix = []
        expected = []  # Empty matrix should remain empty
        Solution().rotate(matrix)  # Shouldn't raise any errors
        self.assertEqual(matrix, expected)

    def test_larger_matrix(self):  # Test with a 4x4 matrix
        matrix = [
            [i + j * 4 for i in range(1, 5)] for j in range(4)
        ]  # Generate a 4x4 matrix
        expected = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)


if __name__ == "__main__":
    unittest.main()
