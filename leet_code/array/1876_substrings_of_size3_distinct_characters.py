"""
Problem: Count substrings of length 3 with all distinct characters

Approach:
- Use fixed-size sliding window of size 3
- For each window, check if all 3 characters are distinct using set
- Slide window one position at a time through the string
- Time complexity: O(n) - single pass through string
- Space complexity: O(1) - fixed size set of at most 3 characters
"""

import unittest


class Solution:
    """Solution for LeetCode problem 1876: Substrings of Size Three with Distinct Characters."""

    def countGoodSubstrings(self, s: str) -> int:
        """Counts substrings of length 3 with all distinct characters using sliding window."""
        if len(s) < 3:
            return 0

        unique_three_sub = 0
        left = 0

        # Slide window of size 3 through the string
        for right in range(2, len(s)):
            # Check if all 3 characters in window are distinct
            if len(set(s[left:right + 1])) == 3:
                unique_three_sub += 1
            left += 1

        return unique_three_sub


class TestSolution(unittest.TestCase):
    """Test cases for Solution class."""

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """Multiple good substrings."""
        s = "xyzzaz"
        expected = 1  # "xyz"
        result = self.solution.countGoodSubstrings(s)
        self.assertEqual(result, expected)

    def test_example2(self):
        """All good substrings."""
        s = "aababcabc"
        expected = 4  # "aba", "bab", "abc", "bca", "cab", "abc"
        result = self.solution.countGoodSubstrings(s)
        self.assertEqual(result, expected)

    def test_short_string(self):
        """String shorter than 3 characters."""
        s = "ab"
        expected = 0
        result = self.solution.countGoodSubstrings(s)
        self.assertEqual(result, expected)

    def test_all_same(self):
        """All characters are the same."""
        s = "aaaa"
        expected = 0
        result = self.solution.countGoodSubstrings(s)
        self.assertEqual(result, expected)

    def test_exactly_three(self):
        """String of exactly length 3 with distinct characters."""
        s = "abc"
        expected = 1
        result = self.solution.countGoodSubstrings(s)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()