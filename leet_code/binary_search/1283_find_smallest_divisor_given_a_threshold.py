"""Module for finding smallest divisor given a threshold."""

import math
import unittest
from typing import List


class Solution:
    """Find smallest divisor such that sum of ceiling divisions is <= threshold."""

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """Find smallest divisor where sum of ceil(num/divisor) <= threshold."""

        def sum_div(divisor):
            """Calculate sum of ceiling divisions for all numbers."""
            res = 0
            for num in nums:
                # Ceiling division: round up to nearest integer
                res += math.ceil(num / divisor)
            return res

        # Binary search bounds: min is 1, max is largest number
        left = 1
        right = max(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            sum_divisor = sum_div(mid)

            # If sum is within threshold, try smaller divisor
            if sum_divisor <= threshold:
                ans = mid
                right = mid - 1
            else:
                # Need larger divisor to reduce the sum
                left = mid + 1

        return ans


class TestFindSmallestDivisor(unittest.TestCase):
    """Unit tests for the Find Smallest Divisor solution."""

    def test_single_element(self):
        """Case with single element."""
        solution = Solution()
        self.assertEqual(solution.smallestDivisor([1], 1), 1)

    def test_multiple_elements(self):
        """Standard case with multiple elements."""
        solution = Solution()
        self.assertEqual(solution.smallestDivisor([1, 2, 5, 9], 6), 5)

    def test_large_threshold(self):
        """Case where threshold is large enough for divisor of 1."""
        solution = Solution()
        self.assertEqual(solution.smallestDivisor([2, 3, 5, 7, 11], 11), 1)

    def test_small_threshold(self):
        """Case where threshold requires larger divisor."""
        solution = Solution()
        self.assertEqual(solution.smallestDivisor([19], 5), 4)


if __name__ == "__main__":
    unittest.main()
