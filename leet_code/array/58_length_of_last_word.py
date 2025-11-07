"""
Problem: Find the length of the last word in a string

Approach:
- Traverse from right to left, skip trailing spaces
- Count characters until next space or start of string
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Finds the length of the last word in a string."""
        pointer = len(s) - 1

        # Skip trailing spaces
        while pointer >= 0 and s[pointer] == " ":
            pointer -= 1

        res = 0

        # Count characters of last word
        while pointer >= 0 and s[pointer] != " ":
            pointer -= 1
            res += 1

        return res


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_case(self):
        """Spaces between words."""
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)

    def test_trailing_spaces(self):
        """Trailing spaces."""
        self.assertEqual(self.solution.lengthOfLastWord("fly me to the moon    "), 4)

    def test_no_trailing_spaces(self):
        """No trailing spaces."""
        self.assertEqual(self.solution.lengthOfLastWord("luffy is still joyboy"), 6)

    def test_single_word(self):
        """Single word."""
        self.assertEqual(self.solution.lengthOfLastWord("SingleWord"), 10)

    def test_only_spaces(self):
        """Only spaces."""
        self.assertEqual(self.solution.lengthOfLastWord("   "), 0)

    def test_empty_string(self):
        """Empty string."""
        self.assertEqual(self.solution.lengthOfLastWord(""), 0)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
