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
    """Standard solution class for the longest palindromic substring problem."""

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


def longest_palindrome_in_a_string(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    # dp[i][j] will be True if substring s[i...j] is a palindrome
    dp = [[False] * n for _ in range(n)]

    max_len = 1
    start_index = 0

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2
            start_index = i

    # Check for palindromes of length 3 or more
    # substring_len is the length of the substring we are checking
    for substring_len in range(3, n + 1):
        # i is the starting index of the substring
        for i in range(n - substring_len + 1):
            # j is the ending index of the substring
            j = i + substring_len - 1

            # Condition for s[i...j] to be a palindrome:
            # 1. First and last characters must match (s[i] == s[j])
            # 2. The inner substring s[i+1...j-1] must be a palindrome (dp[i+1][j-1])
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                max_len = substring_len
                start_index = i

    return s[start_index : start_index + max_len]


class TestLongestPalindrome(unittest.TestCase):
    """Unit tests for the longest palindromic substring implementations."""

    def setUp(self):
        self.implementations = [
            Solution().longestPalindrome,
            longest_palindrome_in_a_string,
        ]

    def test_empty_string(self):
        """Test with an empty string."""
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                self.assertEqual(impl(""), "")

    def test_single_character_string(self):
        """Test with a single character string."""
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                self.assertEqual(impl("a"), "a")

    def test_two_character_palindrome(self):
        """Test with a two-character palindrome."""
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                self.assertEqual(impl("aa"), "aa")

    def test_two_character_non_palindrome(self):
        """Test with a two-character non-palindrome."""
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                self.assertIn(impl("ab"), ["a", "b"])

    def test_simple_palindrome(self):
        """Test with a simple palindrome."""
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                self.assertEqual(impl("aba"), "aba")

    def test_longer_palindrome(self):
        """Test with a longer palindrome, expecting one of two valid results."""
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                self.assertIn(impl("babad"), ["bab", "aba"])

    def test_palindrome_at_the_end(self):
        """Test with a palindrome at the end of the string."""
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                self.assertEqual(impl("cbbd"), "bb")

    def test_example_string_multiple_palindromes(self):
        """Test with an example string containing multiple palindromes."""
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                self.assertIn(impl("bananas"), ["anana"])

    def test_full_string_palindrome(self):
        """Test with a string that is itself a palindrome."""
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                self.assertEqual(impl("racecar"), "racecar")

    def test_another_full_string_palindrome(self):
        """Test with another string that is itself a palindrome."""
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                self.assertEqual(impl("abcba"), "abcba")


if __name__ == "__main__":
    unittest.main()
