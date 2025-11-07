"""
Problem: Generate all unique permutations from array with duplicates

Approach:
- Use Counter to track available count of each unique number
- Backtracking only processes each unique number once per position
- Decrement/increment counter during explore/backtrack
- Time complexity: O(n!)
- Space complexity: O(n) for recursion and counter
"""

import unittest
from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def _permute_unique(curr, counter):
            # Base case: built complete permutation
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            # Try each unique number with available count
            for num in counter:
                if counter[num] > 0:
                    curr.append(num)
                    counter[num] -= 1
                    _permute_unique(curr, counter)
                    counter[num] += 1  # Backtrack
                    curr.pop()

        ans: list[list[int]] = []
        _permute_unique([], Counter(nums))
        return ans


class TestPermuteUnique(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.maxDiff = None

    def test_empty_list(self):
        self.assertEqual(self.solution.permuteUnique([]), [[]])

    def test_single_element(self):
        self.assertEqual(self.solution.permuteUnique([1]), [[1]])

    def test_distinct_elements(self):
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertCountEqual(self.solution.permuteUnique([1, 2, 3]), expected)

    def test_duplicate_elements(self):
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertCountEqual(self.solution.permuteUnique([1, 1, 2]), expected)

    def test_another_duplicate_set(self):
        expected = [
            [1, 1, 2, 2],
            [1, 2, 1, 2],
            [1, 2, 2, 1],
            [2, 1, 1, 2],
            [2, 1, 2, 1],
            [2, 2, 1, 1],
        ]
        self.assertCountEqual(self.solution.permuteUnique([1, 1, 2, 2]), expected)


if __name__ == "__main__":
    unittest.main()
