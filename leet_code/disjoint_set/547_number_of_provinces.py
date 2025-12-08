"""
Problem: Find the number of connected components (provinces) in a graph
         represented by an adjacency matrix. This is equivalent to counting
         the number of disjoint sets in the graph.

Approach:
- Use the Union-Find (Disjoint Set) data structure.
- The input `isConnected` is an adjacency matrix where `isConnected[i][j] == 1`
  means there is an edge between city `i` and city `j`.
- Iterate through the upper triangular part of the matrix (i < j).
- If cities `i` and `j` are connected (`isConnected[i][j] == 1`) and not
  already in the same component (`uf.find(i) != uf.find(j)`), unite them.
- Start with `n` components and decrement the count every time a successful
  union (connecting two separate components) is performed.
- Time complexity: O(n^2 * α(n)) where n is the number of cities and α is
  the inverse Ackermann function (nearly constant). The O(n^2) factor comes
  from iterating over the adjacency matrix.
- Space complexity: O(n) for the parent map in UnionFind.
"""

import unittest
from typing import List


class Solution:
    """Union-Find approach to count the number of provinces (connected components)."""

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Calculates the number of provinces in a given adjacency matrix.

        A province is a group of directly or indirectly connected cities.

        :param isConnected: An n x n matrix where isConnected[i][j] == 1
                            if city i and city j are directly connected.
        :return: The total number of provinces.
        """
        uf = UnionFind()
        n = len(isConnected)
        # Initially, every city is its own component (province).
        number_of_components = n

        # Iterate through the upper triangular part of the matrix (j > i).
        # We only need to check each connection once.
        for i in range(n):
            for j in range(i + 1, n):
                # If there is a direct connection (edge exists)
                if isConnected[i][j] == 1:
                    # Check if i and j are already in the same component.
                    root_i = uf.find(i)
                    root_j = uf.find(j)

                    if root_i != root_j:
                        # Union them and decrement the component count.
                        number_of_components -= 1
                        uf.union(i, j)

        return number_of_components


class UnionFind:
    """Disjoint set data structure with path compression."""

    def __init__(self):
        """Initializes the parent map."""
        self.parent = {}

    def find(self, x):
        """
        Finds the root of element x with path compression.

        :param x: The element to find the root for.
        :return: The root (representative) of the set containing x.
        """
        # Initialize node if it's the first time seeing it (sets its own parent)
        if x not in self.parent:
            self.parent[x] = x

        # Path compression: if x is not its own root, recursively find the root
        # and set x's parent directly to the final root.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        """
        Unites the components containing x and y.

        Performs a union-by-rank/size optimization is typically added here for
        better performance, but not strictly necessary for this problem.
        This implementation performs a simple union.

        :param x: An element in the first set.
        :param y: An element in the second set.
        """
        root_x, root_y = self.find(x), self.find(y)

        # Only unite if they are in different components
        if root_x != root_y:
            # Simple union: make root_x point to root_y
            self.parent[root_x] = root_y


# -----------------------------------------------------------------------------


class TestFindCircleNum(unittest.TestCase):
    """Test cases for the Solution.findCircleNum method."""

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example_one(self):
        """Test case: [[1,1,0],[1,1,0],[0,0,1]] -> Expected 2 provinces."""
        isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        # (0, 1) are connected, (2) is separate.
        self.assertEqual(self.solution.findCircleNum(isConnected), 2)

    def test_example_two(self):
        """Test case: [[1,0,0],[0,1,0],[0,0,1]] -> Expected 3 provinces."""
        isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        # (0), (1), (2) are all separate.
        self.assertEqual(self.solution.findCircleNum(isConnected), 3)

    def test_fully_connected(self):
        """Test case: Fully connected graph -> Expected 1 province."""
        isConnected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        # (0, 1, 2) are all connected.
        self.assertEqual(self.solution.findCircleNum(isConnected), 1)

    def test_single_node(self):
        """Test case: Single node graph -> Expected 1 province."""
        isConnected = [[1]]
        self.assertEqual(self.solution.findCircleNum(isConnected), 1)

    def test_large_two_components(self):
        """Test case: Two separate components in a larger graph."""
        isConnected = [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
        ]
        # (0, 1) and (2, 3) are connected components.
        self.assertEqual(self.solution.findCircleNum(isConnected), 2)


if __name__ == "__main__":
    unittest.main()
