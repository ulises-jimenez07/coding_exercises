"""
Problem: Reverse a list of characters in-place

Approach:
- Use two pointers from both ends, swap and move inward
- Continue until pointers meet in middle
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        """Reverses the input list of characters in-place using two pointers."""
        start = 0
        end = len(s) - 1

        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return s


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_odd_length(self):
        """Odd-length string."""
        input_list = ["h", "e", "l", "l", "o"]
        self.solution.reverseString(input_list)
        self.assertEqual(input_list, ["o", "l", "l", "e", "h"])

    def test_even_length(self):
        """Even-length string."""
        input_list = ["r", "a", "c", "e"]
        self.solution.reverseString(input_list)
        self.assertEqual(input_list, ["e", "c", "a", "r"])

    def test_single_character(self):
        """Single character list."""
        input_list = ["a"]
        self.solution.reverseString(input_list)
        self.assertEqual(input_list, ["a"])

    def test_empty_list(self):
        """Empty list."""
        input_list: List[str] = []
        self.solution.reverseString(input_list)
        self.assertEqual(input_list, [])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
