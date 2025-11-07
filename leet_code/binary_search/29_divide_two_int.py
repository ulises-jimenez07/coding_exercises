"""
Problem: Divide two integers without using multiplication, division, or mod operator

Approach:
- Use exponential search with doubling to find largest multiples
- Work with negative numbers to avoid overflow issues
- Time complexity: O(log^2 n)
- Space complexity: O(log n)
"""

import unittest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Handle overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Convert to negative to avoid overflow
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        # Build doubles and powers of divisor
        doubles = []
        powers_of_two = []

        power_of_two = 1
        while divisor >= dividend:
            doubles.append(divisor)
            powers_of_two.append(power_of_two)
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor
            power_of_two += power_of_two

        # Construct quotient from largest to smallest multiples
        quotient = 0
        for i in reversed(range(len(doubles))):
            if doubles[i] >= dividend:
                quotient += powers_of_two[i]
                dividend -= doubles[i]

        return quotient if negatives != 1 else -quotient


class TestDivide(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_positive_numbers(self):
        self.assertEqual(self.sol.divide(10, 3), 3)
        self.assertEqual(self.sol.divide(7, 2), 3)

    def test_negative_numbers(self):
        self.assertEqual(self.sol.divide(-10, 3), -3)
        self.assertEqual(self.sol.divide(10, -3), -3)
        self.assertEqual(self.sol.divide(-7, -2), 3)

    def test_edge_cases(self):
        self.assertEqual(self.sol.divide(1, 1), 1)
        self.assertEqual(self.sol.divide(0, 1), 0)
        self.assertEqual(self.sol.divide(2147483647, 1), 2147483647)
        self.assertEqual(self.sol.divide(-2147483648, 1), -2147483648)


if __name__ == "__main__":
    unittest.main()
