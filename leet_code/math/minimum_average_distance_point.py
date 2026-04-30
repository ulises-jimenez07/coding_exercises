"""
Problem: Point with Minimum Average Distance
Find a point that minimizes average Euclidean distance to a set of points.

Approach:
- This is the geometric median problem
- Start from the centroid
- Use gradient descent to move opposite the average distance gradient
- Time complexity: O(iterations * n)
- Space complexity: O(1)
"""

import math
import unittest


def average_distance(point, points):
    """Return the average Euclidean distance from point to all points."""
    return sum(math.dist(point, other_point) for other_point in points) / len(points)


def find_optimal_point(points, learning_rate=0.1, iterations=1000):
    """Return an approximate geometric median for 2D points."""
    if not points:
        raise ValueError("points cannot be empty")

    current_x = sum(point[0] for point in points) / len(points)
    current_y = sum(point[1] for point in points) / len(points)

    for _ in range(iterations):
        gradient_x = 0.0
        gradient_y = 0.0

        for point_x, point_y in points:
            distance = math.sqrt((current_x - point_x) ** 2 + (current_y - point_y) ** 2)
            if distance == 0:
                continue

            gradient_x += (current_x - point_x) / distance
            gradient_y += (current_y - point_y) / distance

        current_x -= learning_rate * (gradient_x / len(points))
        current_y -= learning_rate * (gradient_y / len(points))

    return current_x, current_y


class TestMinimumAverageDistancePoint(unittest.TestCase):
    """Unit tests for find_optimal_point."""

    def test_symmetric_square(self):
        points = [(0.0, 0.0), (0.0, 2.0), (2.0, 0.0), (2.0, 2.0)]
        x, y = find_optimal_point(points)

        self.assertAlmostEqual(x, 1.0)
        self.assertAlmostEqual(y, 1.0)

    def test_single_point(self):
        points = [(3.0, 4.0)]

        self.assertEqual(find_optimal_point(points), (3.0, 4.0))

    def test_identical_points(self):
        points = [(5.0, 7.0), (5.0, 7.0), (5.0, 7.0)]

        self.assertEqual(find_optimal_point(points), (5.0, 7.0))

    def test_optimal_point_improves_centroid_for_outlier(self):
        points = [(0.0, 0.0), (0.0, 1.0), (100.0, 0.0)]
        centroid = (
            sum(point[0] for point in points) / len(points),
            sum(point[1] for point in points) / len(points),
        )
        optimal = find_optimal_point(points, learning_rate=0.2, iterations=2000)

        self.assertLess(average_distance(optimal, points), average_distance(centroid, points))

    def test_empty_points(self):
        with self.assertRaises(ValueError):
            find_optimal_point([])


if __name__ == "__main__":
    unittest.main()
