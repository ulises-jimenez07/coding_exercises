"""
Problem: Sort an array into a "wiggle" pattern: nums[0] < nums[1] > nums[2] < nums[3]...
All elements are non-negative integers. It is guaranteed that a valid answer exists.

Approach:
- Sort the original array.
- Split it into two halves: the smaller elements and the larger elements.
- Reverse both halves to handle edge cases where numbers are very close in value.
- Interleave them back into the original array using slicing.
- Time complexity: O(n log n) due to sorting.
- Space complexity: O(n) for the temporary slices.
"""

import unittest
from typing import List


class Solution:
    """Namespace for the solution to LeetCode 324: Wiggle Sort II."""

    def wiggleSort(self, nums: List[int]) -> List[int]:
        """Modifies the array in-place to follow the wiggle sort pattern (strict Inequality)."""
        nums.sort()

        # Find the middle point
        mid = (len(nums) + 1) // 2

        # Create copies of the halves
        left_half = nums[:mid]
        right_half = nums[mid:]

        # Reverse them to avoid identical elements being adjacent during interleaving
        left_half = left_half[::-1]
        right_half = right_half[::-1]

        # Interleave: left half at even, right half at odd indices
        nums[::2] = left_half
        nums[1::2] = right_half

        return nums


class TestWiggleSortII(unittest.TestCase):
    """Unit tests for the Wiggle Sort II solution."""

    def setUp(self):
        self.solution = Solution()

    def _validate_wiggle(self, nums: List[int]):
        """Helper to verify that the array satisfies the wiggle property (strict inequality)."""
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                self.assertLess(nums[i], nums[i + 1], f"Failed at even index {i}")
            else:
                self.assertGreater(nums[i], nums[i + 1], f"Failed at odd index {i}")

    def test_example_1(self):
        """LeetCode example 1: [1, 5, 1, 1, 6, 4]."""
        nums = [1, 5, 1, 1, 6, 4]
        result = self.solution.wiggleSort(nums)
        self._validate_wiggle(result)

    def test_example_2(self):
        """LeetCode example 2: [1, 3, 2, 2, 3, 1]."""
        nums = [1, 3, 2, 2, 3, 1]
        result = self.solution.wiggleSort(nums)
        # Note: multiple valid configurations may exist, checking wiggle property
        self._validate_wiggle(result)

    def test_all_same_not_possible(self):
        """Array with many identical elements (should work if a solution exists)."""
        nums = [1, 1, 2, 1, 2, 2]
        result = self.solution.wiggleSort(nums)
        self._validate_wiggle(result)

    def test_single_element(self):
        """Edge case: single element."""
        nums = [1]
        result = self.solution.wiggleSort(nums)
        self.assertEqual(result, [1])

    def test_two_elements(self):
        """Edge case: two elements."""
        nums = [1, 2]
        result = self.solution.wiggleSort(nums)
        self._validate_wiggle(result)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
