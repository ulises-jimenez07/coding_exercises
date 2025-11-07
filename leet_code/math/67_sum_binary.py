"""
Problem: Add two binary strings and return their sum as a binary string

Approach:
- Process strings from right to left, similar to manual addition
- Track carry bit and build result string from right to left
- Time complexity: O(max(len(a), len(b)))
- Space complexity: O(max(len(a), len(b)))
"""

import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = ""

        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            res = str(carry % 2) + res  # Prepend current bit
            carry = carry // 2  # Update carry

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Test with basic example a='11', b='1'."""
        a = "11"
        b = "1"
        expected = "100"
        self.assertEqual(self.solution.addBinary(a, b), expected)

    def test_longer_strings(self):
        """Test with longer strings a='1010', b='1011'."""
        a = "1010"
        b = "1011"
        expected = "10101"
        self.assertEqual(self.solution.addBinary(a, b), expected)

    def test_strings_of_different_lengths(self):
        """Test with strings of different lengths a='111', b='1'."""
        a = "111"
        b = "1"
        expected = "1000"
        self.assertEqual(self.solution.addBinary(a, b), expected)

    def test_one_string_is_empty(self):
        """Test when one string is empty a='11', b=''."""
        a = "11"
        b = ""
        expected = "11"
        self.assertEqual(self.solution.addBinary(a, b), expected)

    def test_both_strings_are_empty(self):
        """Test when both strings are empty a='', b=''."""
        a = ""
        b = ""
        expected = ""
        self.assertEqual(self.solution.addBinary(a, b), expected)


if __name__ == "__main__":
    unittest.main()
