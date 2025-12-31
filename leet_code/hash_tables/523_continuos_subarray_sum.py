"""Module for checking continuous subarray sum divisible by k."""

import unittest
from typing import List


class Solution:
    """Check if array has continuous subarray with sum divisible by k."""

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """Check if there's a subarray (length >= 2) with sum divisible by k."""
        prefix_mod = 0
        # Initialize with {0: -1} to handle prefix sum divisible by k
        mod_seen = {0: -1}

        for i, num in enumerate(nums):
            # Track running prefix sum modulo k
            prefix_mod = (prefix_mod + num) % k

            # If we've seen this modulo before, subarray between them is divisible by k
            if prefix_mod in mod_seen:
                # Ensure subarray length is at least 2
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                # Store first occurrence of this modulo value
                mod_seen[prefix_mod] = i

        return False


class TestContinuousSubarraySum(unittest.TestCase):
    """Unit tests for the Continuous Subarray Sum solution."""

    def test_valid_subarray(self):
        """Case with valid subarray sum divisible by k."""
        solution = Solution()
        self.assertTrue(solution.checkSubarraySum([23, 2, 4, 6, 7], 6))

    def test_no_valid_subarray(self):
        """Case with no valid subarray."""
        solution = Solution()
        self.assertFalse(solution.checkSubarraySum([23, 2, 6, 4, 7], 13))

    def test_single_element(self):
        """Case with single element (needs at least 2 elements)."""
        solution = Solution()
        self.assertFalse(solution.checkSubarraySum([5], 5))

    def test_prefix_sum_divisible(self):
        """Case where prefix sum itself is divisible by k."""
        solution = Solution()
        self.assertTrue(solution.checkSubarraySum([5, 0, 0, 0], 3))

    def test_consecutive_zeros(self):
        """Case with consecutive zeros (any k divides 0)."""
        solution = Solution()
        self.assertTrue(solution.checkSubarraySum([0, 0], 1))


if __name__ == "__main__":
    unittest.main()
