"""
Problem: Find a peak element in an array. A peak element is an element that is strictly
greater than its neighbors.

Approach: Binary Search
- Compare the middle element with its right neighbor to determine the direction
  of a potential peak.
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """
    Implementation of the peak finding algorithm using binary search.
    """

    def findPeakElement(self, nums: List[int]) -> int:
        """
        Finds a peak element in the given array and returns its index.
        """
        left, right = 0, len(nums) - 1

        # Standard binary search logic for finding a peak
        while left < right:
            mid = (left + right) // 2

            # Check if we are in an ascending or descending slope
            if nums[mid] > nums[mid + 1]:
                # If descending, peak must be at mid or to the left
                right = mid
            else:
                # If ascending, peak must be to the right
                left = mid + 1

        # left and right converge to any peak index
        return left


class TestFindPeakElement(unittest.TestCase):
    """
    Unit tests to verify the correctness of the peak finding algorithm.
    """

    def setUp(self):
        self.solution = Solution()

    def test_provided_examples(self):
        """Test with standard LeetCode examples."""
        test_cases = [([1, 2, 3, 1], {2}), ([1, 2, 1, 3, 5, 6, 4], {1, 5})]
        for _, (nums, expected) in enumerate(test_cases):
            self.assertIn(self.solution.findPeakElement(nums), expected)

    def test_edge_cases(self):
        """Test with edge cases like single elements and small arrays."""
        # Single element case
        self.assertEqual(self.solution.findPeakElement([1]), 0)
        # Two elements cases
        self.assertEqual(self.solution.findPeakElement([1, 2]), 1)
        self.assertEqual(self.solution.findPeakElement([2, 1]), 0)

    def test_monotonic_arrays(self):
        """Test with strictly increasing and decreasing arrays."""
        # Strictly increasing
        self.assertEqual(self.solution.findPeakElement([1, 2, 3, 4, 5]), 4)
        # Strictly decreasing
        self.assertEqual(self.solution.findPeakElement([5, 4, 3, 2, 1]), 0)

    def test_multiple_peaks(self):
        """Verify that any valid peak is returned when multiple exist."""
        nums = [1, 3, 2, 4, 1]
        peak_idx = self.solution.findPeakElement(nums)
        # A peak must be larger than its immediate neighbors
        is_peak = True
        if peak_idx > 0 and nums[peak_idx] <= nums[peak_idx - 1]:
            is_peak = False
        if peak_idx < len(nums) - 1 and nums[peak_idx] <= nums[peak_idx + 1]:
            is_peak = False
        self.assertTrue(is_peak)


if __name__ == "__main__":
    unittest.main()
