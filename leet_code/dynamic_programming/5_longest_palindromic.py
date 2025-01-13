import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        Finds the longest palindromic substring within a given string.

        :type s: str
        :rtype: str
        """
        n = len(s)  # Get the length of the input string
        if n < 2:  # Handle empty or single-character strings
            return s

        ans = ""  # Initialize the longest palindrome to an empty string

        # Create a 2D table to store boolean values indicating whether
        # the substring s[i:j+1] is a palindrome.
        is_palindrome = [[False] * n for _ in range(n)]

        # All single characters are palindromes.
        for i in range(n):
            is_palindrome[i][i] = True

        # Iterate through all possible substring lengths, starting from 2.
        for end in range(n):
            for start in range(end + 1):
                # Check if the characters at start and end indices are the same.
                same_char = s[start] == s[end]

                # The substring between start and end is a palindrome if the characters
                # at start and end are the same and either:
                # 1. The substring has length 2 or 3 (middle part has length 0 or 1).
                # 2. The inner substring (excluding start and end) is a palindrome.
                middle_string_lenght = end - start - 1
                if same_char and (
                    middle_string_lenght <= 1 or is_palindrome[start + 1][end - 1]
                ):
                    is_palindrome[start][end] = True

                    # If current substring is longer than current answer, update answer
                    if end - start >= len(
                        ans
                    ):  # Or > to prioritize later substrings if they have the same max length
                        ans = s[start : end + 1]

        return ans  # Return the longest palindromic substring


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertEqual(self.solution.longestPalindrome(""), "")

    def test_single_character_string(self):
        self.assertEqual(self.solution.longestPalindrome("a"), "a")

    def test_two_character_palindrome(self):
        self.assertEqual(self.solution.longestPalindrome("aa"), "aa")

    def test_two_character_non_palindrome(self):
        self.assertEqual(
            self.solution.longestPalindrome("ab"), "a"
        )  # or "b", both are accepted

    def test_simple_palindrome(self):
        self.assertEqual(self.solution.longestPalindrome("aba"), "aba")

    def test_longer_palindrome(self):
        self.assertEqual(
            self.solution.longestPalindrome("babad"), "bab" or "aba"
        )  # Either is accepted

    def test_palindrome_at_the_end(self):
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")

    def test_example_string(self):
        self.assertIn(
            self.solution.longestPalindrome("bananas"), ["anana", "banana"]
        )  # banana is accepted, since both banana and anana have max length.

    def test_edge_cases(
        self,
    ):  # Check some edge case where multiple palindromes are present
        self.assertIn(
            self.solution.longestPalindrome("racecar"), ["racecar"]
        )  # racecar is accepted, as it's the longest
        self.assertIn(
            self.solution.longestPalindrome("abcba"), ["abcba"]
        )  # abcba is accepted, as it's the longest


if __name__ == "__main__":
    unittest.main()
