from typing import List
import unittest


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates a Reverse Polish Notation (RPN) expression.

        Args:
            tokens: A list of strings representing the RPN expression.
                    Operands are integers, and operators are '+', '-', '*', '/'.

        Returns:
            The integer result of evaluating the RPN expression.
        """
        stack = []
        operators = {"*", "+", "-", "/"}

        def evaluate(operand_1: int, operand_2: int, operation: str) -> int:
            """
            Performs the specified arithmetic operation on two operands.

            Args:
                operand_1: The first operand (comes later in the RPN expression).
                operand_2: The second operand (comes earlier in the RPN expression).
                operation: The arithmetic operation to perform ('+', '-', '*', '/').

            Returns:
                The result of the operation.
            """
            match operation:
                case "+":
                    return operand_1 + operand_2
                case "-":
                    return operand_1 - operand_2
                case "*":
                    return operand_1 * operand_2
                case "/":
                    # Integer division as per the problem statement for LeetCode
                    return int(operand_1 / operand_2)

        for token in tokens:
            if token in operators:
                # Pop the last two operands from the stack
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                # Evaluate the operation and push the result back onto the stack
                result = evaluate(operand_1, operand_2, token)
                stack.append(result)
            else:
                # If the token is not an operator, it's an operand, so push it onto the stack
                stack.append(int(token))

        # The final result will be the only element left on the stack
        return stack[-1]


class TestEvalRPN(unittest.TestCase):
    def test_addition(self):
        solution = Solution()
        self.assertEqual(solution.evalRPN(["2", "1", "+"]), 3)

    def test_subtraction(self):
        solution = Solution()
        self.assertEqual(solution.evalRPN(["4", "2", "-"]), 2)

    def test_multiplication(self):
        solution = Solution()
        self.assertEqual(solution.evalRPN(["3", "4", "*"]), 12)

    def test_division(self):
        solution = Solution()
        self.assertEqual(solution.evalRPN(["10", "3", "/"]), 3)

    def test_complex_expression(self):
        solution = Solution()
        self.assertEqual(solution.evalRPN(["4", "13", "5", "/", "+"]), 6)

    def test_negative_numbers(self):
        solution = Solution()
        self.assertEqual(solution.evalRPN(["-1", "-2", "*"]), 2)

    def test_division_with_negative_result(self):
        solution = Solution()
        self.assertEqual(solution.evalRPN(["-6", "3", "/"]), -2)

    def test_longer_expression(self):
        solution = Solution()
        self.assertEqual(
            solution.evalRPN(
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            ),
            22,
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
