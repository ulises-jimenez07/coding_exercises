"""
Problem: Binary Search - Find target value in sorted array

Approach:
- Classic binary search: divide array in half at each step
- Compare middle element with target to decide which half to search
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Solution class for binary search problem."""

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# --- Unit Tests ---


class TestBinarySearch(unittest.TestCase):
    """
    Unit tests for the search method in the Solution class.
    """

    def setUp(self):
        self.solution = Solution()

    def test_found_at_beginning(self):
        self.assertEqual(
            self.solution.search([-1, 0, 3, 5, 9, 12], -1),
            0,
            "Should find target at index 0",
        )

    def test_found_at_end(self):
        self.assertEqual(
            self.solution.search([-1, 0, 3, 5, 9, 12], 12),
            5,
            "Should find target at last index",
        )

    def test_found_in_middle(self):
        self.assertEqual(
            self.solution.search([-1, 0, 3, 5, 9, 12], 9),
            4,
            "Should find target in the middle",
        )

    def test_not_found(self):
        self.assertEqual(
            self.solution.search([-1, 0, 3, 5, 9, 12], 2),
            -1,
            "Should return -1 when target not found",
        )

    def test_single_element_found(self):
        self.assertEqual(
            self.solution.search([5], 5),
            0,
            "Should find target in single-element array",
        )

    def test_single_element_not_found(self):
        self.assertEqual(
            self.solution.search([5], 1),
            -1,
            "Should return -1 for single-element array when not found",
        )

    def test_empty_array(self):
        self.assertEqual(
            self.solution.search([], 0),
            -1,
            "Should return -1 for empty array",
        )


# Standard boilerplate to run the tests when the script is executed
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
