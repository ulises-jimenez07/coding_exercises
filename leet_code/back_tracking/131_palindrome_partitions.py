"""
Problem: Partition a string into all possible palindromic substrings

Approach:
- Use backtracking to generate all possible partitions
- Check each substring if it's a palindrome before adding to current partition
- Time complexity: O(n * 2^n) where n is string length
- Space complexity: O(n) for recursion stack and temporary arrays
"""


class Solution:
    def partition(self, s):
        ans = []
        self.solution(s, [], ans)
        return ans

    def solution(self, s, curr_arr, ans):
        # Base case: consumed entire string
        if len(s) == 0:
            ans.append(curr_arr[:])
            return

        # Try all possible prefixes
        for i in range(1, len(s) + 1):
            curr_str = s[0:i]
            if self.is_palindrome(curr_str):
                curr_arr.append(curr_str)
                self.solution(s[i:], curr_arr, ans)
                curr_arr.pop()  # Backtrack

    def is_palindrome(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
        return True


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        """Test with a basic palindrome partitioning case."""
        s = "aab"
        expected = [["a", "a", "b"], ["aa", "b"]]
        actual = self.solution.partition(s)
        self.assertCountEqual(actual, expected)

    def test_single_character(self):
        """Test with a single character string."""
        s = "a"
        expected = [["a"]]
        actual = self.solution.partition(s)
        self.assertCountEqual(actual, expected)

    def test_complex_palindrome(self):
        """Test with a string having multiple palindrome partitions."""
        s = "nitin"
        expected = [["n", "i", "t", "i", "n"], ["n", "iti", "n"], ["nitin"]]
        actual = self.solution.partition(s)
        self.assertCountEqual(actual, expected)

    def test_no_palindrome(self):
        """Test with a string that has no non-single-character palindromic partitions."""
        s = "ab"
        expected = [["a", "b"]]
        actual = self.solution.partition(s)
        self.assertCountEqual(actual, expected)

    def test_empty_string(self):
        """Test with an empty string."""
        s = ""
        expected = [[]]
        actual = self.solution.partition(s)
        self.assertCountEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
