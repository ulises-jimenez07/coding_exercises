"""
Problem: Perform flood fill starting from a pixel, changing connected same-color pixels to new color.

Approach:
- Use DFS to recursively fill all connected pixels with matching color
- Skip if starting color already matches new color
- Time complexity: O(m * n)
- Space complexity: O(m * n) for recursion stack
"""

import unittest
from typing import List


class Solution:
    """
    Implements the Flood Fill algorithm using Depth First Search (DFS).
    """

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Performs a flood fill on a 2D grid 'image' starting from a seed pixel (sr, sc).

        Args:
            image: The 2D grid of pixel values (integers).
            sr: The starting row (source row) of the seed pixel.
            sc: The starting column (source column) of the seed pixel.
            color: The new color to paint the connected component with.

        Returns:
            The modified image after the flood fill operation.
        """
        # Get the color of the starting pixel
        start_color = image[sr][sc]

        # If the starting color is already the new color, no operation is needed.
        if start_color == color:
            return image

        # Store the colors as instance variables for easy access within the recursive dfs
        self.old_color = start_color
        self.new_color = color

        # Start the Depth First Search (DFS) from the seed pixel
        self.dfs(image, sr, sc)

        return image

    def dfs(self, image: List[List[int]], row: int, col: int):
        """
        Recursive helper function for Depth First Search.

        Args:
            image: The 2D grid (passed by reference, so modifications are permanent).
            row: The current row index.
            col: The current column index.
        """
        # Check boundary conditions and if the current pixel has the target 'old_color'
        if row >= 0 and row < len(image) and col >= 0 and col < len(image[0]) and image[row][col] == self.old_color:

            # 1. Paint the current pixel with the 'new_color'
            image[row][col] = self.new_color

            # 2. Recursively call DFS on the four cardinal neighbors (up, down, left, right)

            # Neighbor up
            self.dfs(image, row - 1, col)
            # Neighbor down
            self.dfs(image, row + 1, col)
            # Neighbor left
            self.dfs(image, row, col - 1)
            # Neighbor right
            self.dfs(image, row, col + 1)


# ---
## Unit Tests
# ---


class TestFloodFill(unittest.TestCase):
    """
    Test suite for the Solution.floodFill method.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_case_1(self):
        """Tests a standard flood fill operation."""
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr, sc, color = 1, 1, 2
        expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        result = self.solution.floodFill(image, sr, sc, color)
        self.assertEqual(result, expected)

    def test_already_correct_color(self):
        """Tests the case where the starting pixel already has the new color."""
        image = [[0, 0, 0], [0, 1, 0]]
        # Starting pixel (1, 1) has color 1, new color is 1. Should return the original image.
        sr, sc, color = 1, 1, 1
        expected = [[0, 0, 0], [0, 1, 0]]
        result = self.solution.floodFill(image, sr, sc, color)
        self.assertEqual(result, expected)

    def test_edge_case_single_pixel(self):
        """Tests a single-pixel image."""
        image = [[5]]
        sr, sc, color = 0, 0, 9
        expected = [[9]]
        result = self.solution.floodFill(image, sr, sc, color)
        self.assertEqual(result, expected)

    def test_no_connected_component(self):
        """Tests a case where only the starting pixel is changed."""
        image = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # Starting pixel (1, 1) has color 5. No adjacent pixels have color 5.
        sr, sc, color = 1, 1, 0
        expected = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
        result = self.solution.floodFill(image, sr, sc, color)
        self.assertEqual(result, expected)

    def test_fill_entire_image(self):
        """Tests a case where the entire image is filled."""
        image = [[7, 7, 7], [7, 7, 7], [7, 7, 7]]
        sr, sc, color = 0, 0, 5
        expected = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        result = self.solution.floodFill(image, sr, sc, color)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
