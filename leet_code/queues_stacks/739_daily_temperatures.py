"""
Problem: Daily Temperatures - find number of days until warmer temperature

Approach:
- Use a monotonic decreasing stack to track indices of days without warmer future days
- For each day, pop all previous days that are colder and calculate the wait time
- Store indices in stack to calculate the difference in days
- Time complexity: O(n) where n is the number of temperatures
- Space complexity: O(n) for the stack and result array
"""

import unittest
from typing import List


class Solution:
    """Solution for LeetCode 739: Daily Temperatures."""

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Find the number of days until a warmer temperature for each day.

        For each day, determine how many days you have to wait until a warmer temperature.
        If there is no future day with a warmer temperature, the answer is 0.
        """
        n = len(temperatures)
        ans = [0] * n  # Initialize result with zeros (no warmer day by default)
        stack: list[int] = []  # Monotonic decreasing stack storing indices

        # Process each day
        for curr_day, curr_temp in enumerate(temperatures):
            # Current temperature is warmer than previous days in stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day  # Calculate days to wait

            stack.append(curr_day)  # Add current day to stack

        return ans


class TestDailyTemperatures(unittest.TestCase):
    """Test cases for Daily Temperatures solution."""

    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Test with basic example with mixed temperatures."""
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_increasing_temperatures(self):
        """Test with strictly increasing temperatures."""
        temperatures = [30, 40, 50, 60]
        expected = [1, 1, 1, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_decreasing_temperatures(self):
        """Test with strictly decreasing temperatures - no warmer days ahead."""
        temperatures = [60, 50, 40, 30]
        expected = [0, 0, 0, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_single_day(self):
        """Test with single day - no future days."""
        temperatures = [30]
        expected = [0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_all_same_temperature(self):
        """Test where all temperatures are the same."""
        temperatures = [30, 30, 30, 30]
        expected = [0, 0, 0, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_one_peak_at_end(self):
        """Test where warmest day is at the end."""
        temperatures = [30, 40, 35, 45]
        expected = [1, 2, 1, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_one_peak_in_middle(self):
        """Test with peak temperature in the middle."""
        temperatures = [30, 50, 40, 35]
        expected = [1, 0, 0, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_multiple_same_temps_with_warmer(self):
        """Test with multiple same temperatures followed by warmer day."""
        temperatures = [30, 30, 30, 40]
        expected = [3, 2, 1, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_alternating_temps(self):
        """Test with alternating high and low temperatures."""
        temperatures = [40, 30, 50, 35, 60]
        expected = [2, 1, 2, 1, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_long_wait(self):
        """Test where some days have long wait until warmer temperature."""
        temperatures = [30, 29, 28, 27, 26, 100]
        expected = [5, 4, 3, 2, 1, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)


if __name__ == "__main__":
    unittest.main()
