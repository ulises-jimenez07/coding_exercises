"""
Problem: Largest Rectangle in Histogram - find maximum rectangular area in histogram

Approach:
- Use a monotonic increasing stack to track indices of bars that can form rectangles
- When we find a shorter bar, pop taller bars and calculate their max rectangle areas
- The width extends from the current position back to the previous smaller bar
- Process remaining bars in stack after iterating through all bars
- Time complexity: O(n) where n is the number of bars
- Space complexity: O(n) for the stack
"""

import unittest
from typing import List


class Solution:
    """Solution for LeetCode 84: Largest Rectangle in Histogram."""

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Find the largest rectangular area that can be formed in a histogram.

        Given an array of bar heights, find the largest rectangle that can be formed
        using one or more consecutive bars.
        """
        stack: list[int] = [-1]  # Monotonic increasing stack with sentinel -1
        max_area = 0

        # Process each bar in the histogram
        for curr_bar, bar_height in enumerate(heights):
            # Pop bars taller than current bar and calculate their areas
            while stack[-1] != -1 and heights[stack[-1]] >= bar_height:
                current_height = heights[stack.pop()]  # Height of rectangle
                current_width = curr_bar - stack[-1] - 1  # Width extends to prev smaller bar
                max_area = max(max_area, current_height * current_width)
            stack.append(curr_bar)  # Add current bar index to stack

        # Process remaining bars in stack (these extend to end of histogram)
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)

        return max_area


class TestLargestRectangleArea(unittest.TestCase):
    """Test cases for Largest Rectangle in Histogram solution."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Test with basic example with varying heights."""
        heights = [2, 1, 5, 6, 2, 3]
        expected = 10  # Rectangle with height 5 and width 2
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_increasing_heights(self):
        """Test with strictly increasing heights."""
        heights = [1, 2, 3, 4, 5]
        expected = 9  # Rectangle with height 3 and width 3
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_decreasing_heights(self):
        """Test with strictly decreasing heights."""
        heights = [5, 4, 3, 2, 1]
        expected = 9  # Rectangle with height 3 and width 3
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_all_same_height(self):
        """Test where all bars have the same height."""
        heights = [4, 4, 4, 4]
        expected = 16  # Rectangle spanning all bars
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_single_bar(self):
        """Test with single bar."""
        heights = [5]
        expected = 5
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_two_bars_same_height(self):
        """Test with two bars of same height."""
        heights = [3, 3]
        expected = 6  # Rectangle spanning both bars
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_two_bars_different_height(self):
        """Test with two bars of different heights."""
        heights = [2, 4]
        expected = 4  # Single bar with height 4
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_peak_in_middle(self):
        """Test with peak height in the middle."""
        heights = [1, 2, 5, 2, 1]
        expected = 6  # Rectangle with height 2 and width 3
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_valley_pattern(self):
        """Test with valley pattern (high-low-high)."""
        heights = [5, 1, 5]
        expected = 5  # Either of the tall bars
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_multiple_same_max_areas(self):
        """Test where multiple rectangles can have same max area."""
        heights = [2, 2, 2]
        expected = 6  # Rectangle spanning all bars
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_zero_height(self):
        """Test with zero height bars."""
        heights = [0, 2, 0]
        expected = 2  # Single bar with height 2
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_large_rectangle_at_start(self):
        """Test where largest rectangle is at the start."""
        heights = [6, 5, 4, 1, 1]
        expected = 12  # Rectangle with height 4 and width 3
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)

    def test_large_rectangle_at_end(self):
        """Test where largest rectangle is at the end."""
        heights = [1, 1, 4, 5, 6]
        expected = 12  # Rectangle with height 4 and width 3
        self.assertEqual(self.solution.largestRectangleArea(heights), expected)


if __name__ == "__main__":
    unittest.main()
