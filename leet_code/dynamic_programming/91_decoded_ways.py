"""
Problem: Count ways to decode a digit string into letters (1=A, 2=B, ..., 26=Z).

Approach:
- Use dynamic programming array
- dp[i] = number of ways to decode first i characters
- Check if single digit (1-9) or two digits (10-26) form valid codes
- Add previous decode counts if valid
- Time complexity: O(n) single pass
- Space complexity: O(n) for dp array

Example: "226" -> "BZ"(2,26), "VF"(22,6), "BBF"(2,2,6) = 3 ways
"""

import unittest


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1  # Empty string has one way
        dp[1] = 1  # First character (already checked not '0')

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digit = int(s[i - 2 : i])

            # Check if single digit is valid (1-9)
            if one_digit > 0:
                dp[i] += dp[i - 1]

            # Check if two digits form valid code (10-26)
            if 9 < two_digit < 27:
                dp[i] += dp[i - 2]

        return dp[n]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Tests a basic case with a clear number of decodings: '12' -> 2."""
        self.assertEqual(self.solution.numDecodings("12"), 2)

    def test_multiple_valid_combinations(self):
        """Tests a case with multiple valid two-digit combinations: '226' -> 3."""
        self.assertEqual(self.solution.numDecodings("226"), 3)

    def test_single_zero_in_middle(self):
        """Tests a case where a zero appears in the middle of the string: '10' -> 1."""
        self.assertEqual(self.solution.numDecodings("10"), 1)

    def test_leading_zero(self):
        """Tests a case where the string starts with zero: '06' -> 0."""
        self.assertEqual(self.solution.numDecodings("06"), 0)

    def test_consecutive_zeros(self):
        """Tests a case with consecutive zeros: '100' -> 0."""
        self.assertEqual(self.solution.numDecodings("100"), 0)

    def test_no_valid_two_digit_decodings(self):
        """Tests a case where no two-digit decodings are possible: '30' -> 0."""
        self.assertEqual(self.solution.numDecodings("30"), 0)

    def test_complex_case(self):
        """Tests a more complex case with many decodings: '12345' -> 3."""
        self.assertEqual(self.solution.numDecodings("12345"), 3)

    def test_empty_string(self):
        """Tests an empty input string -> 0."""
        self.assertEqual(self.solution.numDecodings(""), 0)

    def test_single_digit(self):
        """Tests a single digit string: '1' -> 1."""
        self.assertEqual(self.solution.numDecodings("1"), 1)


if __name__ == "__main__":
    unittest.main()
