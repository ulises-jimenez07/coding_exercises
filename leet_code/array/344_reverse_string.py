from typing import List
import unittest

class Solution:
    """
    A class containing methods for string manipulation problems.
    """
    def reverseString(self, s: List[str]) -> List[str]:
        """
        Reverses the input list of characters (string) in-place 
        using a two-pointer approach.

        Args:
            s: The list of characters to be reversed. It is modified directly.
        
        Returns:
            The modified list (for testing convenience, though modification is in-place).
        """
        # Initialize two pointers: 'start' at the beginning and 'end' at the end of the list.
        start = 0
        end = len(s) - 1

        # Continue swapping elements as long as the 'start' pointer has not passed the 'end' pointer.
        while start <= end:
            # Swap the characters at the 'start' and 'end' positions simultaneously.
            s[start], s[end] = s[end], s[start]
            
            # Move the pointers towards the center.
            start += 1
            end -= 1
        
        # Return the list, which has been modified in-place.
        return s 

# --- Unit Tests ---

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class's reverseString method.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_basic_odd_length(self):
        """Test with a simple, odd-length string: 'hello' -> 'olleh'."""
        input_list = ["h", "e", "l", "l", "o"]
        expected_list = ["o", "l", "l", "e", "h"]
        # The method modifies input_list in-place
        self.solution.reverseString(input_list)
        self.assertEqual(input_list, expected_list, "Should correctly reverse an odd-length list")

    def test_even_length(self):
        """Test with an even-length string: 'race' -> 'ecar'."""
        input_list = ["r", "a", "c", "e"]
        expected_list = ["e", "c", "a", "r"]
        self.solution.reverseString(input_list)
        self.assertEqual(input_list, expected_list, "Should handle even-length lists")

    def test_single_character(self):
        """Test with a list containing only one character."""
        input_list = ["a"]
        expected_list = ["a"]
        self.solution.reverseString(input_list)
        self.assertEqual(input_list, expected_list, "Should handle a single element list correctly")

    def test_empty_list(self):
        """Test with an empty list (edge case)."""
        input_list: List[str] = []
        expected_list: List[str] = []
        self.solution.reverseString(input_list)
        self.assertEqual(input_list, expected_list, "Should return an empty list for an empty input")

# Execute the tests when the script is run directly
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)