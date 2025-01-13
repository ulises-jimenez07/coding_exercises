import unittest


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converts a string to a 32-bit integer.

        The function follows these rules:

        1. Read in and ignore any leading whitespace.
        2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines the sign of the final result.
        3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
        4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary.
        5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
        6. Return the integer as the final result.

        Args:
            s: The input string.

        Returns:
            The converted 32-bit integer.
        """
        sign = 1  # Initialize sign as positive
        result = 0  # Initialize result
        index = 0  # Initialize index
        n = len(s)  # Get the length of the string

        INT_MAX = pow(2, 31) - 1  # Maximum 32-bit integer
        INT_MIN = -pow(2, 31)  # Minimum 32-bit integer

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
            if (result > INT_MAX // 10) or (
                result == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                return INT_MAX if sign == 1 else INT_MIN

            result = 10 * result + digit
            index += 1

        return sign * result  # Return the result with the correct sign


class TestMyAtoi(unittest.TestCase):
    def test_positive_numbers(self):
        solution = Solution()
        self.assertEqual(solution.myAtoi("42"), 42)
        self.assertEqual(solution.myAtoi("   42"), 42)
        self.assertEqual(solution.myAtoi("0042"), 42)

    def test_negative_numbers(self):
        solution = Solution()
        self.assertEqual(solution.myAtoi("-42"), -42)
        self.assertEqual(solution.myAtoi("  -42  "), -42)

    def test_leading_zeros(self):
        solution = Solution()
        self.assertEqual(solution.myAtoi("0000042"), 42)

    def test_trailing_non_digits(self):
        solution = Solution()
        self.assertEqual(solution.myAtoi("4193 with words"), 4193)

    def test_leading_non_digits(self):
        solution = Solution()
        self.assertEqual(solution.myAtoi("words and 987"), 0)

    def test_empty_string(self):
        solution = Solution()
        self.assertEqual(solution.myAtoi(""), 0)

    def test_whitespace_string(self):
        solution = Solution()
        self.assertEqual(solution.myAtoi("   "), 0)

    def test_overflow(self):
        solution = Solution()
        self.assertEqual(
            solution.myAtoi("2147483648"), 2147483647
        )  # Clamped to INT_MAX
        self.assertEqual(
            solution.myAtoi("-2147483649"), -2147483648
        )  # Clamped to INT_MIN

    def test_plus_sign(self):
        solution = Solution()
        self.assertEqual(solution.myAtoi("+42"), 42)


if __name__ == "__main__":
    unittest.main()
