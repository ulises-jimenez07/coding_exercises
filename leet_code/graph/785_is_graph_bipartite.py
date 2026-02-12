"""
Problem: Check if a graph is bipartite. A graph is bipartite if we can split its nodes into two
independent sets such that every edge connects a node in one set to a node in the other.

Approach:
- DFS: Use recursive DFS to color nodes with two colors (1 and -1).
- If we encounter a node that is already colored with the same color as the current node's neighbor,
  the graph is not bipartite.
- Time complexity: O(V + E) where V is the number of nodes and E is the number of edges.
- Space complexity: O(V) to store the colors and recursion stack.
"""

import unittest
from typing import List


class Solution:
    """
    A class to determine if a graph is bipartite using DFS coloring.
    """

    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Determines if the graph is bipartite.
        """
        # pylint: disable=attribute-defined-outside-init
        self.colors = [0] * len(graph)
        self.graph = graph

        # Iterate through each node to handle disconnected components.
        for i, color in enumerate(self.colors):
            # If the node is not yet colored, start a DFS from it.
            if color == 0 and not self.dfs(i, 1):
                return False

        return True

    def dfs(self, node: int, color: int) -> bool:
        """
        Recursive helper to color nodes and detect bipartition conflicts.
        """
        # Color the current node.
        self.colors[node] = color

        # Visit all neighbors of the current node.
        for neighbor in self.graph[node]:
            # If a neighbor has the same color, the graph is not bipartite.
            if self.colors[neighbor] == color:
                return False
            # If the neighbor is uncolored, color it with the opposite color.
            if self.colors[neighbor] == 0 and not self.dfs(neighbor, -color):
                return False

        return True


class TestIsGraphBipartite(unittest.TestCase):
    """
    Unit tests for the isBipartite implementation.
    """

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        """LeetCode Example 1: Non-bipartite graph."""
        graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        self.assertFalse(self.sol.isBipartite(graph))

    def test_example_2(self):
        """LeetCode Example 2: Bipartite graph."""
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        self.assertTrue(self.sol.isBipartite(graph))

    def test_empty_graph(self):
        """Edge Case: Empty graph."""
        graph = []
        self.assertTrue(self.sol.isBipartite(graph))

    def test_single_node(self):
        """Edge Case: Single node."""
        graph = [[]]
        self.assertTrue(self.sol.isBipartite(graph))

    def test_disconnected_bipartite(self):
        """Disconnected components that are bipartite."""
        graph = [[1], [0], [3], [2]]
        self.assertTrue(self.sol.isBipartite(graph))


if __name__ == "__main__":
    unittest.main()
