"""Module to solve the Backspace String Compare problem."""

import unittest


class Solution:
    """Provides a method to compare strings after processing backspaces."""

    def backspaceCompare(self, s: str, t: str) -> bool:
        """Checks if two strings are equal after backspace characters are processed."""
        i = len(s) - 1
        j = len(t) - 1

        def get_next_valid(string, index):
            """Finds the index of the next character that hasn't been backspaced."""
            skip = 0
            while index >= 0:
                if string[index] == "#":
                    skip += 1
                    index -= 1
                elif skip > 0:
                    index -= 1
                    skip -= 1
                else:
                    break
            return index

        while i >= 0 or j >= 0:
            i = get_next_valid(s, i)
            j = get_next_valid(t, j)

            # Compare identified valid characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            # One string has remaining valid characters while the other doesn't
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1
        return True


class TestBackspaceCompare(unittest.TestCase):
    """Unit tests for the BackspaceCompare solution."""

    def setUp(self):
        """Sets up the solution instance for testing."""
        self.solution = Solution()

    def test_basic_match(self):
        """Standard case with identical results."""
        self.assertTrue(self.solution.backspaceCompare("ab#c", "ad#c"))

    def test_both_empty(self):
        """Case where everything is deleted."""
        self.assertTrue(self.solution.backspaceCompare("ab##", "c#d#"))

    def test_mismatch(self):
        """Strings that result in different content."""
        self.assertFalse(self.solution.backspaceCompare("a#c", "b"))

    def test_multiple_backspaces(self):
        """Case with multiple backspaces in a row."""
        self.assertTrue(self.solution.backspaceCompare("a##c", "#a#c"))

    def test_complex_backspaces(self):
        """Complex sequence of characters and backspaces."""
        self.assertFalse(self.solution.backspaceCompare("bxj##tw", "bxj###tw"))


if __name__ == "__main__":
    unittest.main()
