"""
Problem: Running Sum of 1d Array (LeetCode 1480)

Given an array nums, return the running sum array where runningSum[i] = sum(nums[0]…nums[i]).

Approach:
- Build prefix sum array where each element is the cumulative sum up to that index
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest
from typing import List


class Solution:
    """Solution class for running sum of 1d array problem."""

    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Calculate running sum where result[i] = sum of nums[0] to nums[i].

        Strategy: Build prefix sum array by adding current element to previous sum.
        """
        res = [0] * len(nums)
        res[0] = nums[0]

        for i in range(1, len(nums)):
            res[i] = nums[i] + res[i - 1]

        return res


class TestRunningSum(unittest.TestCase):
    """Test cases for running sum solution."""

    def setUp(self):
        self.sol = Solution()

    def test_basic_case(self):
        """Test basic positive numbers."""
        nums = [1, 2, 3, 4]
        result = self.sol.runningSum(nums)
        self.assertEqual(result, [1, 3, 6, 10])

    def test_mixed_numbers(self):
        """Test with positive and negative numbers."""
        nums = [1, 1, 1, 1, 1]
        result = self.sol.runningSum(nums)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_with_negatives(self):
        """Test with negative numbers."""
        nums = [3, 1, 2, 10, 1]
        result = self.sol.runningSum(nums)
        self.assertEqual(result, [3, 4, 6, 16, 17])

    def test_single_element(self):
        """Test single element array."""
        nums = [5]
        result = self.sol.runningSum(nums)
        self.assertEqual(result, [5])

    def test_with_zero(self):
        """Test array with zeros."""
        nums = [0, 0, 0, 0]
        result = self.sol.runningSum(nums)
        self.assertEqual(result, [0, 0, 0, 0])

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        nums = [-1, -2, -3, -4]
        result = self.sol.runningSum(nums)
        self.assertEqual(result, [-1, -3, -6, -10])

    def test_alternating_signs(self):
        """Test alternating positive and negative."""
        nums = [1, -1, 1, -1, 1]
        result = self.sol.runningSum(nums)
        self.assertEqual(result, [1, 0, 1, 0, 1])

    def test_large_numbers(self):
        """Test with larger numbers."""
        nums = [100, 200, 300]
        result = self.sol.runningSum(nums)
        self.assertEqual(result, [100, 300, 600])

    def test_two_elements(self):
        """Test with two elements."""
        nums = [5, 10]
        result = self.sol.runningSum(nums)
        self.assertEqual(result, [5, 15])

    def test_decreasing_sequence(self):
        """Test with decreasing sequence."""
        nums = [10, 5, 2, 1]
        result = self.sol.runningSum(nums)
        self.assertEqual(result, [10, 15, 17, 18])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
