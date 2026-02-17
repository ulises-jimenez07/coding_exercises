"""
Problem: Find the minimum cost to connect all points in a 2D plane.
The cost between two points is the Manhattan distance.

Approach:
- Use Kruskal's algorithm to find the Minimum Spanning Tree (MST)
- Calculate Manhattan distance between all pairs of points as edges
- Sort edges by weight and add them to the MST using Union-Find to avoid cycles
- Time complexity: O(E log E) where E is the number of edges O(n^2)
- Space complexity: O(E) for storing edges
"""

import unittest
from typing import List


class UnionFind:
    """
    Standard Union-Find data structure with path compression and union by size.
    """

    def __init__(self, size: int):
        """Initialize each point as its own parent with size 1."""
        self.parent = list(range(size))
        self.size = [1] * size

    def union(self, x: int, y: int) -> bool:
        """Merge components containing x and y. Returns True if successful."""
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            # Union by size to keep the tree flat
            if self.size[rep_x] > self.size[rep_y]:
                self.parent[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]
            else:
                self.parent[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_x]
            return True
        return False

    def find(self, x: int) -> int:
        """Find the root of the component containing x with path compression."""
        if x == self.parent[x]:
            return x
        # Path compression happens here
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution:
    """
    A class to solve the 'Min Cost to Connect All Points' problem.
    """

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Calculate the total minimum Manhattan distance to connect all points."""
        n = len(points)
        if n <= 1:
            return 0

        edges = []
        # Calculate Manhattan distance for all possible pairs
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, n):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edges.append((cost, i, j))

        # Sort edges by weight to apply Kruskal's algorithm
        edges.sort()
        uf = UnionFind(n)
        total_cost = 0
        edges_added = 0

        # Build the MST by greedily adding non-cycle edges
        for cost, p1, p2 in edges:
            if uf.union(p1, p2):
                total_cost += cost
                edges_added += 1
                # Optimization: MST has exactly n-1 edges
                if edges_added == n - 1:
                    break

        return total_cost


# -----------------------------------------------------------------------------


class TestMinCostConnectPoints(unittest.TestCase):
    """
    Unit tests for the Solution class's minCostConnectPoints method.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test with basic five points example."""
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        expected = 20
        self.assertEqual(self.solution.minCostConnectPoints(points), expected)

    def test_example_2(self):
        """Test with three points involving negative coordinates."""
        points = [[3, 12], [-2, 5], [-4, 1]]
        expected = 18
        self.assertEqual(self.solution.minCostConnectPoints(points), expected)

    def test_single_point(self):
        """Test case with only one point (cost should be 0)."""
        points = [[0, 0]]
        expected = 0
        self.assertEqual(self.solution.minCostConnectPoints(points), expected)

    def test_empty_input(self):
        """Test case with an empty list of points."""
        points = []
        expected = 0
        self.assertEqual(self.solution.minCostConnectPoints(points), expected)

    def test_two_points(self):
        """Test case with exactly two points."""
        points = [[0, 0], [1, 1]]
        expected = 2
        self.assertEqual(self.solution.minCostConnectPoints(points), expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
