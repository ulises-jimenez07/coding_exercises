"""
Problem: Convert a string to a 32-bit signed integer (atoi)

Approach:
- Skip whitespace, handle sign, parse digits with overflow checking
- Stop at first non-digit character
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def myAtoi(self, s: str) -> int:
        """Converts a string to a 32-bit integer."""
        sign = 1
        result = 0
        index = 0
        n = len(s)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        # Skip leading whitespace
        while index < n and s[index] == " ":
            index += 1

        # Check for sign
        if index < n and s[index] == "+":
            sign = 1
            index += 1
        elif index < n and s[index] == "-":
            sign = -1
            index += 1

        # Process digits
        while index < n and s[index].isdigit():
            digit = int(s[index])

            # Check for overflow
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            result = 10 * result + digit
            index += 1

        return sign * result


class TestMyAtoi(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_numbers(self):
        """Positive numbers."""
        self.assertEqual(self.solution.myAtoi("42"), 42)
        self.assertEqual(self.solution.myAtoi("   42"), 42)
        self.assertEqual(self.solution.myAtoi("0042"), 42)

    def test_negative_numbers(self):
        """Negative numbers."""
        self.assertEqual(self.solution.myAtoi("-42"), -42)
        self.assertEqual(self.solution.myAtoi("  -42  "), -42)

    def test_leading_zeros(self):
        """Leading zeros."""
        self.assertEqual(self.solution.myAtoi("0000042"), 42)

    def test_trailing_non_digits(self):
        """Trailing non-digits."""
        self.assertEqual(self.solution.myAtoi("4193 with words"), 4193)

    def test_leading_non_digits(self):
        """Leading non-digits."""
        self.assertEqual(self.solution.myAtoi("words and 987"), 0)

    def test_empty_string(self):
        """Empty string."""
        self.assertEqual(self.solution.myAtoi(""), 0)

    def test_whitespace_string(self):
        """Whitespace string."""
        self.assertEqual(self.solution.myAtoi("   "), 0)

    def test_overflow(self):
        """Overflow."""
        self.assertEqual(self.solution.myAtoi("2147483648"), 2147483647)
        self.assertEqual(self.solution.myAtoi("-2147483649"), -2147483648)

    def test_plus_sign(self):
        """Plus sign."""
        self.assertEqual(self.solution.myAtoi("+42"), 42)


if __name__ == "__main__":
    unittest.main()
