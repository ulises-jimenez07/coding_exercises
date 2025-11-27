"""
Problem: Trapping Rain Water - calculate how much water can be trapped after raining

Approach:
- Use a monotonic decreasing stack to track indices of bars
- When we find a taller bar, calculate water trapped between it and previous taller bar
- Water fills the depression between two boundaries (left and right taller bars)
- Width is the distance between boundaries, height is bounded by the shorter boundary
- Time complexity: O(n) where n is the number of bars
- Space complexity: O(n) for the stack
"""

import unittest
from typing import List


class Solution:
    """Solution for LeetCode 42: Trapping Rain Water."""

    def trap(self, height: List[int]) -> int:
        """
        Calculate total amount of water that can be trapped after raining.

        Given elevation map represented by array, compute how much water can be trapped.
        Water accumulates in depressions between higher bars.
        """
        ans = 0
        stack: list[int] = []  # Monotonic decreasing stack storing indices

        # Process each bar
        for curr_bar, curr_bar_height in enumerate(height):
            # Current bar is taller - water can be trapped
            while stack and curr_bar_height > height[stack[-1]]:
                prev_bar = stack.pop()  # Bottom of the depression
                if not stack:
                    break  # No left boundary

                # Calculate water trapped in this layer
                distance = curr_bar - stack[-1] - 1  # Width of depression
                bounded_height = min(curr_bar_height, height[stack[-1]]) - height[prev_bar]
                ans += distance * bounded_height

            stack.append(curr_bar)  # Add current bar to stack

        return ans


class TestTrappingRainWater(unittest.TestCase):
    """Test cases for Trapping Rain Water solution."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Test with basic example with trapped water."""
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        self.assertEqual(self.solution.trap(height), expected)

    def test_simple_valley(self):
        """Test with simple valley pattern."""
        height = [4, 2, 0, 3, 2, 5]
        expected = 9
        self.assertEqual(self.solution.trap(height), expected)

    def test_no_water_trapped(self):
        """Test with increasing heights - no water trapped."""
        height = [1, 2, 3, 4, 5]
        expected = 0
        self.assertEqual(self.solution.trap(height), expected)

    def test_decreasing_heights(self):
        """Test with decreasing heights - no water trapped."""
        height = [5, 4, 3, 2, 1]
        expected = 0
        self.assertEqual(self.solution.trap(height), expected)

    def test_single_bar(self):
        """Test with single bar - no water can be trapped."""
        height = [5]
        expected = 0
        self.assertEqual(self.solution.trap(height), expected)

    def test_two_bars(self):
        """Test with two bars - no water trapped."""
        height = [3, 5]
        expected = 0
        self.assertEqual(self.solution.trap(height), expected)

    def test_three_bars_valley(self):
        """Test with three bars forming valley."""
        height = [3, 0, 3]
        expected = 3
        self.assertEqual(self.solution.trap(height), expected)

    def test_multiple_valleys(self):
        """Test with multiple valleys."""
        height = [3, 0, 2, 0, 4]
        expected = 7
        self.assertEqual(self.solution.trap(height), expected)

    def test_flat_terrain(self):
        """Test with flat terrain - no water trapped."""
        height = [2, 2, 2, 2]
        expected = 0
        self.assertEqual(self.solution.trap(height), expected)

    def test_deep_single_depression(self):
        """Test with deep single depression."""
        height = [5, 1, 5]
        expected = 4
        self.assertEqual(self.solution.trap(height), expected)

    def test_asymmetric_boundaries(self):
        """Test with asymmetric left and right boundaries."""
        height = [5, 2, 1, 2, 1, 3]
        expected = 6
        self.assertEqual(self.solution.trap(height), expected)

    def test_stepped_valley(self):
        """Test with stepped valley pattern."""
        height = [4, 3, 2, 1, 2, 3, 4]
        expected = 9
        self.assertEqual(self.solution.trap(height), expected)

    def test_empty_array(self):
        """Test with empty array."""
        height = []
        expected = 0
        self.assertEqual(self.solution.trap(height), expected)

    def test_all_zeros(self):
        """Test with all zero heights."""
        height = [0, 0, 0, 0]
        expected = 0
        self.assertEqual(self.solution.trap(height), expected)

    def test_peak_in_middle(self):
        """Test with peak in middle - water on both sides."""
        height = [1, 0, 5, 0, 1]
        expected = 2  # 1 unit left of peak, 1 unit right of peak
        self.assertEqual(self.solution.trap(height), expected)


if __name__ == "__main__":
    unittest.main()
