"""
Problem: Check if an integer is a palindrome

Approach:
- Two solutions: convert to string and compare, or reverse half without conversion
- String method uses two pointers, math method reverses second half
- Time complexity: O(log n) - number of digits
- Space complexity: O(1) for math method, O(log n) for string method
"""

import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Checks if an integer is a palindrome by converting to string."""
        str_int = str(x)
        left = 0
        right = len(str_int) - 1

        while left < right:
            if str_int[left] != str_int[right]:
                return False
            left += 1
            right -= 1

        return True

    def isPalindrome_no_convert(self, x: int) -> bool:
        """Checks if an integer is a palindrome without string conversion."""
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revert_num = 0

        while x > revert_num:
            revert_num = revert_num * 10 + x % 10
            x //= 10

        return x == revert_num or x == revert_num // 10


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_palindrome(self):
        """Positive palindrome."""
        self.assertTrue(self.solution.isPalindrome(121))
        self.assertTrue(self.solution.isPalindrome_no_convert(121))

    def test_negative_number(self):
        """Negative number."""
        self.assertFalse(self.solution.isPalindrome(-121))
        self.assertFalse(self.solution.isPalindrome_no_convert(-121))

    def test_non_palindrome(self):
        """Non-palindrome."""
        self.assertFalse(self.solution.isPalindrome(123))
        self.assertFalse(self.solution.isPalindrome_no_convert(123))

    def test_single_digit(self):
        """Single digit."""
        self.assertTrue(self.solution.isPalindrome(7))
        self.assertTrue(self.solution.isPalindrome_no_convert(7))

    def test_zero(self):
        """Zero."""
        self.assertTrue(self.solution.isPalindrome(0))
        self.assertTrue(self.solution.isPalindrome_no_convert(0))

    def test_number_ending_in_zero(self):
        """Number ending in zero."""
        self.assertFalse(self.solution.isPalindrome(10))
        self.assertFalse(self.solution.isPalindrome_no_convert(10))

    def test_large_palindrome(self):
        """Large palindrome."""
        self.assertTrue(self.solution.isPalindrome(123454321))
        self.assertTrue(self.solution.isPalindrome_no_convert(123454321))

    def test_large_non_palindrome(self):
        """Large non-palindrome."""
        self.assertFalse(self.solution.isPalindrome(123456789))
        self.assertFalse(self.solution.isPalindrome_no_convert(123456789))

    def test_odd_length_palindrome(self):
        """Odd length palindrome."""
        self.assertTrue(self.solution.isPalindrome(12321))
        self.assertTrue(self.solution.isPalindrome_no_convert(12321))


if __name__ == "__main__":
    unittest.main()
