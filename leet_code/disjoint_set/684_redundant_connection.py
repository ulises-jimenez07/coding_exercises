"""
Problem: In a graph that was originally a tree with N nodes and N-1 edges, one
         additional edge is added, creating a cycle. Find this redundant edge.

Approach:
- Use the Union-Find (Disjoint Set) data structure to keep track of connected components.
- Iterate through the given list of edges sequentially.
- For each edge (u, v):
    - Use `uf.find(u)` and `uf.find(v)` to determine if nodes u and v are already connected.
    - If `find(u) == find(v)`, adding the edge (u, v) would create a cycle. Since the
      problem guarantees only one such edge, this is the redundant connection. Return it.
    - If `find(u) != find(v)`, they belong to different components. Perform `uf.union(u, v)`.
- The UnionFind's `union` method is modified to return `True` if a cycle is detected
  (meaning the two elements are already in the same set).

- Time complexity: O(N * α(N)), where N is the number of nodes/edges and α is
  the inverse Ackermann function (nearly constant).
- Space complexity: O(N) for the UnionFind parent map.
"""

import unittest
from typing import List


class Solution:
    """Union-Find approach to find the single redundant connection in a graph."""

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Finds the edge that, when added to a tree, creates a cycle.
        """
        n_edges = len(edges)
        # The number of nodes is implicitly at most n_edges + 1. Since UnionFind
        # initializes nodes lazily, the initial count can be arbitrary or just 0,
        # but matching the number of edges is fine for node indexing logic (1-based).
        # Note: The problem often uses 1-based indexing for nodes.
        uf = UnionFind(n_edges)

        # Iterate through edges and check for cycle creation
        for edge in edges:
            # The union operation returns True if the two nodes are already
            # connected (i.e., they share the same root), which means adding
            # this edge closes a cycle.
            if uf.union(edge[0], edge[1]):
                return edge

        # Should not be reached based on problem constraints (a redundant edge always exists)
        return []


class UnionFind:
    """Disjoint set data structure with path compression. Optimized for cycle detection."""

    def __init__(self, initial_count):
        """
        Initializes the parent map. The initial_count is only relevant for counting components,
        which is not used here, but kept for consistency with previous examples.
        """
        # The parent map stores the parent of each element.
        self.parent = {}
        # count is not strictly necessary for this specific problem but is kept.
        self.count = initial_count

    def find(self, x):
        """
        Finds the root of element x with path compression.
        """
        # Initialize node if not seen (handles 1-based node indexing)
        if x not in self.parent:
            self.parent[x] = x

        # Path compression: recursively find the root and set x's parent directly to it
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        """
        Unites the components containing x and y. Returns True if a cycle is detected.

        Returns:
            bool: True if x and y were already in the same set (cycle detected), False otherwise.
        """
        root_x, root_y = self.find(x), self.find(y)

        # If roots are the same, the nodes are already connected: a cycle is formed.
        if root_x == root_y:
            return True

        # If roots are different, merge the two components.
        self.parent[root_x] = root_y
        # Note: self.count could be decremented here if we were tracking components.
        return False


# -----------------------------------------------------------------------------


class TestFindRedundantConnection(unittest.TestCase):
    """Test cases for the Solution.findRedundantConnection method."""

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example_one(self):
        """Test case: Redundant edge (3, 4)."""
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        # The edges (1, 2), (2, 3), (3, 4) connect 1-4. Edge [1, 4] completes the cycle.
        self.assertEqual(self.solution.findRedundantConnection(edges), [1, 4])

    def test_example_two(self):
        """Test case: Redundant edge (1, 3)."""
        edges = [[1, 2], [1, 3], [2, 3]]
        # (1, 2) connects them. (1, 3) connects them. Edge [2, 3] completes the cycle.
        self.assertEqual(self.solution.findRedundantConnection(edges), [2, 3])

    def test_linear_graph(self):
        """Test case: Redundant edge at the end of a long chain."""
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]
        # The first four edges form a chain. Edge [5, 1] closes the loop.
        self.assertEqual(self.solution.findRedundantConnection(edges), [5, 1])

    def test_triangle_cycle_first(self):
        """Test case: Redundant edge forms a cycle immediately."""
        edges = [[1, 2], [3, 4], [4, 1], [2, 3]]
        # (1, 2), (3, 4) are separate. [4, 1] connects them. [2, 3] closes the loop.
        self.assertEqual(self.solution.findRedundantConnection(edges), [2, 3])

    def test_tree_then_cycle(self):
        """Test case: Standard tree structure before cycle."""
        edges = [[1, 2], [2, 3], [3, 1]]
        # (1, 2) unioned. (2, 3) unioned. [3, 1] closes the loop.
        self.assertEqual(self.solution.findRedundantConnection(edges), [3, 1])


if __name__ == "__main__":
    unittest.main()
