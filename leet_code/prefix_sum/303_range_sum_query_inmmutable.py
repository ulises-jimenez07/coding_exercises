"""
Problem: Range Sum Query - Immutable (LeetCode 303)

Given an integer array nums, handle multiple queries to calculate the sum of elements
between indices left and right (inclusive).

Approach:
- Use prefix sum (cumulative sum) array to precompute sums
- Query in O(1) time by computing difference: cum_sum[right+1] - cum_sum[left]
- Time complexity: O(n) for initialization, O(1) per query
- Space complexity: O(n)
"""

import unittest
from typing import List


class NumArray:
    """
    Data structure for efficient range sum queries using prefix sum approach.
    """

    def __init__(self, nums: List[int]):
        """
        Initialize the NumArray with a prefix sum array.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        # Create cumulative sum array with extra element at start for easier computation
        self.cum_sum = [0] * (len(nums) + 1)

        # Build prefix sum array where cum_sum[i] = sum of first i elements
        for i, num in enumerate(nums):
            self.cum_sum[i + 1] = self.cum_sum[i] + num

    def sumRange(self, left: int, right: int) -> int:
        """
        Calculate sum of elements between indices left and right (inclusive).

        Time complexity: O(1)
        """
        # Sum from left to right = cum_sum[right+1] - cum_sum[left]
        # This works because cum_sum[right+1] contains sum up to right (inclusive)
        # and cum_sum[left] contains sum up to left-1 (exclusive)
        return self.cum_sum[right + 1] - self.cum_sum[left]


class TestNumArray(unittest.TestCase):
    """Test cases for NumArray class."""

    def test_basic_case(self):
        """Test basic range sum queries."""
        nums = [-2, 0, 3, -5, 2, -1]
        obj = NumArray(nums)

        self.assertEqual(obj.sumRange(0, 2), 1)  # -2 + 0 + 3 = 1
        self.assertEqual(obj.sumRange(2, 5), -1)  # 3 + (-5) + 2 + (-1) = -1
        self.assertEqual(obj.sumRange(0, 5), -3)  # Sum of entire array

    def test_single_element_range(self):
        """Test queries with single element ranges."""
        nums = [1, 2, 3, 4, 5]
        obj = NumArray(nums)

        self.assertEqual(obj.sumRange(0, 0), 1)
        self.assertEqual(obj.sumRange(2, 2), 3)
        self.assertEqual(obj.sumRange(4, 4), 5)

    def test_entire_array(self):
        """Test query spanning entire array."""
        nums = [1, 2, 3, 4, 5]
        obj = NumArray(nums)

        self.assertEqual(obj.sumRange(0, 4), 15)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -2, -3, -4, -5]
        obj = NumArray(nums)

        self.assertEqual(obj.sumRange(0, 2), -6)
        self.assertEqual(obj.sumRange(1, 3), -9)

    def test_mixed_numbers(self):
        """Test with mix of positive, negative, and zero."""
        nums = [5, -3, 0, 2, -1, 4]
        obj = NumArray(nums)

        self.assertEqual(obj.sumRange(1, 3), -1)  # -3 + 0 + 2 = -1
        self.assertEqual(obj.sumRange(0, 5), 7)  # Sum of all
        self.assertEqual(obj.sumRange(3, 5), 5)  # 2 + (-1) + 4 = 5

    def test_single_element_array(self):
        """Test with array containing single element."""
        nums = [42]
        obj = NumArray(nums)

        self.assertEqual(obj.sumRange(0, 0), 42)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
