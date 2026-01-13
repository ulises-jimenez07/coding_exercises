"""
Problem: Find the length of the longest substring without repeating characters

Approach:
- Use sliding window with hash map to track character positions
- Expand window right, contract left when duplicate found
- Time complexity: O(n)
- Space complexity: O(min(n, m)) where m is charset size
"""

import unittest


class Solution:
    """Solution for finding the longest substring without repeating characters."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        """Finds the length of the longest substring without repeating characters."""
        max_length = 0
        prev_indexes: dict[str, int] = {}
        left = 0

        for right, ch in enumerate(s):
            if ch in prev_indexes:
                left = max(prev_indexes[ch] + 1, left)
            prev_indexes[ch] = right
            max_length = max(max_length, right - left + 1)
        return max_length


class TestLengthOfLongestSubstring(unittest.TestCase):
    """Unit tests for lengthOfLongestSubstring."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_repeating_characters(self):
        """All repeating characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_no_repeating(self):
        """No repeating characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_empty_string(self):
        """Empty string."""
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_character(self):
        """Single character."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)

    def test_all_unique(self):
        """All unique characters."""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdefg"), 7)


if __name__ == "__main__":
    unittest.main()
