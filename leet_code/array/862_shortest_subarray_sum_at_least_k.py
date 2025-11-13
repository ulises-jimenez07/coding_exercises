"""
Problem: Find the shortest subarray with sum at least K

Approach:
- Use prefix sums combined with monotonic deque
- Deque maintains indices in increasing order of prefix sums
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest
from collections import deque
from typing import List


class Solution:
    """Solution for finding shortest subarray with sum at least K."""

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """Finds the shortest subarray with sum at least K."""
        n = len(nums)

        # Build prefix sum array
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        # Deque stores indices of prefix sums in increasing order
        candidate_indices: deque[int] = deque()
        shortest_sub_array = n + 1

        for i in range(n + 1):
            # Check if we found a valid subarray from front indices
            while candidate_indices and prefix_sum[i] - prefix_sum[candidate_indices[0]] >= k:
                shortest_sub_array = min(shortest_sub_array, i - candidate_indices.popleft())

            # Remove indices with larger prefix sums (they won't be useful)
            while candidate_indices and prefix_sum[i] <= prefix_sum[candidate_indices[-1]]:
                candidate_indices.pop()

            candidate_indices.append(i)

        return shortest_sub_array if shortest_sub_array != n + 1 else -1


class TestShortestSubarray(unittest.TestCase):
    """Test cases for shortest subarray with sum at least K."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example with positive and negative numbers."""
        self.assertEqual(self.solution.shortestSubarray([1], 1), 1)

    def test_with_negatives(self):
        """Example with negative numbers."""
        self.assertEqual(self.solution.shortestSubarray([2, -1, 2], 3), 3)

    def test_shortest_at_start(self):
        """Shortest subarray is at the start."""
        self.assertEqual(self.solution.shortestSubarray([1, 2], 4), -1)

    def test_large_k(self):
        """K larger than total sum."""
        self.assertEqual(self.solution.shortestSubarray([1, 2, 3], 10), -1)

    def test_single_element_sufficient(self):
        """Single element meets the requirement."""
        self.assertEqual(self.solution.shortestSubarray([10, 1, 2], 10), 1)

    def test_entire_array_needed(self):
        """Entire array is the shortest valid subarray."""
        self.assertEqual(self.solution.shortestSubarray([1, 1, 1, 1], 4), 4)

    def test_middle_subarray(self):
        """Shortest subarray is in the middle."""
        self.assertEqual(self.solution.shortestSubarray([1, 2, 3, 4], 7), 2)


if __name__ == "__main__":
    unittest.main()
