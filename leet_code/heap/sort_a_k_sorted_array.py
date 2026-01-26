"""
Problem: Sort a K-Sorted Array
Given an array where each element is at most k distances away from its target position,
sort the array efficiently.

Approach:
- Use a min-heap of size k + 1 to keep track of the smallest current elements.
- The smallest element in the heap will always be the correct element for the current position.
- Time complexity: O(n log k)
- Space complexity: O(k)
"""

import heapq
import unittest
from typing import List


class Solution:
    """Class to sort a k-sorted array."""

    def sortKSortedArray(self, nums: List[int], k: int) -> List[int]:
        """
        Sorts an array where each element is at most k distance from its sorted position.
        """
        if not nums:
            return []

        # Initialize min-heap with the first k + 1 elements
        # Since each element is at most k away, the minimum must be in the first k + 1
        min_heap = nums[: k + 1]
        heapq.heapify(min_heap)

        insert_index = 0

        # Process remaining elements: pop minimum and push new element
        for i in range(k + 1, len(nums)):
            nums[insert_index] = heapq.heappop(min_heap)
            insert_index += 1
            heapq.heappush(min_heap, nums[i])

        # Empty the heap into the remaining positions
        while min_heap:
            nums[insert_index] = heapq.heappop(min_heap)
            insert_index += 1

        return nums


class TestSortKSortedArray(unittest.TestCase):
    """Unit tests for sortKSortedArray implementation."""

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Standard k-sorted array test."""
        nums = [6, 5, 3, 2, 8, 10, 9]
        k = 3
        expected = [2, 3, 5, 6, 8, 9, 10]
        self.assertEqual(self.solution.sortKSortedArray(nums, k), expected)

    def test_empty_list(self):
        """Edge case: empty list."""
        self.assertEqual(self.solution.sortKSortedArray([], 2), [])

    def test_single_element(self):
        """Edge case: single element."""
        self.assertEqual(self.solution.sortKSortedArray([1], 0), [1])

    def test_already_sorted(self):
        """Test with an already sorted array."""
        nums = [1, 2, 3, 4, 5]
        k = 2
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.sortKSortedArray(nums, k), expected)

    def test_multiple_scenarios(self):
        """Test multiple scenarios using enumerate."""
        scenarios = [
            ([3, 2, 1], 2, [1, 2, 3]),
            ([10, 9, 8, 7, 4, 70, 60, 50], 4, [4, 7, 8, 9, 10, 50, 60, 70]),
        ]
        for i, (nums, k, expected) in enumerate(scenarios):
            with self.subTest(scenario=i):
                # We use a copy of nums because the function might modify it in-place
                self.assertEqual(self.solution.sortKSortedArray(nums[:], k), expected)


if __name__ == "__main__":
    unittest.main()
