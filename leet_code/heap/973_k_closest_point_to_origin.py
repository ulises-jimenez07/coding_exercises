"""
Problem: Find the k closest points to the origin (0, 0)

Approach:
- Use a max heap of size k to track the k closest points
- Keep heap size at k by removing the farthest point when exceeding
- Time complexity: O(n log k) where n is the number of points
- Space complexity: O(k) for the heap
"""

import heapq
import math
import unittest
from typing import List


class Solution:
    """Provides a method to find the k closest points to the origin."""

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Returns the k closest points to the origin (0, 0).
        """
        if not points or k <= 0:
            return []

        def distance_to_zero(point: List[int]) -> float:
            """Calculates Euclidean distance to the origin."""
            return math.sqrt(point[0] ** 2 + point[1] ** 2)

        heap: list[tuple[float, List[int]]] = []

        for point in points:
            distance = distance_to_zero(point)
            # Use negative distance for max heap simulation
            heapq.heappush(heap, (-distance, point))
            if len(heap) > k:
                heapq.heappop(heap)

        # Return only the points from the heap
        return [item[1] for item in heap]


class TestKClosest(unittest.TestCase):
    """Test cases for the kClosest method."""

    def setUp(self):
        """Initializes the Solution object before each test."""
        self.solution = Solution()

    def test_empty_list(self):
        """Tests with an empty list of points."""
        self.assertEqual(self.solution.kClosest([], 1), [])

    def test_k_zero_or_negative(self):
        """Tests with k equal to 0 or negative."""
        self.assertEqual(self.solution.kClosest([[1, 2]], 0), [])
        self.assertEqual(self.solution.kClosest([[1, 2]], -1), [])

    def test_k_larger_than_list_size(self):
        """Tests when k is larger than the number of points."""
        points = [[1, 3], [-2, 2]]
        self.assertCountEqual(self.solution.kClosest(points, 5), [[-2, 2], [1, 3]])

    def test_basic_example_one(self):
        """Tests the first basic LeetCode example."""
        points = [[1, 3], [-2, 2]]
        k = 1
        self.assertEqual(self.solution.kClosest(points, k), [[-2, 2]])

    def test_basic_example_two(self):
        """Tests the second basic LeetCode example."""
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        self.assertCountEqual(self.solution.kClosest(points, k), [[3, 3], [-2, 4]])

    def test_duplicate_points(self):
        """Tests with duplicate points."""
        points = [[1, 1], [1, 1], [2, 2]]
        k = 2
        self.assertCountEqual(self.solution.kClosest(points, k), [[1, 1], [1, 1]])

    def test_points_on_origin(self):
        """Tests with points exactly on the origin."""
        points = [[0, 0], [1, 1], [0, 0]]
        k = 2
        self.assertCountEqual(self.solution.kClosest(points, k), [[0, 0], [0, 0]])


if __name__ == "__main__":
    unittest.main()
