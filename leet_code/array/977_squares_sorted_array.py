"""
Problem: Sort Array by Squares of Elements
Given an integer array sorted in non-decreasing order, return the array with its elements
sorted in ascending order of their squares (i.e., by absolute value). The original values
are returned, not the squares themselves.

Examples from problem statement:
  [1, 5, 7, 7, 8, 10]      →  [1, 5, 7, 7, 8, 10]        (all positive, order unchanged)
  [-5, -3, -3, 2, 4, 4, 8] →  [2, -3, -3, 4, 4, -5, 8]   (sorted by |x|, original values kept)

Related: LeetCode 977 - Squares of a Sorted Array (returns squared values instead of originals)

Approach: Two Pointers
- The input is sorted, so the largest absolute values are at the two ends.
- Use two pointers (left=0, right=n-1) and fill the result from right to left.
- At each step, compare abs(nums[left]) vs abs(nums[right]), place the element with the
  larger absolute value at result[pos], move that pointer inward, decrement pos.

Complexity:
- Time:  O(n)
- Space: O(n) for the result array
"""

import unittest
from typing import List


class Solution:
    """Solution for sorting an array by the squares of its elements."""

    def sortBySquares(self, nums: List[int]) -> List[int]:
        """Return elements sorted by their absolute value (ascending) in O(n)."""
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1  # Fill result from the largest position downward

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left]
                left += 1
            else:
                result[pos] = nums[right]
                right -= 1
            pos -= 1

        return result


class TestSortBySquares(unittest.TestCase):
    """Unit tests for sortBySquares."""

    def setUp(self):
        self.solution = Solution()

    def test_example_1_all_positive(self):
        """All positive — sorted by square = sorted by value, output unchanged."""
        nums = [1, 5, 7, 7, 8, 10]
        self.assertEqual(self.solution.sortBySquares(nums), [1, 5, 7, 7, 8, 10])

    def test_example_2_mixed(self):
        """Mixed negatives and positives — sort original values by |x|."""
        nums = [-5, -3, -3, 2, 4, 4, 8]
        self.assertEqual(self.solution.sortBySquares(nums), [2, -3, -3, 4, 4, -5, 8])

    def test_all_negative(self):
        """All negative — largest |x| is at the left, smallest at the right."""
        nums = [-7, -3, -1]
        self.assertEqual(self.solution.sortBySquares(nums), [-1, -3, -7])

    def test_single_element(self):
        """Single element — trivially sorted."""
        self.assertEqual(self.solution.sortBySquares([-3]), [-3])
        self.assertEqual(self.solution.sortBySquares([4]), [4])

    def test_zeros(self):
        """Zeros have square 0 — smallest possible."""
        nums = [-2, 0, 0, 3]
        self.assertEqual(self.solution.sortBySquares(nums), [0, 0, -2, 3])

    def test_symmetric_array(self):
        """Symmetric array — both ends have equal absolute values."""
        nums = [-3, -1, 0, 1, 3]
        result = self.solution.sortBySquares(nums)
        # Sorted by |x|: 0, ±1, ±1, ±3, ±3
        self.assertEqual([abs(x) for x in result], [0, 1, 1, 3, 3])

    def test_two_elements(self):
        """Minimal two-element input."""
        self.assertEqual(self.solution.sortBySquares([-1, 2]), [-1, 2])
        self.assertEqual(self.solution.sortBySquares([-2, 1]), [1, -2])


if __name__ == "__main__":
    unittest.main()
