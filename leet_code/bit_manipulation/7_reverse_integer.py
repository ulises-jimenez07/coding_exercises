# solution.py
# test_solution.py

import unittest

class Solution:
    """
    This class contains a method to reverse an integer.
    """
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of an integer.

        Args:
            x (int): The integer to be reversed.

        Returns:
            int: The reversed integer. Returns 0 if the reversed integer overflows.
        """
        # Initialize a variable to store the reversed number.
        reversed_num = 0
        # Determine the sign of the input integer.
        sign = -1 if x < 0 else 1

        # Work with the absolute value of the number for easier digit manipulation.
        x = abs(x)

        # Loop through the digits of the number.
        while x != 0:
            # Extract the last digit.
            digit = x % 10
            # Append the digit to the reversed number.
            reversed_num = reversed_num * 10 + digit
            # Remove the last digit from the original number.
            x = x // 10

        # Apply the original sign to the reversed number.
        reversed_num *= sign

        # Check for integer overflow against the 32-bit signed integer range.
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num


class TestSolution(unittest.TestCase):
    """
    Test cases for the Solution class.
    """

    def test_positive_number(self):
        """
        Test a standard positive integer.
        """
        self.assertEqual(Solution().reverse(123), 321)

    def test_negative_number(self):
        """
        Test a standard negative integer.
        """
        self.assertEqual(Solution().reverse(-123), -321)

    def test_number_with_trailing_zeros(self):
        """
        Test a number with trailing zeros.
        """
        self.assertEqual(Solution().reverse(120), 21)

    def test_single_digit_number(self):
        """
        Test a single-digit integer.
        """
        self.assertEqual(Solution().reverse(7), 7)

    def test_zero(self):
        """
        Test the number zero.
        """
        self.assertEqual(Solution().reverse(0), 0)

    def test_overflow_positive(self):
        """
        Test for a positive integer that will overflow when reversed.
        """
        self.assertEqual(Solution().reverse(1534236469), 0)

    def test_overflow_negative(self):
        """
        Test for a negative integer that will overflow when reversed.
        """
        self.assertEqual(Solution().reverse(-2147483648), 0)

if __name__ == '__main__':
    unittest.main()