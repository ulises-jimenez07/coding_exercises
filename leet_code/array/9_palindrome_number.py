import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Checks if an integer is a palindrome by converting it to a string.

        A palindrome is a number that reads the same backward as forward.

        Args:
            x: The integer to check.

        Returns:
            True if x is a palindrome, False otherwise.
        """
        str_int = str(x)  # Convert the integer to a string
        left = 0  # Initialize the left pointer to the start of the string
        right = (
            len(str_int) - 1
        )  # Initialize the right pointer to the end of the string

        while left < right:  # Continue until the pointers meet in the middle
            if str_int[left] != str_int[right]:  # If characters don't match
                return False  # Not a palindrome
            left += 1  # Move the left pointer to the right
            right -= 1  # Move the right pointer to the left

        return True  # If the loop completes, it's a palindrome

    def isPalindrome_no_convert(self, x: int) -> bool:
        """
        Checks if an integer is a palindrome without converting it to a string.

        This method reverses the second half of the number and compares it with the first half.

        Args:
            x: The integer to check.

        Returns:
            True if x is a palindrome, False otherwise.
        """
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revert_num = 0  # Initialize the reversed number

        while (
            x > revert_num
        ):  # Continue until the reversed number is greater than or equal to the original number
            revert_num = revert_num * 10 + x % 10  # Build the reversed number
            x //= 10  # Reduce the original number

        # If the original number and reversed number are equal, or if the original number is equal to the reversed number divided by 10 (for odd-length palindromes), it's a palindrome
        return x == revert_num or x == revert_num // 10


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(121))
        self.assertTrue(self.solution.isPalindrome_no_convert(121))

    def test_negative_number(self):
        self.assertFalse(self.solution.isPalindrome(-121))
        self.assertFalse(self.solution.isPalindrome_no_convert(-121))

    def test_non_palindrome(self):
        self.assertFalse(self.solution.isPalindrome(123))
        self.assertFalse(self.solution.isPalindrome_no_convert(123))

    def test_single_digit(self):
        self.assertTrue(self.solution.isPalindrome(7))
        self.assertTrue(self.solution.isPalindrome_no_convert(7))

    def test_zero(self):
        self.assertTrue(self.solution.isPalindrome(0))
        self.assertTrue(self.solution.isPalindrome_no_convert(0))

    def test_number_ending_in_zero(self):
        self.assertFalse(self.solution.isPalindrome(10))
        self.assertFalse(self.solution.isPalindrome_no_convert(10))

    def test_large_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(123454321))
        self.assertTrue(self.solution.isPalindrome_no_convert(123454321))

    def test_large_non_palindrome(self):
        self.assertFalse(self.solution.isPalindrome(123456789))
        self.assertFalse(self.solution.isPalindrome_no_convert(123456789))

    def test_odd_length_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(12321))
        self.assertTrue(self.solution.isPalindrome_no_convert(12321))


if __name__ == "__main__":
    unittest.main()
