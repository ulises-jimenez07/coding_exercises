"""
Problem: Check if an array is a valid mountain array (strict increase then decrease)

Approach:
- Walk up while increasing, then walk down while decreasing
- Peak must not be at first or last position
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        """Checks if an array is a valid mountain array."""
        n = len(A)
        if n < 3:
            return False

        i = 1

        # Walk up
        while i < n and A[i] > A[i - 1]:
            i += 1

        # Peak can't be first or last
        if i == 1 or i == n:
            return False

        # Walk down
        while i < n and A[i] < A[i - 1]:
            i += 1

        return i == n


class TestValidMountainArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_mountain(self):
        """Valid mountain."""
        self.assertTrue(self.solution.validMountainArray([0, 3, 2, 1]))

    def test_not_mountain_increasing(self):
        """Not a mountain - increasing."""
        self.assertFalse(self.solution.validMountainArray([0, 1, 2, 3, 4]))

    def test_not_mountain_decreasing(self):
        """Not a mountain - decreasing."""
        self.assertFalse(self.solution.validMountainArray([4, 3, 2, 1, 0]))

    def test_valid_mountain_longer(self):
        """Valid mountain - longer."""
        self.assertTrue(self.solution.validMountainArray([0, 1, 2, 3, 4, 3, 2, 1]))

    def test_not_mountain_plateau(self):
        """Not a mountain - plateau."""
        self.assertFalse(self.solution.validMountainArray([0, 1, 2, 3, 3, 2, 1]))

    def test_too_short(self):
        """Too short."""
        self.assertFalse(self.solution.validMountainArray([0, 1]))

    def test_single_element(self):
        """Single element."""
        self.assertFalse(self.solution.validMountainArray([1]))


if __name__ == "__main__":
    unittest.main()
