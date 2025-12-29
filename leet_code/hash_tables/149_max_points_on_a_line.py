"""
Problem: Given an array of points where points[i] = [xi, yi], return the maximum number of points that lie on the same straight line.

Approach:
- For each point, calculate the slope with every other point.
- Points with the same slope from a fixed point lie on the same line.
- Use a hash table to count frequencies of slopes for each point.
- Represent slopes as a reduced fraction (dy, dx) using GCD to avoid floating-point precision issues.
- Time complexity: O(n^2)
- Space complexity: O(n)
"""

import math
import unittest
from typing import List


class Solution:
    """Solution for finding maximum points on a line."""

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        def get_gcd(a, b):
            return math.gcd(a, b)

        max_points = 1
        for i in range(n):
            slopes: dict[tuple[int, int], int] = {}
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                # Reduce to simplest fraction and normalize sign
                g = get_gcd(dx, dy)
                dx //= g
                dy //= g

                # Normalize: ensure first non-zero component is positive
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy

                slope = (dx, dy)
                slopes[slope] = slopes.get(slope, 0) + 1

            # Max for current point i is (most points on a slope + 1 for point i itself)
            if slopes:
                max_points = max(max_points, max(slopes.values()) + 1)

        return max_points


class TestMaxPoints(unittest.TestCase):
    """Unit tests for the maxPoints solution."""

    def setUp(self):
        """Set up the Solution instance."""
        self.solution = Solution()

    def test_example_1(self):
        """Test example 1 from LeetCode."""
        points = [[1, 1], [2, 2], [3, 3]]
        self.assertEqual(self.solution.maxPoints(points), 3)

    def test_example_2(self):
        """Test example 2 from LeetCode."""
        points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
        self.assertEqual(self.solution.maxPoints(points), 4)

    def test_single_point(self):
        """Test with a single point."""
        points = [[1, 1]]
        self.assertEqual(self.solution.maxPoints(points), 1)

    def test_two_points(self):
        """Test with two points."""
        points = [[1, 1], [2, 2]]
        self.assertEqual(self.solution.maxPoints(points), 2)

    def test_vertical_line(self):
        """Test with points forming a vertical line."""
        points = [[1, 1], [1, 2], [1, 3]]
        self.assertEqual(self.solution.maxPoints(points), 3)

    def test_horizontal_line(self):
        """Test with points forming a horizontal line."""
        points = [[1, 1], [2, 1], [3, 1]]
        self.assertEqual(self.solution.maxPoints(points), 3)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
