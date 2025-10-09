import unittest

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divides two integers `dividend` and `divisor` without using standard multiplication, division, or modulo operators.

        This method uses a bit manipulation approach to repeatedly subtract multiples of the divisor from the dividend,
        which is significantly more efficient than a simple iterative subtraction. It also handles edge cases, such as
        integer overflow for 32-bit signed integers.
        """
        # Handles the specific edge case where `dividend` is the minimum 32-bit integer (-2^31) and `divisor` is -1.
        # The result of this operation (2^31) would overflow a 32-bit signed integer, so the method returns the
        # maximum possible value for a 32-bit signed integer (2^31 - 1).
        if dividend == (-1 << 31) and divisor == -1:
            return ((1 << 31) -1)
        
        # Determines the sign of the final result. The result is positive if `dividend` and `divisor` have the same sign,
        # and negative otherwise.
        is_positive = ((dividend > 0 and divisor >0) or (dividend < 0 and divisor < 0))

        # Converts both the `dividend` and `divisor` to their absolute values to simplify the division logic.
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0
        
        # If the absolute values of the dividend and divisor are the same, the quotient is 1. The sign is applied based on `is_positive`.
        if a == b:
            return 1 if is_positive else -1

        # The core division logic: a loop that continues as long as the dividend's absolute value is greater than or equal to the divisor's.
        while a >= b:
            i = 0
            # Inner loop to find the largest power of 2 (2^i) such that `divisor` * 2^i (`b << i`) is less than or equal to `dividend`.
            while ((b << i) <= a):
                i += 1
            # Adds the corresponding power of 2 (2^(i-1)) to the `quotient`. This is a crucial step for the bit manipulation approach's efficiency.
            quotient += (1 << (i -1))
            # Subtracts the largest found multiple of the divisor (`b << (i - 1)`) from the dividend.
            a -= (b << (i - 1))

        # Returns the calculated quotient, applying the correct sign determined earlier.
        return quotient if is_positive else -quotient

# The `TestSolution` class contains unit tests for the `Solution.divide` method to ensure its correctness.
class TestSolution(unittest.TestCase):
    
    # Test case for a standard division with positive numbers.
    def test_positive_division(self):
        self.assertEqual(Solution().divide(10, 3), 3)

    # Test case for division where the dividend is negative.
    def test_negative_dividend(self):
        self.assertEqual(Solution().divide(-7, 3), -2)

    # Test case for division where the divisor is negative.
    def test_negative_divisor(self):
        self.assertEqual(Solution().divide(7, -3), -2)

    # Test case for division where both the dividend and divisor are negative.
    def test_both_negative(self):
        self.assertEqual(Solution().divide(-10, -3), 3)

    # Test case for division by 1.
    def test_divide_by_one(self):
        self.assertEqual(Solution().divide(100, 1), 100)

    # Test case where the dividend is smaller than the divisor, resulting in 0.
    def test_less_than_one(self):
        self.assertEqual(Solution().divide(1, 3), 0)

    # Test case for the specific integer overflow scenario.
    def test_edge_case_overflow(self):
        self.assertEqual(Solution().divide(-2147483648, -1), 2147483647)

    # Test case where the dividend and divisor are equal.
    def test_equal_numbers(self):
        self.assertEqual(Solution().divide(5, 5), 1)

    # Test case for division where the dividend is zero.
    def test_zero_dividend(self):
        self.assertEqual(Solution().divide(0, 5), 0)

    # Test case for a division involving larger numbers.
    def test_large_numbers(self):
        self.assertEqual(Solution().divide(1000000, 2), 500000)

# Entry point for running the unit tests when the script is executed.
if __name__ == '__main__':
    unittest.main()