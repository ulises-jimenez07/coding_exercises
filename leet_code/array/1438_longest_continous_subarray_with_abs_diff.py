"""
Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Approach:
- Use two heaps to track min and max values in sliding window
- Max heap (negated values) to get maximum element
- Min heap to get minimum element
- Store (value, index) pairs to track positions
- When max-min exceeds limit, shrink window from left
- Remove stale elements from heaps that are outside window
- Time complexity: O(n log n)
- Space complexity: O(n)
"""

import heapq
import unittest
from typing import List


class Solution:
    """Solution for finding longest continuous subarray with absolute difference <= limit."""

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """Finds longest subarray where absolute difference between max and min <= limit."""
        min_heap: list[tuple[int, int]] = []  # Stores (value, index) to track minimum
        max_heap: list[tuple[int, int]] = []  # Stores (-value, index) to track maximum
        left = 0
        max_length = 0

        for right, num in enumerate(nums):
            # Add current element to both heaps
            heapq.heappush(max_heap, (-num, right))
            heapq.heappush(min_heap, (num, right))

            # Shrink window if difference exceeds limit
            while -max_heap[0][0] - min_heap[0][0] > limit:
                # Move left pointer to exclude the element causing violation
                left += 1
                # Remove stale elements from max heap (outside current window)
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)

                # Remove stale elements from min heap (outside current window)
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            # Update maximum length of valid subarray
            max_length = max(max_length, right - left + 1)

        return max_length


class TestLongestSubarray(unittest.TestCase):
    """Test cases for longest subarray with absolute difference constraint."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example with limit 4."""
        nums = [8, 2, 4, 7]
        limit = 4
        self.assertEqual(self.solution.longestSubarray(nums, limit), 2)

    def test_larger_example(self):
        """Larger example with limit 5."""
        nums = [10, 1, 2, 4, 7, 2]
        limit = 5
        self.assertEqual(self.solution.longestSubarray(nums, limit), 4)

    def test_small_limit(self):
        """Small limit that restricts subarray size."""
        nums = [4, 2, 2, 2, 4, 4, 2, 2]
        limit = 0
        self.assertEqual(self.solution.longestSubarray(nums, limit), 3)

    def test_all_elements_valid(self):
        """All elements within limit."""
        nums = [1, 2, 3, 4, 5]
        limit = 10
        self.assertEqual(self.solution.longestSubarray(nums, limit), 5)

    def test_single_element(self):
        """Single element array."""
        nums = [5]
        limit = 2
        self.assertEqual(self.solution.longestSubarray(nums, limit), 1)

    def test_two_elements(self):
        """Two elements within limit."""
        nums = [3, 6]
        limit = 3
        self.assertEqual(self.solution.longestSubarray(nums, limit), 2)

    def test_two_elements_exceeds_limit(self):
        """Two elements exceeding limit."""
        nums = [3, 10]
        limit = 5
        self.assertEqual(self.solution.longestSubarray(nums, limit), 1)


if __name__ == "__main__":
    unittest.main()
