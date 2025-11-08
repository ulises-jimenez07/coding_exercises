"""
Problem: Find the maximum average of a contiguous subarray of length k

Approach:
- Use sliding window technique to maintain sum of k consecutive elements
- Initialize window with first k elements, then slide one position at a time
- Update window by subtracting leftmost element and adding new rightmost element
- Time complexity: O(n) - single pass through array
- Space complexity: O(1) - only storing window sum and max
"""

import unittest
from typing import List


class Solution:
    """Solution for LeetCode problem 643: Maximum Average Subarray I."""

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """Finds maximum average of contiguous subarray of length k using sliding window."""
        window = sum(nums[:k])
        max_window = window

        for i in range(k, len(nums)):
            window = window - nums[i - k] + nums[i]
            max_window = max(window, max_window)

        return max_window / k


class TestSolution(unittest.TestCase):
    """Test cases for Solution class."""

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """Standard case with mixed positive and negative numbers."""
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        expected = 12.75
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, expected)

    def test_example2(self):
        """Single element array."""
        nums = [5]
        k = 1
        expected = 5.0
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, expected)

    def test_example3(self):
        """Window size of 1 with multiple elements."""
        nums = [0, 4, 0, 3, 2]
        k = 1
        expected = 4.0
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
