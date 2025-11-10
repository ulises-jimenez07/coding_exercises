"""
Problem: Find the k-beauty of a number (count of k-length substrings that divide the number)

Approach:
- Use fixed-size sliding window of size k on string representation of number
- For each window, convert substring to integer and check if it divides num
- Check for zero divisor to avoid division error
- Time complexity: O(n) - single pass through digits, where n is length of num
- Space complexity: O(n) - string representation of number
"""

import unittest


class Solution:
    """Solution for LeetCode problem 2269: Find the K-Beauty of a Number."""

    def divisorSubstrings(self, num: int, k: int) -> int:
        """Counts k-length substrings of num that divide num evenly using sliding window."""
        k_beauty = 0
        left = 0
        s_num = str(num)

        # Slide window of size k through the number's digits
        for right in range(k - 1, len(s_num)):
            int_sub = int(s_num[left : right + 1])

            # Check if substring is non-zero and divides num evenly
            if int_sub > 0 and num % int_sub == 0:
                k_beauty += 1
            left += 1

        return k_beauty


class TestSolution(unittest.TestCase):
    """Test cases for Solution class."""

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """Standard case with multiple divisors."""
        num = 240
        k = 2
        expected = 2  # "24" and "40" divide 240
        result = self.solution.divisorSubstrings(num, k)
        self.assertEqual(result, expected)

    def test_example2(self):
        """Case with no valid divisors."""
        num = 430043
        k = 2
        expected = 2  # "43" and "30" divide 430043
        result = self.solution.divisorSubstrings(num, k)
        self.assertEqual(result, expected)

    def test_single_digit(self):
        """Single digit number."""
        num = 5
        k = 1
        expected = 1  # "5" divides 5
        result = self.solution.divisorSubstrings(num, k)
        self.assertEqual(result, expected)

    def test_with_zeros(self):
        """Number containing zeros (should not divide)."""
        num = 1000
        k = 2
        expected = 1  # Only "10" divides 1000, "00" is skipped
        result = self.solution.divisorSubstrings(num, k)
        self.assertEqual(result, expected)

    def test_all_digits_divide(self):
        """Multiple single digit divisors."""
        num = 121
        k = 1
        expected = 2  # "1" and "1" divide 121, but "2" does not
        result = self.solution.divisorSubstrings(num, k)
        self.assertEqual(result, expected)

    def test_larger_k(self):
        """Window size equal to number length."""
        num = 100
        k = 3
        expected = 1  # "100" divides 100
        result = self.solution.divisorSubstrings(num, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
