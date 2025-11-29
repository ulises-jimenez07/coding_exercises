"""
Problem: Minimum Insertions to Balance a Parentheses String
         Every '(' must match with '))', not just ')'

Approach:
- Use a counter to track needed ')' characters (each '(' needs 2 ')')
- When seeing '(': if count is odd, add a ')' to complete the pair, then add 2 for new '('
- When seeing ')': decrement count; if negative, add '(' and adjust count by +2
- At the end, add remaining count to ans (unmatched ')' needed)
- Time complexity: O(n) where n is the length of string
- Space complexity: O(1)
"""

import unittest


class Solution:
    """Solution for LeetCode 1541: Minimum Insertions to Balance a Parentheses String."""

    def minInsertions(self, s: str) -> int:
        """
        Calculate minimum insertions to balance parentheses where each '(' needs '))'.

        In this problem, every opening '(' must be closed by two consecutive ')'.
        """
        ans = 0  # Count of insertions needed
        count = 0  # Count of ')' needed to balance

        for char in s:
            if char == "(":
                # If count is odd, we have a single ')' that needs pairing
                if count % 2:
                    count -= 1  # Use this ')' with previous '('
                    ans += 1  # Add one ')' to complete the pair
                count += 2  # Each '(' needs two ')'
            else:
                count -= 1  # Found a ')', reduce needed count

            # If count becomes negative, we need to add '('
            if count < 0:
                ans += 1  # Add one '('
                count += 2  # That '(' needs two ')'

        # Remaining count means we need more ')' to close
        ans += count

        return ans


class TestMinInsertions(unittest.TestCase):
    """Test cases for Minimum Insertions to Balance solution."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_case_1(self):
        """Test with basic case: '(()))'."""
        s = "(()))"
        expected = 1  # Need to add '(' at the beginning
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_basic_case_2(self):
        """Test with basic case: '())'."""
        s = "())"
        expected = 0  # Already balanced: one '(' with two ')'
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_need_closing_parentheses(self):
        """Test case needing closing parentheses: '))()(('."""
        s = "))()))(("
        expected = 7
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_single_open(self):
        """Test single opening: '('."""
        s = "("
        expected = 2  # Need '))'
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_single_close(self):
        """Test single closing: ')'."""
        s = ")"
        expected = 2  # Need '()' before it
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_two_closes(self):
        """Test two closing: '))'."""
        s = "))"
        expected = 1  # Need '(' before them
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_three_closes(self):
        """Test three closing: ')))'."""
        s = ")))"
        expected = 3  # Need '(' for first two, '(' for third + one more ')'
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_multiple_opens(self):
        """Test multiple opens: '((('."""
        s = "((("
        expected = 6  # Each needs '))', so 3 * 2 = 6
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_alternating_pattern(self):
        """Test alternating pattern: '()()('."""
        s = "()()("
        expected = 4  # First two '()' need one more ')', last '(' needs '))'
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_empty_string(self):
        """Test empty string."""
        s = ""
        expected = 0
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_already_balanced(self):
        """Test already balanced string: '(()))(())'."""
        s = "(()))(())"
        expected = 3
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_complex_case_1(self):
        """Test complex case: '(()))('."""
        s = "(()))("
        expected = 3
        self.assertEqual(self.solution.minInsertions(s), expected)

    def test_complex_case_2(self):
        """Test complex case: ')))))))'."""
        s = "))))))))"
        expected = 4  # 8 ')' need 4 '('
        self.assertEqual(self.solution.minInsertions(s), expected)


if __name__ == "__main__":
    unittest.main()
