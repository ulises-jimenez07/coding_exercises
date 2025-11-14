"""
Problem: Count subarrays with exactly K distinct integers

Approach:
- Use "at most K" trick: exactly K = (at most K) - (at most K-1)
- Sliding window with frequency map to track distinct integers
- Time complexity: O(n)
- Space complexity: O(k)
"""

import unittest
from collections import defaultdict
from typing import List


class Solution:
    """Solution for counting subarrays with exactly K distinct integers."""

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """Counts subarrays with exactly K distinct integers."""
        # Exactly K = (at most K) - (at most K-1)
        return self.sliding_windwow_at_most(nums, k) - self.sliding_windwow_at_most(nums, k - 1)

    def sliding_windwow_at_most(self, nums, distinct_k):
        """Helper function to count subarrays with at most K distinct integers."""
        freq_map = defaultdict(int)
        left = 0
        total_count = 0

        for right, num in enumerate(nums):
            freq_map[num] += 1

            # Shrink window if we have too many distinct integers
            while len(freq_map) > distinct_k:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1

            # All subarrays ending at right are valid
            total_count += right - left + 1

        return total_count


class TestSubarraysWithKDistinct(unittest.TestCase):
    """Test cases for subarrays with K distinct integers."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example with K=2."""
        self.assertEqual(self.solution.subarraysWithKDistinct([1, 2, 1, 2, 3], 2), 7)

    def test_all_same(self):
        """All elements are the same."""
        self.assertEqual(self.solution.subarraysWithKDistinct([1, 1, 1, 1], 1), 10)

    def test_k_equals_one(self):
        """K equals 1."""
        self.assertEqual(self.solution.subarraysWithKDistinct([1, 2, 1, 3, 4], 1), 5)

    def test_k_equals_array_length(self):
        """K equals number of distinct elements."""
        self.assertEqual(self.solution.subarraysWithKDistinct([1, 2, 3], 3), 1)

    def test_small_array(self):
        """Single element array."""
        self.assertEqual(self.solution.subarraysWithKDistinct([1], 1), 1)

    def test_mixed_elements(self):
        """Mixed elements with K=3."""
        self.assertEqual(self.solution.subarraysWithKDistinct([1, 2, 1, 3, 4], 3), 3)


if __name__ == "__main__":
    unittest.main()
