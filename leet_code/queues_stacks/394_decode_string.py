"""
Problem: Decode String - decode a pattern of k[encoded_string]

Approach:
- Use a stack to track the previous strings and multiplier counts
- Process characters: digits form counts, '[' starts a new nesting level
- Time complexity: O(n) where n is the length of the decoded string
- Space complexity: O(n) to store the stack and intermediate strings
"""

import unittest


class Solution:
    """
    Provides a solution for the LeetCode 'Decode String' problem.
    """

    def decodeString(self, s: str) -> str:
        """
        Decodes a string where k[encoded_string] repeats the inner part k times.
        """
        stack = []
        current_str = ""
        current_num = 0

        # Use enumerate to iterate through the string characters
        for _, char in enumerate(s):
            if char.isdigit():
                # Build the multiplier number for multi-digit cases
                current_num = current_num * 10 + int(char)
            elif char == "[":
                # Push the current state to the stack and reset for the inner segment
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == "]":
                # Pop the previous state and append the repeated current segment
                prev_str, num = stack.pop()
                current_str = prev_str + (num * current_str)
            else:
                # Append normal characters to the current string segment
                current_str += char

        return current_str


class TestDecodeString(unittest.TestCase):
    """
    Unit tests for the decodeString method.
    """

    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example_1(self):
        """Test with input '3[a]2[bc]'."""
        self.assertEqual(self.solution.decodeString("3[a]2[bc]"), "aaabcbc")

    def test_leetcode_example_2(self):
        """Test with input '3[a2[c]]'."""
        self.assertEqual(self.solution.decodeString("3[a2[c]]"), "accaccacc")

    def test_leetcode_example_3(self):
        """Test with input '2[abc]3[cd]ef'."""
        self.assertEqual(self.solution.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_single_element(self):
        """Test with a single character string."""
        self.assertEqual(self.solution.decodeString("a"), "a")

    def test_nested_brackets(self):
        """Test with multiple levels of nested brackets."""
        self.assertEqual(self.solution.decodeString("2[2[b]]"), "bbbb")

    def test_empty_string(self):
        """Test with an empty string input."""
        self.assertEqual(self.solution.decodeString(""), "")

    def test_large_multiplier(self):
        """Test with a multi-digit multiplier."""
        self.assertEqual(self.solution.decodeString("10[a]"), "aaaaaaaaaa")


if __name__ == "__main__":
    unittest.main()
