"""
Problem: Generate Parentheses - generate all valid combinations of n pairs of parentheses

Approach:
- Use backtracking to build valid parenthesis combinations character by character
- Track count of left and right parentheses used
- Add '(' if we haven't used all n left parentheses
- Add ')' only if it doesn't exceed the count of left parentheses (keeps it valid)
- Time complexity: O(4^n / sqrt(n)) - nth Catalan number
- Space complexity: O(n) for recursion stack depth
"""

import unittest
from typing import List


class Solution:
    """Solution for LeetCode 22: Generate Parentheses."""

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of n pairs of well-formed parentheses.

        Uses backtracking to explore all valid combinations by adding '(' and ')'
        while maintaining validity constraints.
        """
        ans: list[str] = []  # Store all valid combinations

        def _generate_valid(curr: list[str], left_count: int, right_count: int) -> None:
            """
            Recursively generate valid parenthesis combinations.

            curr: Current combination being built
            left_count: Number of '(' used so far
            right_count: Number of ')' used so far
            """
            # Base case: complete combination found
            if len(curr) == (n * 2):
                ans.append("".join(curr))
                return

            # Add '(' if we haven't used all n left parentheses
            if left_count < n:
                curr.append("(")
                _generate_valid(curr, left_count + 1, right_count)
                curr.pop()  # Backtrack

            # Add ')' only if it doesn't make combination invalid
            if right_count < left_count:
                curr.append(")")
                _generate_valid(curr, left_count, right_count + 1)
                curr.pop()  # Backtrack

        _generate_valid([], 0, 0)
        return ans


class TestGenerateParenthesis(unittest.TestCase):
    """Test cases for Generate Parentheses solution."""

    def setUp(self):
        self.solution = Solution()

    def test_n_equals_1(self):
        """Test with n=1 - single pair."""
        n = 1
        expected = ["()"]
        self.assertEqual(sorted(self.solution.generateParenthesis(n)), sorted(expected))

    def test_n_equals_2(self):
        """Test with n=2 - two pairs."""
        n = 2
        expected = ["(())", "()()"]
        self.assertEqual(sorted(self.solution.generateParenthesis(n)), sorted(expected))

    def test_n_equals_3(self):
        """Test with n=3 - three pairs."""
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertEqual(sorted(self.solution.generateParenthesis(n)), sorted(expected))

    def test_n_equals_4(self):
        """Test with n=4 - four pairs, validates Catalan number count."""
        n = 4
        result = self.solution.generateParenthesis(n)
        # 4th Catalan number is 14
        self.assertEqual(len(result), 14)
        # Verify all results are unique
        self.assertEqual(len(result), len(set(result)))
        # Verify all results have correct length
        for combo in result:
            self.assertEqual(len(combo), n * 2)

    def test_all_valid_parentheses(self):
        """Test that all generated combinations are valid."""
        n = 3
        result = self.solution.generateParenthesis(n)
        for combo in result:
            self.assertTrue(self._is_valid_parentheses(combo), f"Invalid combination: {combo}")

    def test_correct_count(self):
        """Test that result count matches Catalan number for various n."""
        # Catalan numbers: C(0)=1, C(1)=1, C(2)=2, C(3)=5, C(4)=14, C(5)=42
        catalan = [1, 1, 2, 5, 14, 42]
        for n in range(1, 6):
            result = self.solution.generateParenthesis(n)
            self.assertEqual(len(result), catalan[n], f"Wrong count for n={n}")

    def test_no_duplicates(self):
        """Test that there are no duplicate combinations."""
        for n in range(1, 5):
            result = self.solution.generateParenthesis(n)
            self.assertEqual(len(result), len(set(result)), f"Duplicates found for n={n}")

    def test_all_have_correct_length(self):
        """Test that all combinations have exactly 2n characters."""
        for n in range(1, 5):
            result = self.solution.generateParenthesis(n)
            for combo in result:
                self.assertEqual(len(combo), n * 2, f"Wrong length for combo: {combo}")

    def test_equal_left_right_count(self):
        """Test that all combinations have equal number of '(' and ')'."""
        n = 3
        result = self.solution.generateParenthesis(n)
        for combo in result:
            self.assertEqual(combo.count("("), n)
            self.assertEqual(combo.count(")"), n)

    def _is_valid_parentheses(self, s: str) -> bool:
        """Helper method to validate a parenthesis string."""
        balance = 0
        for char in s:
            if char == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0


if __name__ == "__main__":
    unittest.main()
