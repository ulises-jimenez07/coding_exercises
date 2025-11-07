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
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Finds the length of the longest substring without repeating characters."""
        if len(s) <= 1:
            return len(s)

        seen: dict[str, int] = {}
        max_length = 0
        left = right = 0

        for i in range(len(s)):
            if s[i] in seen:
                left = max(left, seen[s[i]] + 1)

            right += 1
            seen[s[i]] = i
            max_length = max(right - left, max_length)

        return max_length


class TestLengthOfLongestSubstring(unittest.TestCase):
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
