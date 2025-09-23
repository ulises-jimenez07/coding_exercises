import unittest

class Solution:
    """
    This class contains a method to calculate the number of ways a string can be decoded.
    """
    def numDecodings(self, s: str) -> int:
        """
        Calculates the number of possible decodings for a string of digits.

        The method uses dynamic programming to solve the problem. Each digit can be decoded
        as a single-digit number (1-9) or, in combination with the previous digit, as a
        two-digit number (10-26).

        Args:
            s: The string of digits to be decoded.

        Returns:
            The total number of ways the string can be decoded.
        """
        # A string starting with '0' or an empty string has no valid decodings.
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i] will store the number of ways to decode the substring s[0...i-1].
        dp = [0] * (n + 1)

        # Base cases:
        # dp[0] = 1 represents an empty string, which has one way to be decoded (empty).
        dp[0] = 1
        # dp[1] = 1 represents a single digit string (not '0'), which has one way to be decoded.
        dp[1] = 1

        # Iterate from the second digit to the end of the string.
        for i in range(2, n + 1):
            # one_digit is the value of the current digit.
            one_digit = int(s[i-1])
            # two_digit is the value of the two-digit number formed by the last two digits.
            two_digit = int(s[i-2:i])

            # If the current digit is not '0', it can be decoded independently.
            # We add the number of ways to decode the substring up to the previous digit.
            if one_digit > 0:
                dp[i] += dp[i-1]
            
            # If the two-digit number is between 10 and 26 (inclusive), it can be decoded
            # as a combined unit. We add the number of ways to decode the substring
            # up to two digits before the current one.
            if 9 < two_digit < 27:
                dp[i] += dp[i-2]

        return dp[n]

# ---

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class's numDecodings method.
    """

    def test_basic_case(self):
        """Tests a basic case with a clear number of decodings."""
        self.assertEqual(Solution().numDecodings("12"), 2) # "12" can be decoded as "AB" (1, 2) or "L" (12)

    def test_multiple_valid_combinations(self):
        """Tests a case with multiple valid two-digit combinations."""
        self.assertEqual(Solution().numDecodings("226"), 3) # "226" can be "BBF" (2,2,6), "VF" (22,6), "BZ" (2,26)

    def test_single_zero_in_middle(self):
        """Tests a case where a zero appears in the middle of the string."""
        self.assertEqual(Solution().numDecodings("10"), 1) # "10" can only be "J" (10). "1,0" is not valid.

    def test_leading_zero(self):
        """Tests a case where the string starts with zero."""
        self.assertEqual(Solution().numDecodings("06"), 0) # A string starting with '0' cannot be decoded.

    def test_consecutive_zeros(self):
        """Tests a case with consecutive zeros."""
        self.assertEqual(Solution().numDecodings("100"), 0) # '00' is not a valid decoding.

    def test_no_valid_two_digit_decodings(self):
        """Tests a case where no two-digit decodings are possible."""
        self.assertEqual(Solution().numDecodings("30"), 0) # '30' is not a valid decoding.

    def test_complex_case(self):
        """Tests a more complex case with many decodings."""
        self.assertEqual(Solution().numDecodings("12345"), 3) # "1,2,3,4,5", "12,3,4,5", "1,23,4,5"

    def test_empty_string(self):
        """Tests an empty input string."""
        self.assertEqual(Solution().numDecodings(""), 0)

    def test_single_digit(self):
        """Tests a single digit string."""
        self.assertEqual(Solution().numDecodings("1"), 1)

if __name__ == '__main__':
    unittest.main()