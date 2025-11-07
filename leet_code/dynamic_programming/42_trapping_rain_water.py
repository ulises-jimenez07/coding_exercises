"""
Problem: Calculate how much rainwater can be trapped between elevation bars.

Approach:
- Use dynamic programming to precompute max heights
- For each position, water level = min(max_left, max_right)
- Water trapped = water_level - current_height
- Build left_max and right_max arrays in two passes
- Time complexity: O(n) three passes through array
- Space complexity: O(n) for two auxiliary arrays

Example: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6 units of water trapped
"""

import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n
        trapped_water = 0

        # Build left_max: highest bar to the left of each position
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        # Build right_max: highest bar to the right of each position
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        # Calculate trapped water at each position
        for i in range(n):
            trapped_water += min(right_max[i], left_max[i]) - height[i]

        return trapped_water


class TestTrap(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_input(self):
        """Test with an empty elevation map."""
        self.assertEqual(self.solution.trap([]), 0)

    def test_single_bar(self):
        """Test with a single bar."""
        self.assertEqual(self.solution.trap([5]), 0)

    def test_two_bars(self):
        """Test with two bars."""
        self.assertEqual(self.solution.trap([5, 2]), 0)

    def test_simple_case(self):
        """Test with a simple elevation map."""
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_all_same_height(self):
        """Test with all bars having the same height."""
        self.assertEqual(self.solution.trap([5, 5, 5, 5, 5]), 0)

    def test_increasing_height(self):
        """Test with increasing bar heights."""
        self.assertEqual(self.solution.trap([1, 2, 3, 4, 5]), 0)

    def test_decreasing_height(self):
        """Test with decreasing bar heights."""
        self.assertEqual(self.solution.trap([5, 4, 3, 2, 1]), 0)

    def test_leetcode_example_1(self):
        """Test case from LeetCode example 1."""
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_leetcode_example_2(self):
        """Test case from LeetCode example 2."""
        self.assertEqual(self.solution.trap([4, 2, 0, 3, 2, 5]), 9)


if __name__ == "__main__":
    unittest.main()
