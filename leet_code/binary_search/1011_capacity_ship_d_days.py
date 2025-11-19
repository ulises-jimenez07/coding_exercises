"""
Problem: Capacity To Ship Packages Within D Days

Approach:
- Binary search on the capacity range
- Minimum capacity is max(weights), maximum is sum(weights)
- For each mid capacity, check if we can ship within days
- Time complexity: O(n * log(sum of weights))
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Solution class for ship capacity problem."""

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        ans = end

        while start <= end:
            mid = (start + end) // 2
            if self.is_possible(weights, mid, days):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans

    def is_possible(self, weights, capacity, days):
        """Check if we can ship all packages with given capacity in days."""
        days_needed = 1
        current_load = 0

        for weight in weights:
            current_load += weight
            if current_load > capacity:
                days_needed += 1
                current_load = weight

        return days_needed <= days


# --- Unit Tests ---


class TestShipCapacity(unittest.TestCase):
    """
    Unit tests for the shipWithinDays method in the Solution class.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        self.assertEqual(
            self.solution.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
            15,
            "Should return capacity 15 for 5 days",
        )

    def test_example_two(self):
        self.assertEqual(
            self.solution.shipWithinDays([3, 2, 2, 4, 1, 4], 3),
            6,
            "Should return capacity 6 for 3 days",
        )

    def test_one_day(self):
        self.assertEqual(
            self.solution.shipWithinDays([1, 2, 3, 4, 5], 1),
            15,
            "Should return sum of all weights when days is 1",
        )

    def test_days_equal_packages(self):
        self.assertEqual(
            self.solution.shipWithinDays([1, 2, 3, 4, 5], 5),
            5,
            "Should return max weight when days equals package count",
        )

    def test_single_package(self):
        self.assertEqual(
            self.solution.shipWithinDays([10], 1),
            10,
            "Should return the weight for single package",
        )

    def test_all_same_weight(self):
        self.assertEqual(
            self.solution.shipWithinDays([5, 5, 5, 5], 2),
            10,
            "Should handle packages with same weight",
        )


# Standard boilerplate to run the tests when the script is executed
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
