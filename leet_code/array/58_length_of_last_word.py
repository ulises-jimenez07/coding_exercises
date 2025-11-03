import unittest

class Solution:
    """
    Implements a method to find the length of the last word in a given string 's'.
    A "word" is defined as a maximal substring consisting of non-space characters.
    """
    def lengthOfLastWord(self, s: str) -> int:
        """
        Calculates the length of the last word in the string 's' by traversing 
        the string backward.

        Args:
            s (str): The input string, which may contain spaces and words.

        Returns:
            int: The length of the last word.
        """
        # Initialize a pointer to the index of the very last character in the string.
        pointer = len(s) - 1
        
        # --- Step 1: Skip trailing spaces ---
        # Move the pointer backward until the first non-space character is found, 
        # or the beginning of the string is reached.
        while pointer >= 0 and s[pointer] == ' ':
            pointer -= 1

        # Initialize the result variable to count the characters of the last word.
        res = 0

        # --- Step 2: Count characters of the last word ---
        # Continue moving the pointer backward, counting characters, 
        # as long as we haven't hit the start of the string or a space.
        while pointer >= 0 and s[pointer] != ' ':
            pointer -= 1
            res += 1

        # 'res' now holds the total count of characters found in the last word.
        return res

# --- Unit Tests ---

class TestLengthOfLastWord(unittest.TestCase):
    """
    Unit tests for the lengthOfLastWord method in the Solution class.
    """

    def test_standard_case(self):
        """Test with a string having spaces between words."""
        solution = Solution()
        s = "Hello World"
        # The last word is "World", length 5
        self.assertEqual(solution.lengthOfLastWord(s), 5)

    def test_trailing_spaces(self):
        """Test with a string that ends in multiple spaces."""
        solution = Solution()
        s = "fly me to the moon    "
        # The last word is "moon", length 4
        self.assertEqual(solution.lengthOfLastWord(s), 4)

    def test_no_trailing_spaces(self):
        """Test with a string that has no trailing spaces."""
        solution = Solution()
        s = "luffy is still joyboy"
        # The last word is "joyboy", length 6
        self.assertEqual(solution.lengthOfLastWord(s), 6)

    def test_single_word(self):
        """Test with a string containing only one word."""
        solution = Solution()
        s = "SingleWord"
        self.assertEqual(solution.lengthOfLastWord(s), 10)

    def test_only_spaces(self):
        """Test with a string containing only spaces."""
        solution = Solution()
        s = "   "
        # Should return 0 as there is no word
        self.assertEqual(solution.lengthOfLastWord(s), 0)

    def test_empty_string(self):
        """Test with an empty input string."""
        solution = Solution()
        s = ""
        # Should return 0
        self.assertEqual(solution.lengthOfLastWord(s), 0)

if __name__ == '__main__':
    # Run tests only if the script is executed directly
    unittest.main(argv=['first-arg-is-ignored'], exit=False)