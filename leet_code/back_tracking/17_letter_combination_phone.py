"""
Problem: Generate all letter combinations from phone number digits

Approach:
- Map each digit to its corresponding letters (like on a phone keypad)
- Use backtracking to explore all combinations by choosing one letter per digit
- Time complexity: O(4^n) where n is number of digits
- Space complexity: O(n) for recursion stack
"""


class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        # Phone keypad mapping
        digits_to_string = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []
        self.back_tracking(digits, digits_to_string, "", ans, 0)
        return ans

    def back_tracking(self, digits, digits_to_string, curr, ans, digit_index):
        # Base case: built complete combination
        if len(curr) == len(digits):
            ans.append(curr)
            return

        current_digit = digits[digit_index]
        current_string = digits_to_string[current_digit]

        # Try each letter for current digit
        for char in current_string:
            self.back_tracking(digits, digits_to_string, curr + char, ans, digit_index + 1)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.maxDiff = None

    def test_two_digits(self):
        """Test with two digits '23'."""
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertCountEqual(self.solution.letterCombinations(digits), expected)

    def test_empty_digits(self):
        """Test with an empty string of digits."""
        digits = ""
        expected = []
        self.assertEqual(self.solution.letterCombinations(digits), expected)

    def test_single_digit(self):
        """Test with a single digit '2'."""
        digits = "2"
        expected = ["a", "b", "c"]
        self.assertCountEqual(self.solution.letterCombinations(digits), expected)

    def test_two_other_digits(self):
        """Test with two other digits '79'."""
        digits = "79"
        expected = ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]
        actual = self.solution.letterCombinations(digits)
        self.assertCountEqual(sorted(actual), sorted(expected))


if __name__ == "__main__":
    unittest.main()
