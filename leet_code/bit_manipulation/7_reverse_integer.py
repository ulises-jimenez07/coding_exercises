"""
Problem: Reverse the digits of a 32-bit signed integer

Approach:
- Extract digits one by one using modulo and integer division
- Build reversed number by multiplying by 10 and adding digit
- Return 0 if result overflows 32-bit signed integer range
- Time complexity: O(log n) where n is the input value
- Space complexity: O(1)
"""

import unittest


class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        reversed_num *= sign

        # Check for 32-bit overflow
        if reversed_num < -(2**31) or reversed_num > 2**31 - 1:
            return 0
        return reversed_num


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_number(self):
        """Test a standard positive integer."""
        self.assertEqual(self.solution.reverse(123), 321)

    def test_negative_number(self):
        """Test a standard negative integer."""
        self.assertEqual(self.solution.reverse(-123), -321)

    def test_number_with_trailing_zeros(self):
        """Test a number with trailing zeros."""
        self.assertEqual(self.solution.reverse(120), 21)

    def test_single_digit_number(self):
        """Test a single-digit integer."""
        self.assertEqual(self.solution.reverse(7), 7)

    def test_zero(self):
        """Test the number zero."""
        self.assertEqual(self.solution.reverse(0), 0)

    def test_overflow_positive(self):
        """Test for a positive integer that will overflow when reversed."""
        self.assertEqual(self.solution.reverse(1534236469), 0)

    def test_overflow_negative(self):
        """Test for a negative integer that will overflow when reversed."""
        self.assertEqual(self.solution.reverse(-2147483648), 0)


if __name__ == "__main__":
    unittest.main()
