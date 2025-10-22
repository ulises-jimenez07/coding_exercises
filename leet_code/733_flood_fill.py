from typing import List
import unittest

# Define the Solution class for the Flood Fill algorithm
class Solution:
    """
    Implements the Flood Fill algorithm using Depth First Search (DFS).
    The goal is to change the color of a connected component of pixels
    starting at (sr, sc) with the same color as image[sr][sc] to a new 'color'.
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        The main function to initiate the flood fill operation.

        Args:
            image: The 2D grid representing the image.
            sr: The starting row for the fill.
            sc: The starting column for the fill.
            color: The new color to paint the connected component with.

        Returns:
            The modified image after the flood fill operation.
        """
        # Base case: If the starting pixel already has the new color, do nothing and return.
        if image[sr][sc] == color:
            return image
        
        # Store the original color of the starting pixel (the color to be replaced).
        self.old_color = image[sr][sc]
        # Store the new color to fill with.
        self.new_color = color
        
        # Start the Depth First Search from the starting coordinates (sr, sc).
        self.dfs(image, sr, sc)
        
        # Return the modified image.
        return image
    
    def dfs(self, image, row, col):
        """
        Recursive helper function for Depth First Search to perform the fill.

        Args:
            image: The 2D grid representing the image.
            row: The current row being checked/filled.
            col: The current column being checked/filled.
        """
        # Check boundary conditions and if the current pixel's color matches the old_color.
        # Boundary checks: 
        # 1. row is within the image height (0 to len(image) - 1).
        # 2. col is within the image width (0 to len(image[0]) - 1).
        # Color check: 
        # 3. The pixel at (row, col) has the color we intend to replace.
        if row >= 0 and row < len(image) and col>= 0 and col < len(image[0]) and image[row][col] == self.old_color:
            
            # If all conditions met, paint the current pixel with the new color.
            image[row][col]= self.new_color
            
            # Recursively call DFS for the four adjacent pixels (up, down, left, right).
            # Up
            self.dfs(image, row -1, col )
            # Down
            self.dfs(image, row +1, col )
            # Left
            self.dfs(image, row , col -1 )
            # Right
            self.dfs(image, row, col +1)

# -----------------------------------------------------------------------------
# Unit tests
# -----------------------------------------------------------------------------

class TestFloodFill(unittest.TestCase):
    """Unit test class for the Solution.floodFill method."""
    
    def test_example_case_1(self):
        """Test case from a standard example."""
        # Input image and parameters
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr, sc, color = 1, 1, 2
        # Expected output after flood fill
        expected = [[2,2,2],[2,2,0],[2,0,1]]
        # Create an instance of the Solution class
        s = Solution()
        # Call the floodFill method
        result = s.floodFill(image, sr, sc, color)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_already_colored(self):
        """Test case where the starting pixel already has the new color."""
        # Input image and parameters
        image = [[0,0,0],[0,0,0]]
        sr, sc, color = 0, 0, 0
        # Expected output (should be unchanged)
        expected = [[0,0,0],[0,0,0]]
        # Create an instance of the Solution class
        s = Solution()
        # Call the floodFill method
        result = s.floodFill(image, sr, sc, color)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

    def test_single_pixel(self):
        """Test case with a single pixel image."""
        # Input image and parameters
        image = [[5]]
        sr, sc, color = 0, 0, 9
        # Expected output
        expected = [[9]]
        # Create an instance of the Solution class
        s = Solution()
        # Call the floodFill method
        result = s.floodFill(image, sr, sc, color)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)
        
    def test_complex_shape(self):
        """Test case with a more complex shape to fill."""
        # Input image and parameters
        image = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
        sr, sc, color = 1, 1, 7
        # Expected output
        expected = [[0,0,0,0],[0,7,7,0],[0,7,7,0],[0,0,0,0]]
        # Create an instance of the Solution class
        s = Solution()
        # Call the floodFill method
        result = s.floodFill(image, sr, sc, color)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)
        
    def test_boundary_fill(self):
        """Test case where the fill starts at a boundary."""
        # Input image and parameters
        image = [[1,1,1],[1,1,1],[1,1,1]]
        sr, sc, color = 0, 0, 3
        # Expected output (all pixels should be 3)
        expected = [[3,3,3],[3,3,3],[3,3,3]]
        # Create an instance of the Solution class
        s = Solution()
        # Call the floodFill method
        result = s.floodFill(image, sr, sc, color)
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

# Boilerplate to run the tests when the script is executed directly
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)