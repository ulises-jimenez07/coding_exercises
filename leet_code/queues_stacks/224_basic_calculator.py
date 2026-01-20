"""
Problem: Basic Calculator - evaluate a basic mathematical expression string

Approach:
- Use a stack to handle parentheses and manage local vs global evaluation states
- Maintain a running result, current number, and current sign
- Time complexity: O(n) where n is the length of the string
- Space complexity: O(n) for the stack in case of nested parentheses
"""

import unittest
from typing import List


class Solution:
    """
    Class to solve the Basic Calculator problem.
    """

    def calculate(self, s: str) -> int:
        """
        Evaluates a mathematical expression containing +, -, (, ), and spaces.
        """
        stack: List[int] = []
        curr_num, sign, res = 0, 1, 0

        for _, char in enumerate(s):
            if char.isdigit():
                # Form the multi-digit number
                curr_num = curr_num * 10 + int(char)
            elif char in ("+", "-"):
                # Evaluate the previous part and update sign
                res += sign * curr_num
                sign = -1 if char == "-" else 1
                curr_num = 0
            elif char == "(":
                # Push the current result and sign to stack to be resolved later
                stack.append(res)
                stack.append(sign)
                # Reset result and sign for the new local scope
                res, sign = 0, 1
            elif char == ")":
                # Finish the local evaluation and apply the sign/previous result
                res += sign * curr_num
                res *= stack.pop()  # Multiplier (sign before bracket)
                res += stack.pop()  # Previous result before bracket
                curr_num = 0

        # Add the final number after the loop ends
        return res + sign * curr_num


class TestBasicCalculator(unittest.TestCase):
    """
    Unit tests for the Basic Calculator solution.
    """

    def setUp(self):
        """Initialize the solution instance before each test."""
        self.solution = Solution()

    def test_simple_addition(self):
        """Test simple addition '1 + 1'."""
        self.assertEqual(self.solution.calculate("1 + 1"), 2)

    def test_spaces_and_subtraction(self):
        """Test expression with spaces and subtraction ' 2-1 + 2 '."""
        self.assertEqual(self.solution.calculate(" 2-1 + 2 "), 3)

    def test_nested_parentheses(self):
        """Test a complex expression with nested parentheses."""
        self.assertEqual(self.solution.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

    def test_single_number(self):
        """Test an expression that is just a single number."""
        self.assertEqual(self.solution.calculate("123"), 123)

    def test_parentheses_single_number(self):
        """Test a single number wrapped in parentheses."""
        self.assertEqual(self.solution.calculate("(1)"), 1)

    def test_large_number(self):
        """Test with a large integer string."""
        self.assertEqual(self.solution.calculate("2147483647"), 2147483647)


if __name__ == "__main__":
    unittest.main()
