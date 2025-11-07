"""
Problem: Divide two integers without using multiplication, division, or modulo

Approach:
- Use bit shifting to multiply divisor by powers of 2
- Subtract largest possible shifted divisor from dividend
- Handle overflow and sign edge cases
- Time complexity: O(log²n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case
        if dividend == (-1 << 31) and divisor == -1:
            return (1 << 31) - 1

        # Determine result sign
        is_positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

        a = abs(dividend)
        b = abs(divisor)
        quotient = 0

        # Quick check for equal values
        if a == b:
            return 1 if is_positive else -1

        while a >= b:
            i = 0
            while (b << i) <= a:  # Find largest shift
                i += 1
            quotient += 1 << (i - 1)
            a -= b << (i - 1)

        return quotient if is_positive else -quotient


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_division(self):
        """Test standard division with positive numbers."""
        self.assertEqual(self.solution.divide(10, 3), 3)

    def test_negative_dividend(self):
        """Test division where the dividend is negative."""
        self.assertEqual(self.solution.divide(-7, 3), -2)

    def test_negative_divisor(self):
        """Test division where the divisor is negative."""
        self.assertEqual(self.solution.divide(7, -3), -2)

    def test_both_negative(self):
        """Test division where both the dividend and divisor are negative."""
        self.assertEqual(self.solution.divide(-10, -3), 3)

    def test_divide_by_one(self):
        """Test division by 1."""
        self.assertEqual(self.solution.divide(100, 1), 100)

    def test_less_than_one(self):
        """Test where the dividend is smaller than the divisor, resulting in 0."""
        self.assertEqual(self.solution.divide(1, 3), 0)

    def test_edge_case_overflow(self):
        """Test for the specific integer overflow scenario."""
        self.assertEqual(self.solution.divide(-2147483648, -1), 2147483647)

    def test_equal_numbers(self):
        """Test where the dividend and divisor are equal."""
        self.assertEqual(self.solution.divide(5, 5), 1)

    def test_zero_dividend(self):
        """Test division where the dividend is zero."""
        self.assertEqual(self.solution.divide(0, 5), 0)

    def test_large_numbers(self):
        """Test a division involving larger numbers."""
        self.assertEqual(self.solution.divide(1000000, 2), 500000)


if __name__ == "__main__":
    unittest.main()
