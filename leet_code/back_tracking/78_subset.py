"""
Problem: Generate all possible subsets (power set) of an array

Approach:
- Use backtracking to build subsets incrementally
- Add current subset at each recursion level
- For each element, choose to include or exclude it
- Time complexity: O(2^n) as there are 2^n subsets
- Space complexity: O(n) for recursion stack
"""

import unittest
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generates all possible subsets (power set) of an array of unique elements.
    """

    def _subsets(nums, ans, curr, index):
        """
        Helper backtracking function to generate subsets.
        """
        # Add current subset
        ans.append(curr[:])

        # Try adding each remaining element
        for i, num in enumerate(nums[index:], start=index):
            curr.append(num)
            _subsets(nums, ans, curr, i + 1)
            curr.pop()  # Backtrack

    ans: List[List[int]] = []
    curr: List[int] = []
    _subsets(nums, ans, curr, 0)
    return ans


class TestSubsets(unittest.TestCase):
    """
    Unit tests for subsets solution.
    """

    def setUp(self):
        self.maxDiff = None

    def test_example_one(self):
        """Test with input [1, 2, 3]."""
        nums = [1, 2, 3]
        expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        actual = subsets(nums)
        self.assertCountEqual(actual, expected)

    def test_empty_list(self):
        """Test with an empty input list."""
        nums = []
        expected = [[]]
        actual = subsets(nums)
        self.assertCountEqual(actual, expected)

    def test_single_element(self):
        """Test with a single-element list."""
        nums = [1]
        expected = [[], [1]]
        actual = subsets(nums)
        self.assertCountEqual(actual, expected)

    def test_two_elements(self):
        """Test with a two-element list."""
        nums = [1, 2]
        expected = [[], [1], [1, 2], [2]]
        actual = subsets(nums)
        self.assertCountEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
