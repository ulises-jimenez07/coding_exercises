"""
Problem: Longest Valid Parentheses - find the length of the longest valid (well-formed) parentheses substring

Approach:
- Use a stack to keep track of indices
- Initialize stack with -1 to handle edge cases
- Time complexity: O(n) where n is string length
- Space complexity: O(n) for the stack
"""

import unittest


class Solution:
    """
    Solution class for Longest Valid Parentheses problem.
    """

    def longestValidParentheses(self, s: str) -> int:
        """
        Finds the length of the longest valid (well-formed) parentheses substring.
        """
        ans = 0
        stack = []
        # Push -1 to handle the case where the valid substring starts at index 0
        stack.append(-1)

        for i, ch in enumerate(s):
            if ch == "(":
                # Store index of opening bracket
                stack.append(i)
            else:
                # Closing bracket: try to match
                stack.pop()
                if not stack:
                    # Stack empty means unmatched closing bracket
                    # Push current index as new base for valid substrings
                    stack.append(i)
                else:
                    # Valid match found, calculate length
                    ans = max(ans, i - stack[-1])
        return ans


class TestLongestValidParentheses(unittest.TestCase):
    """
    Unit tests for the Longest Valid Parentheses solution.
    """

    def setUp(self):
        self.solution = Solution()

    def test_simple_valid_case(self):
        """Test with a simple valid string '(()'."""
        self.assertEqual(self.solution.longestValidParentheses("(()"), 2)

    def test_longer_valid_case(self):
        """Test with a longer valid string ')()())'."""
        self.assertEqual(self.solution.longestValidParentheses(")()())"), 4)

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(self.solution.longestValidParentheses(""), 0)

    def test_no_valid_parentheses(self):
        """Test with no valid parentheses '('."""
        self.assertEqual(self.solution.longestValidParentheses("("), 0)

    def test_all_valid(self):
        """Test with all valid parentheses '()()'."""
        self.assertEqual(self.solution.longestValidParentheses("()()"), 4)

    def test_nested_valid(self):
        """Test with nested valid parentheses '(()())'."""
        self.assertEqual(self.solution.longestValidParentheses("(()())"), 6)


if __name__ == "__main__":
    unittest.main()
