import unittest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divides two integers without using multiplication, division, and mod operator.

        Args:
            dividend: The dividend.
            divisor: The divisor.

        Returns:
            The quotient. Returns 2**31 - 1 if the quotient is greater than 2**31 - 1,
            and -2**31 if the quotient is less than -2**31.

        """
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: Overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Count the number of negative signs
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend  # Convert to negative for easier handling of overflow
        if divisor > 0:
            negatives -= 1
            divisor = -divisor  # Convert to negative

        # Build arrays to store doubles of divisor and corresponding powers of two
        doubles = []
        powers_of_two = []

        power_of_two = 1
        while divisor >= dividend:
            doubles.append(divisor)
            powers_of_two.append(power_of_two)
            # Prevent potential overflow
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor  # Double the divisor
            power_of_two += power_of_two  # Double the power of two

        # Calculate the quotient by iterating through doubles in reverse
        quotient = 0
        for i in reversed(range(len(doubles))):
            if doubles[i] >= dividend:
                quotient += powers_of_two[i]
                dividend -= doubles[i]

        # Adjust sign based on number of negative signs
        return quotient if negatives != 1 else -quotient


class TestDivide(unittest.TestCase):
    def test_positive_numbers(self):
        sol = Solution()
        self.assertEqual(sol.divide(10, 3), 3)
        self.assertEqual(sol.divide(7, 2), 3)

    def test_negative_numbers(self):
        sol = Solution()
        self.assertEqual(sol.divide(-10, 3), -3)
        self.assertEqual(sol.divide(10, -3), -3)
        self.assertEqual(sol.divide(-7, -2), 3)

    def test_edge_cases(self):
        sol = Solution()
        self.assertEqual(sol.divide(1, 1), 1)
        self.assertEqual(sol.divide(0, 1), 0)
        self.assertEqual(sol.divide(2147483647, 1), 2147483647)
        self.assertEqual(sol.divide(-2147483648, 1), -2147483648)


if __name__ == "__main__":
    unittest.main()
