"""
Problem: Evaluate Reverse Polish Notation (RPN) arithmetic expression

Approach:
- Use a stack to process operands and operators
- Pop two operands when encountering an operator
- Time complexity: O(n) where n is number of tokens
- Space complexity: O(n) for the stack
"""

import unittest
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates a Reverse Polish Notation (RPN) expression.
        Operands are integers, and operators are '+', '-', '*', '/'.
        """
        stack: list[int] = []
        operators = {"*", "+", "-", "/"}

        def evaluate(operand_1: int, operand_2: int, operation: str) -> int:
            """
            Performs the specified arithmetic operation on two operands.
            """
            match operation:
                case "+":
                    return operand_1 + operand_2
                case "-":
                    return operand_1 - operand_2
                case "*":
                    return operand_1 * operand_2
                case "/":
                    return int(operand_1 / operand_2)
                case _:
                    raise ValueError(f"Unknown operator: {operation}")

        for token in tokens:
            if token in operators:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                result = evaluate(operand_1, operand_2, token)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]


class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_addition(self):
        """Test basic addition."""
        self.assertEqual(self.solution.evalRPN(["2", "1", "+"]), 3)

    def test_subtraction(self):
        """Test basic subtraction."""
        self.assertEqual(self.solution.evalRPN(["4", "2", "-"]), 2)

    def test_multiplication(self):
        """Test basic multiplication."""
        self.assertEqual(self.solution.evalRPN(["3", "4", "*"]), 12)

    def test_division(self):
        """Test basic division."""
        self.assertEqual(self.solution.evalRPN(["10", "3", "/"]), 3)

    def test_complex_expression(self):
        """Test a complex RPN expression."""
        self.assertEqual(self.solution.evalRPN(["4", "13", "5", "/", "+"]), 6)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(self.solution.evalRPN(["-1", "-2", "*"]), 2)

    def test_division_with_negative_result(self):
        """Test division resulting in a negative number."""
        self.assertEqual(self.solution.evalRPN(["-6", "3", "/"]), -2)

    def test_longer_expression(self):
        """Test a longer RPN expression."""
        self.assertEqual(
            self.solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
            22,
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
