"""
Problem: Find the longest palindromic substring in a given string.

Approach:
- Use dynamic programming with 2D table
- dp[start][end] = True if substring s[start:end+1] is palindrome
- Build from smaller substrings to larger ones
- Check if ends match and middle is palindrome
- Time complexity: O(n²) nested loops
- Space complexity: O(n²) for dp table

Example: "babad" -> "bab" or "aba" (both valid)
"""

import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        ans = ""
        is_palindrome = [[False] * n for _ in range(n)]

        # Single characters are palindromes
        for i in range(n):
            is_palindrome[i][i] = True

        for end in range(n):
            for start in range(end + 1):
                same_char = s[start] == s[end]
                middle_string_length = end - start - 1

                # Check if palindrome: ends match and middle is palindrome
                if same_char and (middle_string_length <= 1 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True

                    # Update answer if longer palindrome found
                    if end - start >= len(ans):
                        ans = s[start : end + 1]

        return ans


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(self.solution.longestPalindrome(""), "")

    def test_single_character_string(self):
        """Test with a single character string."""
        self.assertEqual(self.solution.longestPalindrome("a"), "a")

    def test_two_character_palindrome(self):
        """Test with a two-character palindrome."""
        self.assertEqual(self.solution.longestPalindrome("aa"), "aa")

    def test_two_character_non_palindrome(self):
        """Test with a two-character non-palindrome."""
        self.assertIn(self.solution.longestPalindrome("ab"), ["a", "b"])

    def test_simple_palindrome(self):
        """Test with a simple palindrome."""
        self.assertEqual(self.solution.longestPalindrome("aba"), "aba")

    def test_longer_palindrome(self):
        """Test with a longer palindrome, expecting one of two valid results."""
        self.assertIn(self.solution.longestPalindrome("babad"), ["bab", "aba"])

    def test_palindrome_at_the_end(self):
        """Test with a palindrome at the end of the string."""
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")

    def test_example_string_multiple_palindromes(self):
        """Test with an example string containing multiple palindromes."""
        self.assertIn(self.solution.longestPalindrome("bananas"), ["anana"])

    def test_full_string_palindrome(self):
        """Test with a string that is itself a palindrome."""
        self.assertEqual(self.solution.longestPalindrome("racecar"), "racecar")

    def test_another_full_string_palindrome(self):
        """Test with another string that is itself a palindrome."""
        self.assertEqual(self.solution.longestPalindrome("abcba"), "abcba")


if __name__ == "__main__":
    unittest.main()
