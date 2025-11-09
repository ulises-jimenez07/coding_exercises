"""
Problem: Find maximum number of vowels in a substring of given length k

Approach:
- Use fixed-size sliding window technique to track vowels in current window
- Initialize window with first k characters and count vowels
- Slide window by removing leftmost character and adding new rightmost character
- Update vowel count when characters entering/leaving are vowels
- Time complexity: O(n) - single pass through string
- Space complexity: O(1) - constant space for vowel set and counters
"""

import unittest


class Solution:
    """Solution for LeetCode problem 1456: Maximum Number of Vowels in a Substring of Given Length."""

    def maxVowels(self, s: str, k: int) -> int:
        """Finds maximum number of vowels in any substring of length k using sliding window."""
        # Get first window of size k
        window = s[:k]
        vowels = {"a", "e", "i", "o", "u"}
        current_vowels = 0

        # Count vowels in initial window
        for c in window:
            if c in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # Slide window through rest of string
        for i in range(k, len(s)):
            # Remove leftmost char if it's a vowel
            if s[i - k] in vowels:
                current_vowels -= 1
            # Add new rightmost char if it's a vowel
            if s[i] in vowels:
                current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels


class TestSolution(unittest.TestCase):
    """Test cases for Solution class."""

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """Standard case with vowels scattered throughout."""
        s = "abciiidef"
        k = 3
        expected = 3  # substring "iii"
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, expected)

    def test_example2(self):
        """Case with mixed vowels and consonants."""
        s = "aeiou"
        k = 2
        expected = 2  # any 2-char substring has 2 vowels
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, expected)

    def test_example3(self):
        """Case with mostly consonants."""
        s = "leetcode"
        k = 3
        expected = 2  # substring "lee" or "eet"
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, expected)

    def test_no_vowels(self):
        """Case with no vowels."""
        s = "rhythms"
        k = 3
        expected = 0
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, expected)

    def test_all_vowels(self):
        """Case with all vowels."""
        s = "aeiouaeiou"
        k = 5
        expected = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, expected)

    def test_single_character(self):
        """Window size of 1."""
        s = "weallloveyou"
        k = 1
        expected = 1
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, expected)

    def test_full_string(self):
        """Window size equals string length."""
        s = "hello"
        k = 5
        expected = 2  # 'e' and 'o'
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
