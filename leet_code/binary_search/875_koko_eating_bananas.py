"""
Problem: Find minimum eating speed to finish all banana piles within h hours

Approach:
- Binary search on eating speed (1 to max pile size)
- For each speed, calculate total hours needed
- Time complexity: O(n log m) where m is max pile size
- Space complexity: O(1)
"""

import math
import unittest
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        ans = end

        while start <= end:
            mid = (start + end) // 2
            if self.count_hours(piles, mid) > h:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1

        return ans

    def count_hours(self, piles: List[int], speed: int) -> int:
        # Calculate total hours at given eating speed
        return sum(math.ceil(pile / speed) for pile in piles)


class TestMinEatingSpeed(unittest.TestCase):
    """
    Unit tests for the minEatingSpeed method.
    """

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        """Test with a standard example from LeetCode."""
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(self.sol.minEatingSpeed(piles, h), 4)

    def test_example_2(self):
        """Test with a different example."""
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(self.sol.minEatingSpeed(piles, h), 30)

    def test_example_3(self):
        """Test with an example where the speed is 1."""
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(self.sol.minEatingSpeed(piles, h), 23)

    def test_single_pile(self):
        """Test with a single pile."""
        piles = [10]
        h = 3
        self.assertEqual(self.sol.minEatingSpeed(piles, h), 4)

    def test_large_numbers(self):
        """Test with large numbers in piles and hours."""
        piles = [1000000000]
        h = 2
        self.assertEqual(self.sol.minEatingSpeed(piles, h), 500000000)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
