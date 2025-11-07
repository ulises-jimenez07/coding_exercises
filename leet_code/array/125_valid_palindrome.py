"""
Problem: Determine if a string is a palindrome, ignoring non-alphanumeric characters and case

Approach:
- Use two pointers from both ends of string
- Skip non-alphanumeric characters and compare case-insensitively
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Determines if string is a palindrome, ignoring case and non-alphanumeric characters."""
        left = 0
        right = len(s) - 1

        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()

            if not left_char.isalnum():
                left += 1
            elif not right_char.isalnum():
                right -= 1
            elif left_char != right_char:
                return False
            else:
                left += 1
                right -= 1

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_palindromes(self):
        """Valid palindromes with various characters."""
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(self.solution.isPalindrome("racecar"))
        self.assertTrue(self.solution.isPalindrome("Madam, I'm Adam"))
        self.assertTrue(self.solution.isPalindrome("12321"))
        self.assertTrue(self.solution.isPalindrome("ab@a"))
        self.assertTrue(self.solution.isPalindrome(" "))
        self.assertTrue(self.solution.isPalindrome("a"))
        self.assertTrue(self.solution.isPalindrome(""))
        self.assertTrue(self.solution.isPalindrome("0P0"))

    def test_invalid_palindromes(self):
        """Strings that are not palindromes."""
        self.assertFalse(self.solution.isPalindrome("hello"))
        self.assertFalse(self.solution.isPalindrome("race a car"))
        self.assertFalse(self.solution.isPalindrome("0P"))
        self.assertFalse(self.solution.isPalindrome("abcde"))

    def test_case_and_non_alphanumeric_handling(self):
        """Case-insensitivity and non-alphanumeric character handling."""
        self.assertTrue(self.solution.isPalindrome("AbA"))
        self.assertTrue(self.solution.isPalindrome("A B A"))
        self.assertTrue(self.solution.isPalindrome("A-B-A"))
        self.assertTrue(self.solution.isPalindrome("A-B@A"))
        self.assertFalse(self.solution.isPalindrome("ab@c"))


if __name__ == "__main__":
    unittest.main()
