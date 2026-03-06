"""
Problem: Sort an array into a "wiggle" pattern: nums[0] <= nums[1] >= nums[2] <= nums[3]...

Approach:
- Iterate through the array once.
- For even indices, ensure nums[i] <= nums[i+1].
- For odd indices, ensure nums[i] >= nums[i+1].
- Swap adjacent elements if they violate the condition.
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Namespace for the solution to LeetCode 280: Wiggle Sort."""

    def wiggleSort(self, nums: List[int]) -> None:
        """Modifies the array in-place to follow the wiggle sort pattern."""
        # Use range to compare current element with the next one
        for i in range(len(nums) - 1):
            # Check if even index should be <= next or odd index should be >= next
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


class TestWiggleSort(unittest.TestCase):
    """Unit tests for the Wiggle Sort solution."""

    def setUp(self):
        self.solution = Solution()

    def _validate_wiggle(self, nums: List[int]):
        """Helper to verify that the array satisfies the wiggle property."""
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                self.assertLessEqual(nums[i], nums[i + 1], f"Failed at even index {i}")
            else:
                self.assertGreaterEqual(nums[i], nums[i + 1], f"Failed at odd index {i}")

    def test_example_1(self):
        """LeetCode example: [3, 5, 2, 1, 6, 4]."""
        nums = [3, 5, 2, 1, 6, 4]
        self.solution.wiggleSort(nums)
        self._validate_wiggle(nums)

    def test_sorted_ascending(self):
        """Array already sorted in ascending order."""
        nums = [1, 2, 3, 4, 5, 6]
        self.solution.wiggleSort(nums)
        self._validate_wiggle(nums)

    def test_sorted_descending(self):
        """Array sorted in descending order."""
        nums = [6, 5, 4, 3, 2, 1]
        self.solution.wiggleSort(nums)
        self._validate_wiggle(nums)

    def test_all_same(self):
        """Array with all elements the same."""
        nums = [2, 2, 2, 2]
        self.solution.wiggleSort(nums)
        self.assertEqual(nums, [2, 2, 2, 2])

    def test_empty_list(self):
        """Edge case: empty list."""
        nums = []
        self.solution.wiggleSort(nums)
        self.assertEqual(nums, [])

    def test_single_element(self):
        """Edge case: single element."""
        nums = [1]
        self.solution.wiggleSort(nums)
        self.assertEqual(nums, [1])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
