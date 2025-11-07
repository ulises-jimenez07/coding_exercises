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


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1 = len(s)
        len2 = len(t)

        if len1 < len2:
            return ""

        hash_pat: dict[str, int] = {}
        hash_str: dict[str, int] = {}

        # Count characters in target string
        for i in range(len2):
            char = t[i]
            hash_pat[char] = hash_pat.get(char, 0) + 1

        count = 0
        left = 0
        start_index = -1
        min_len = float("inf")

        # Expand window with right pointer
        for right in range(len1):
            char = s[right]
            hash_str[char] = hash_str.get(char, 0) + 1

            if char in hash_pat and hash_str[char] <= hash_pat[char]:
                count += 1

            # Shrink window from left when valid
            if count == len2:
                while s[left] not in hash_pat or hash_str[s[left]] > hash_pat[s[left]]:
                    left_char = s[left]
                    if left_char in hash_pat and hash_str[left_char] > hash_pat.get(left_char, 0):
                        hash_str[left_char] -= 1
                    left += 1

                window_len = right - left + 1

                if min_len > window_len:
                    min_len = window_len
                    start_index = left

        if start_index == -1:
            return ""

        return s[start_index : start_index + int(min_len)]


class TestMinWindow(unittest.TestCase):
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
