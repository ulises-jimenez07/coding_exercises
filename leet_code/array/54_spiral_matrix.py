from typing import List
import unittest

class Solution:
    """
    Given an m x n matrix, return all elements of the matrix in spiral order.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Traverses a 2D matrix in a spiral pattern and returns the elements in a single list.

        Args:
            matrix: A list of lists of integers representing the matrix.

        Returns:
            A list of integers containing the elements of the matrix in spiral order.
        """
        # Get the dimensions of the matrix
        m = len(matrix)
        n = len(matrix[0])
        
        # Initialize the output list to store the spiral order elements
        output = []
        
        # Define the boundaries of the matrix traversal
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        
        # 'direction' determines the current traversal direction:
        # 0: left to right (top row)
        # 1: top to bottom (right column)
        # 2: right to left (bottom row)
        # 3: bottom to top (left column)
        direction = 0

        # Loop until the boundaries cross each other
        while top <= bottom and left <= right:
            # Match statement to handle different directions
            match direction:
                case 0:  # Traverse from left to right along the top row
                    for i in range(left, right + 1):
                        output.append(matrix[top][i])
                    # Move the top boundary down and change direction
                    top += 1
                    direction = 1
                case 1:  # Traverse from top to bottom along the right column
                    for i in range(top, bottom + 1):
                        output.append(matrix[i][right])
                    # Move the right boundary left and change direction
                    right -= 1
                    direction = 2
                case 2:  # Traverse from right to left along the bottom row
                    for i in range(right, left - 1, -1):
                        output.append(matrix[bottom][i])
                    # Move the bottom boundary up and change direction
                    bottom -= 1
                    direction = 3
                case 3:  # Traverse from bottom to top along the left column
                    for i in range(bottom, top - 1, -1):
                        output.append(matrix[i][left])
                    # Move the left boundary right and change direction
                    left += 1
                    direction = 0
        
        return output

class TestSpiralOrder(unittest.TestCase):
    """
    Unit tests for the spiralOrder method.
    """
    def test_3x3_matrix(self):
        """
        Test case for a 3x3 matrix.
        """
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_4x4_matrix(self):
        """
        Test case for a 4x4 matrix.
        """
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_1x5_matrix(self):
        """
        Test case for a 1x5 matrix.
        """
        matrix = [[1, 2, 3, 4, 5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_5x1_matrix(self):
        """
        Test case for a 5x1 matrix.
        """
        matrix = [[1], [2], [3], [4], [5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_2x3_matrix(self):
        """
        Test case for a 2x3 matrix.
        """
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [1, 2, 3, 6, 5, 4]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_3x2_matrix(self):
        """
        Test case for a 3x2 matrix.
        """
        matrix = [[1, 2], [3, 4], [5, 6]]
        expected = [1, 2, 4, 6, 5, 3]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_single_element_matrix(self):
        """
        Test case for a matrix with a single element.
        """
        matrix = [[1]]
        expected = [1]
        self.assertEqual(Solution().spiralOrder(matrix), expected)

    def test_empty_matrix(self):
        """
        Test case for an empty matrix.
        """
        matrix = [[]]
        # An empty matrix will result in an empty list
        expected = []
        self.assertEqual(Solution().spiralOrder(matrix), expected)

if __name__ == '__main__':
    unittest.main()