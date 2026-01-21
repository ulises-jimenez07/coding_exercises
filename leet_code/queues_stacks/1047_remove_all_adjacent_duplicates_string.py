"""
Problem: Remove All Adjacent Duplicates In String (LeetCode 1047)

You are given a string s consisting of lowercase English letters. A duplicate
removal consists of choosing two adjacent and equal letters and removing them.

Approach: Stack-based removal
- Use a stack to track characters as we process the string.
- If the current character matches the top of the stack, pop it (adjacent duplicate).
- Otherwise, push the current character onto the stack.
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest
from typing import List


class Solution:
    """Solution for removing adjacent duplicates in a string."""

    def removeDuplicates(self, s: str) -> str:
        """
        Removes all adjacent duplicates from the string s using a stack.
        """
        stack: List[str] = []

        # Process each character to identify adjacent duplicates
        for char in s:
            # If stack top matches current character, remove the duplicate
            if stack and stack[-1] == char:
                stack.pop()
            else:
                # No match found, add character to the stack
                stack.append(char)

        return "".join(stack)


class TestRemoveDuplicates(unittest.TestCase):
    """Unit tests for the Solution class."""

    def setUp(self):
        """Set up the solution instance for testing."""
        self.sol = Solution()

    def test_example_1(self):
        """Test with input 'abbaca' resulting in 'ca'."""
        self.assertEqual(self.sol.removeDuplicates("abbaca"), "ca")

    def test_example_2(self):
        """Test with input 'azxxzy' resulting in 'ay'."""
        self.assertEqual(self.sol.removeDuplicates("azxxzy"), "ay")

    def test_empty_string(self):
        """Test with an empty input string."""
        self.assertEqual(self.sol.removeDuplicates(""), "")

    def test_single_character(self):
        """Test with a single character string."""
        self.assertEqual(self.sol.removeDuplicates("a"), "a")

    def test_no_duplicates(self):
        """Test with a string containing no adjacent duplicates."""
        self.assertEqual(self.sol.removeDuplicates("abcdef"), "abcdef")

    def test_additional_cases(self):
        """Test additional edge cases using enumerate for subtests."""
        test_cases = [
            ("aaaaaa", ""),  # Even number of duplicates
            ("aaaaa", "a"),  # Odd number of duplicates
            ("abba", ""),  # Nested duplicates
            ("abacaba", "abacaba"),  # No adjacent duplicates
        ]
        for i, (input_str, expected) in enumerate(test_cases):
            with self.subTest(case_index=i):
                self.assertEqual(self.sol.removeDuplicates(input_str), expected)


if __name__ == "__main__":
    unittest.main()
