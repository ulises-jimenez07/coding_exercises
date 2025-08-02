import unittest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, this method determines if it is a palindrome.

        A string is considered a palindrome if, after converting all uppercase letters to
        lowercase and removing all non-alphanumeric characters, it reads the same forward
        and backward. Alphanumeric characters include letters and numbers.

        This implementation uses a two-pointer approach for efficient checking.
        A 'left' pointer starts at the beginning of the string and a 'right' pointer
        starts at the end. The pointers move inward, skipping over any
        non-alphanumeric characters. The alphanumeric characters are compared
        in a case-insensitive manner. If a mismatch is found, the string is not a
        palindrome. If the pointers meet or cross without any mismatches, it is a
        palindrome.

        Args:
            s: The input string to be checked.

        Returns:
            True if the string is a palindrome, False otherwise.
        """
        # Initialize two pointers, one at the beginning and one at the end of the string.
        left = 0
        right = len(s) - 1

        # Continue the loop as long as the left pointer is before the right pointer.
        while left < right:
            # Get the characters at the current pointer positions and convert to lowercase.
            left_char = s[left].lower()
            right_char = s[right].lower()

            # If the left character is not alphanumeric, move the left pointer to the right.
            if not left_char.isalnum():
                left += 1
            # If the right character is not alphanumeric, move the right pointer to the left.
            elif not right_char.isalnum():
                right -= 1
            # If both characters are alphanumeric and they don't match, it's not a palindrome.
            elif left_char != right_char:
                return False
            # If both characters are alphanumeric and they match, move both pointers inward.
            else:
                left += 1
                right -= 1
        
        # If the loop completes without finding any mismatches, the string is a palindrome.
        return True

class TestSolution(unittest.TestCase):
    """
    Unit tests for the isPalindrome method in the Solution class.
    """

    def test_valid_palindromes(self):
        """
        Test cases for various valid palindromes, including phrases, single words,
        and strings with different characters and lengths.
        """
        self.assertTrue(Solution().isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(Solution().isPalindrome("racecar"))
        self.assertTrue(Solution().isPalindrome("Madam, I'm Adam"))
        self.assertTrue(Solution().isPalindrome("12321"))
        self.assertTrue(Solution().isPalindrome("ab@a"))
        self.assertTrue(Solution().isPalindrome(" "))
        self.assertTrue(Solution().isPalindrome("a"))
        self.assertTrue(Solution().isPalindrome(""))
        self.assertTrue(Solution().isPalindrome("0P0")) # Example with number and letter

    def test_invalid_palindromes(self):
        """
        Test cases for strings that are not palindromes.
        """
        self.assertFalse(Solution().isPalindrome("hello"))
        self.assertFalse(Solution().isPalindrome("race a car"))
        self.assertFalse(Solution().isPalindrome("0P")) # Example with non-matching alphanumeric chars
        self.assertFalse(Solution().isPalindrome("abcde"))

    def test_case_and_non_alphanumeric_handling(self):
        """
        Test cases specifically to verify that the method correctly handles
        case-insensitivity and ignores non-alphanumeric characters.
        """
        self.assertTrue(Solution().isPalindrome("AbA"))
        self.assertTrue(Solution().isPalindrome("A B A"))
        self.assertTrue(Solution().isPalindrome("A-B-A"))
        self.assertTrue(Solution().isPalindrome("A-B@A"))
        self.assertFalse(Solution().isPalindrome("ab@c"))

if __name__ == '__main__':
    unittest.main()
