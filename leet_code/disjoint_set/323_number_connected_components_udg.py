"""
Problem: Count number of connected components in undirected graph

Approach:
- Use Union-Find (Disjoint Set) data structure
- Unite connected nodes through edges
- Count unique root parents for all nodes
- Time complexity: O(E * α(n)) where α is inverse Ackermann function
- Space complexity: O(n) for parent map
"""

import unittest
from typing import List


class Solution:
    """Union-Find approach to count connected components."""

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()

        # Unite all connected nodes
        for a, b in edges:
            uf.union(a, b)

        # Count unique roots (each root represents one component)
        return len(set(uf.find(i) for i in range(n)))


class UnionFind:
    """Disjoint set data structure with path compression."""

    def __init__(self):
        self.parent = {}

    def find(self, x):
        """Find root of x with path compression."""
        # Initialize node if not seen
        if x not in self.parent:
            self.parent[x] = x

        # Path compression: point directly to root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        """Unite two components by connecting their roots."""
        root_x, root_y = self.find(x), self.find(y)

        # Connect roots if in different components
        if root_x != root_y:
            self.parent[root_x] = root_y


# -----------------------------------------------------------------------------


class TestCountComponents(unittest.TestCase):
    """Test cases for counting connected components."""

    def setUp(self):
        self.solution = Solution()

    def test_single_component(self):
        """All nodes connected in one component."""
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.solution.countComponents(n, edges), 1)

    def test_multiple_components(self):
        """Multiple separate components."""
        n = 5
        edges = [[0, 1], [2, 3]]
        self.assertEqual(self.solution.countComponents(n, edges), 3)

    def test_no_edges(self):
        """No edges means all nodes are separate components."""
        n = 4
        edges = []
        self.assertEqual(self.solution.countComponents(n, edges), 4)

    def test_fully_connected(self):
        """Complete graph forms one component."""
        n = 3
        edges = [[0, 1], [0, 2], [1, 2]]
        self.assertEqual(self.solution.countComponents(n, edges), 1)

    def test_single_node(self):
        """Single node with no edges."""
        n = 1
        edges = []
        self.assertEqual(self.solution.countComponents(n, edges), 1)

    def test_two_equal_components(self):
        """Two components with same size."""
        n = 6
        edges = [[0, 1], [1, 2], [3, 4], [4, 5]]
        self.assertEqual(self.solution.countComponents(n, edges), 2)


if __name__ == "__main__":
    unittest.main()
