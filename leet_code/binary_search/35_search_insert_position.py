"""
Problem: Find the index to insert target in a sorted array

Approach:
- Use binary search to find insertion position
- Return position where target should be or is found
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Solution class for find the index to insert target in a sorted array problem."""

    def searchInsert_v1(self, nums: List[int], target: int) -> int:
        """
        Version 1: Binary Search with closed interval [start, end].

        - Starting left/right: start = 0, end = len(nums) - 1.
        - Stop condition: start > end (while start <= end).
        - Condition to move left: If nums[mid] < target, target is in the right half.
        - Condition to move right: If nums[mid] >= target, target is in the left half
          (or at mid), update potential answer and shrink right.
        """
        start = 0
        end = len(nums) - 1
        ans = len(nums)

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < target:
                # Move left boundary: target is greater than mid element
                start = mid + 1
            else:
                # Move right boundary: mid element is greater than or equal to target
                ans = mid
                end = mid - 1
        return ans

    def searchInsert_v2(self, nums: List[int], target: int) -> int:
        """
        Version 2: Binary Search with half-open interval [left, right).

        - Starting left/right: left = 0, right = len(nums).
        - Stop condition: left == right (while left < right).
        - Condition to move left: If nums[mid] < target, target is in the right half.
        - Condition to move right: If nums[mid] >= target, mid could be the insertion
          point, so shrink right to mid.
        """
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                # Move right boundary: mid element is >= target
                right = mid
            else:
                # Move left boundary: mid element is < target
                left = mid + 1

        return left

    # Alias for compatibility or default preference
    searchInsert = searchInsert_v2


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def setUp(self):
        """
        Set up a Solution instance for each test.
        """
        self.solution = Solution()

    def run_on_both(self, nums, target, expected):
        """
        Helper to run test cases on both implementations.
        """
        self.assertEqual(self.solution.searchInsert_v1(nums, target), expected, f"v1 failed for {nums}, {target}")
        self.assertEqual(self.solution.searchInsert_v2(nums, target), expected, f"v2 failed for {nums}, {target}")

    def test_target_is_found(self):
        """
        Test cases where the target is present in the array.
        """
        self.run_on_both([1, 3, 5, 6], 5, 2)
        self.run_on_both([1, 3, 5, 6], 1, 0)
        self.run_on_both([1, 3, 5, 6], 6, 3)

    def test_target_is_not_found(self):
        """
        Test cases where the target is not present in the array,
        and we need to find the correct insertion position.
        """
        self.run_on_both([1, 3, 5, 6], 2, 1)
        self.run_on_both([1, 3, 5, 6], 7, 4)
        self.run_on_both([1, 3, 5, 6], 0, 0)

    def test_empty_array(self):
        """
        Test case for an empty input array.
        The target should be inserted at index 0.
        """
        self.run_on_both([], 5, 0)

    def test_single_element_array(self):
        """
        Test cases for an array with a single element.
        """
        self.run_on_both([5], 5, 0)
        self.run_on_both([5], 6, 1)
        self.run_on_both([5], 4, 0)


if __name__ == "__main__":
    unittest.main()
