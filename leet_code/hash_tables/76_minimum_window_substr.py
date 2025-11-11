"""
Problem: Find minimum window in string s containing all characters from string t

Approach:
- Use sliding window with two pointers
- Track character frequencies with hash tables
- Expand window until valid, then shrink from left
- Time complexity: O(m + n) where m=len(s), n=len(t)
- Space complexity: O(m + n)
"""

import unittest
from collections import defaultdict


class Solution:
    """Solution for finding minimum window substring containing all target characters."""

    def minWindow(self, s: str, t: str) -> str:
        len_str = len(s)
        len_target = len(t)

        # Can't find t in s if t is longer
        if len_str < len_target:
            return ""

        # Track char frequencies in both strings
        hash_str: defaultdict[str, int] = defaultdict(int)
        hash_target: defaultdict[str, int] = defaultdict(int)

        # Count what we need from target string
        for ch in t:
            hash_target[ch] += 1

        count = 0  # How many chars we've matched so far
        left = 0  # Left pointer of our window
        min_length_win = len_str + 1  # Track smallest window found
        start_index = -1  # Where the min window starts

        # Expand window with right pointer
        for right, ch in enumerate(s):
            hash_str[ch] += 1

            # Only count if it's needed and we haven't exceeded the requirement
            if ch in hash_target and hash_str[ch] <= hash_target[ch]:
                count += 1

            # When we have all chars, try to shrink window from left
            if count == len_target:
                # Remove chars that aren't needed or are extra
                while s[left] not in hash_target or hash_str[s[left]] > hash_target[s[left]]:
                    if s[left] in hash_target:
                        hash_str[s[left]] -= 1
                    left += 1

                # Check if this window is smaller than what we've seen
                if min_length_win > right - left + 1:
                    min_length_win = right - left + 1
                    start_index = left

        return s[start_index : start_index + min_length_win] if start_index != -1 else ""


class TestMinWindow(unittest.TestCase):
    """Test cases for the minimum window substring solution."""

    def setUp(self):
        self.solution = Solution()

    def test_empty_s(self):
        self.assertEqual(self.solution.minWindow("", "A"), "")

    def test_t_longer_than_s(self):
        self.assertEqual(self.solution.minWindow("AB", "ABC"), "")

    def test_substring_at_beginning(self):
        self.assertEqual(self.solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_substring_at_end(self):
        self.assertEqual(self.solution.minWindow("BBBBBBCCCCA", "ABC"), "BCCCCA")

    def test_no_substring_found(self):
        self.assertEqual(self.solution.minWindow("ADOBECODEBAN", "ABCC"), "")

    def test_single_character_t(self):
        self.assertEqual(self.solution.minWindow("ABCDE", "B"), "B")

    def test_all_characters_same(self):
        self.assertEqual(self.solution.minWindow("AAAAA", "A"), "A")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
