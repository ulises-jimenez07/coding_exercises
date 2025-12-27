"""Module for splitting array into k subarrays with minimum largest sum."""

import unittest
from typing import List


class Solution:
    """Split array into k subarrays minimizing the largest subarray sum."""

    def splitArray(self, nums: List[int], k: int) -> int:
        """Find minimum largest sum when splitting nums into k subarrays."""

        def min_subarrays_required(max_sum_allowed):
            """Count minimum subarrays needed if each can have max_sum_allowed."""
            current_sum = 0
            splits_required = 0

            for element in nums:
                # If adding element exceeds limit, start a new subarray
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    current_sum = element
                    splits_required += 1

            # +1 because splits count gaps between subarrays
            return splits_required + 1

        # Binary search bounds: min is largest element, max is total sum
        left = max(nums)
        right = sum(nums)
        minimum_largest_split_sum = right

        while left <= right:
            max_sum_allowed = (left + right) // 2

            # If we can split into k or fewer subarrays, try smaller sum
            if min_subarrays_required(max_sum_allowed) <= k:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                # Need larger sum to fit into k subarrays
                left = max_sum_allowed + 1

        return minimum_largest_split_sum


class TestSplitArrayLargestSum(unittest.TestCase):
    """Unit tests for the Split Array Largest Sum solution."""

    def test_single_subarray(self):
        """Case with k=1, entire array is one subarray."""
        solution = Solution()
        self.assertEqual(solution.splitArray([7, 2, 5, 10, 8], 1), 32)

    def test_multiple_subarrays(self):
        """Standard case with multiple subarrays."""
        solution = Solution()
        self.assertEqual(solution.splitArray([7, 2, 5, 10, 8], 2), 18)

    def test_equal_elements(self):
        """Case with all equal elements."""
        solution = Solution()
        self.assertEqual(solution.splitArray([1, 1, 1, 1], 2), 2)

    def test_single_element(self):
        """Case with single element array."""
        solution = Solution()
        self.assertEqual(solution.splitArray([1], 1), 1)


if __name__ == "__main__":
    unittest.main()
