"""
Problem: Generate all permutations of distinct integers

Approach:
- Use backtracking to build permutations
- Track used elements to avoid duplicates in current permutation
- Explore all possibilities by trying each unused number at each position
- Time complexity: O(n!)
- Space complexity: O(n) for recursion stack
"""

import unittest
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _permute(curr):
            # Base case: built complete permutation
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            # Try each number not yet used
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    _permute(curr)
                    curr.pop()  # Backtrack

        ans: list[list[int]] = []
        _permute([])
        return ans


class TestPermute(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.maxDiff = None

    def test_empty_list(self):
        self.assertEqual(self.solution.permute([]), [[]])

    def test_single_element(self):
        self.assertEqual(self.solution.permute([1]), [[1]])

    def test_multiple_elements(self):
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertCountEqual(self.solution.permute([1, 2, 3]), expected)


if __name__ == "__main__":
    unittest.main()
