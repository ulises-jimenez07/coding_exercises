"""
Problem: Find the longest common prefix string amongst an array of strings

Approach:
- Use binary search on the length of the prefix
- Check if all strings share a prefix of length mid
- Time complexity: O(S * log n) where S is sum of all characters
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(x) for x in strs)
        start, end = 1, min_len

        while start <= end:
            mid = (start + end) // 2
            if self.is_common_prefix(strs, mid):
                start = mid + 1
            else:
                end = mid - 1

        return strs[0][:end]

    def is_common_prefix(self, strs, l):
        # Check if first l characters match across all strings
        str1 = strs[0][:l]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True


# --- Unit Tests ---


class TestLongestCommonPrefix(unittest.TestCase):
    """
    Unit tests for the longestCommonPrefix method in the Solution class.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        self.assertEqual(
            self.solution.longestCommonPrefix(["flower", "flow", "flight"]),
            "fl",
            "Should return 'fl' for ['flower', 'flow', 'flight']",
        )

    def test_example_two(self):
        self.assertEqual(
            self.solution.longestCommonPrefix(["dog", "racecar", "car"]),
            "",
            "Should return '' for ['dog', 'racecar', 'car']",
        )

    def test_empty_list(self):
        self.assertEqual(self.solution.longestCommonPrefix([]), "", "Should return '' for an empty list")

    def test_single_string(self):
        self.assertEqual(
            self.solution.longestCommonPrefix(["a"]), "a", "Should return the string itself for a single-element list"
        )

    def test_all_same_string(self):
        self.assertEqual(
            self.solution.longestCommonPrefix(["abc", "abc", "abc"]),
            "abc",
            "Should return the string itself when all are identical",
        )

    def test_empty_strings_present(self):
        self.assertEqual(
            self.solution.longestCommonPrefix(["a", ""]), "", "Should return '' if an empty string is present"
        )
        self.assertEqual(
            self.solution.longestCommonPrefix(["", "b", "c"]), "", "Should return '' if an empty string is present"
        )

    def test_no_common_prefix_one_char(self):
        self.assertEqual(self.solution.longestCommonPrefix(["apple", "apricot", "apex"]), "ap", "Should return 'ap'")


# Standard boilerplate to run the tests when the script is executed
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
