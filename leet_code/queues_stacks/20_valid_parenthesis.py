"""
Problem: Valid Parentheses - check if string has properly matched brackets

Approach:
- Use a stack to track opening brackets
- Match closing brackets with stack top
- Time complexity: O(n) where n is string length
- Space complexity: O(n) for the stack
"""

import unittest


class Solution:
    def isValid(self, s):
        """
        Determines if a string containing parentheses is valid.
        A valid string has properly nested and matching parentheses.
        """
        brackets = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for char in s:
            if char in brackets:
                stack.append(char)
            elif not stack:
                return False
            else:
                top = stack.pop()
                if brackets[top] != char:
                    return False

        return not stack


class TestIsValid(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_valid_case(self):
        """Test with a simple valid string '()'."""
        self.assertTrue(self.solution.isValid("()"))

    def test_multiple_valid_bracket_types(self):
        """Test with multiple valid bracket types '()[]{}'."""
        self.assertTrue(self.solution.isValid("()[]{}"))

    def test_mismatched_brackets(self):
        """Test with mismatched brackets '(]'."""
        self.assertFalse(self.solution.isValid("(]"))

    def test_incorrect_nesting(self):
        """Test with incorrect nesting '([)]'."""
        self.assertFalse(self.solution.isValid("([)]"))

    def test_correct_nesting(self):
        """Test with correct nesting '{[]}'."""
        self.assertTrue(self.solution.isValid("{[]}"))

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertTrue(self.solution.isValid(""))

    def test_unclosed_opening_bracket(self):
        """Test with an unclosed opening bracket '('."""
        self.assertFalse(self.solution.isValid("("))

    def test_unmatched_closing_bracket(self):
        """Test with an unmatched closing bracket '}'."""
        self.assertFalse(self.solution.isValid("}"))

    def test_multiple_unclosed_opening_brackets(self):
        """Test with multiple unclosed opening brackets '{{{{'."""
        self.assertFalse(self.solution.isValid("{{{{"))

    def test_multiple_unmatched_closing_brackets(self):
        """Test with multiple unmatched closing brackets '}}'."""
        self.assertFalse(self.solution.isValid("}}"))


if __name__ == "__main__":
    unittest.main()
