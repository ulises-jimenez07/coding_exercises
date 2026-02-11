"""
Problem: Clone an undirected graph where each node contains a value and a list of neighbors.

Approach:
- BFS: Use BFS with a hash map to track original-to-clone node mappings.
- DFS: Use recursive DFS with a hash map to handle cycles and child node creation.
- Time complexity: O(N + E) for both where N is nodes and E is edges.
- Space complexity: O(N) for both.
"""

import unittest
from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    """
    Representation of a node in an undirected graph.
    """

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class SolutionBFS:
    """
    A class to clone an undirected graph using BFS.
    """

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        Clones a given undirected graph using Breadth-First Search (BFS).

        Args:
            node: The starting node of the graph to be cloned.

        Returns:
            The starting node of the cloned graph, or None if the input is None.
        """
        if not node:
            return node

        # Use a dictionary 'visited' to map original nodes to their clones.
        visited = {}

        # Initialize a queue for BFS with the starting node.
        queue = deque([node])

        # Create a clone of the starting node and add it to 'visited'.
        visited[node] = Node(node.val, [])

        # Perform BFS
        while queue:
            # Dequeue the current node.
            curr = queue.popleft()

            # Iterate over the neighbors of the current node.
            for neighbor in curr.neighbors:
                # If the neighbor hasn't been visited yet:
                if neighbor not in visited:
                    # Create a clone of the neighbor.
                    visited[neighbor] = Node(neighbor.val, [])
                    # Enqueue the neighbor.
                    queue.append(neighbor)

                # Add the clone of the neighbor to the neighbors list of the clone of the current node.
                visited[curr].neighbors.append(visited[neighbor])

        # Return the clone of the starting node.
        return visited[node]


class SolutionDFS:
    """
    A class to clone an undirected graph using recursive DFS.
    """

    def __init__(self):
        self.cloned_map: dict[Node, Node] = {}

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        Clones a given undirected graph using Depth-First Search (DFS).
        """
        if not node:
            return node

        self.cloned_map = {}
        return self.dfs(node)

    def dfs(self, node):
        """Recursive helper for DFS cloning."""
        if node in self.cloned_map:
            return self.cloned_map[node]

        # Create the clone for the current node
        cloned_node = Node(node.val)
        self.cloned_map[node] = cloned_node

        # Recursively clone all neighbors
        for neighbor in node.neighbors:
            cloned_neighbor = self.dfs(neighbor)
            cloned_node.neighbors.append(cloned_neighbor)

        return cloned_node


class TestCloneGraph(unittest.TestCase):
    """
    Unit tests for both BFS and DFS cloneGraph implementations.
    """

    def test_bfs_implementation(self):
        """Runs all tests using BFS implementation."""
        self._run_all_tests(SolutionBFS())

    def test_dfs_implementation(self):
        """Runs all tests using DFS implementation."""
        self._run_all_tests(SolutionDFS())

    def _run_all_tests(self, sol):
        # 1. Empty Graph
        self.assertIsNone(sol.cloneGraph(None))

        # 2. Single Node
        node1 = Node(1)
        cloned_node = sol.cloneGraph(node1)
        self.assertEqual(cloned_node.val, 1)
        self.assertEqual(len(cloned_node.neighbors), 0)
        self.assertIsNot(cloned_node, node1)

        # 3. Two-node cycle
        node_a = Node(1)
        node_b = Node(2)
        node_a.neighbors.append(node_b)
        node_b.neighbors.append(node_a)

        cloned_a = sol.cloneGraph(node_a)
        self.assertEqual(cloned_a.val, 1)
        self.assertEqual(len(cloned_a.neighbors), 1)
        self.assertEqual(cloned_a.neighbors[0].val, 2)
        self.assertIsNot(cloned_a, node_a)
        self.assertIsNot(cloned_a.neighbors[0], node_b)

        # 4. Complex graph
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n1.neighbors = [n2, n4]
        n2.neighbors = [n1, n3]
        n3.neighbors = [n2, n4]
        n4.neighbors = [n1, n3]

        cloned_g = sol.cloneGraph(n1)
        self.assertEqual(cloned_g.val, 1)
        self.assertEqual(len(cloned_g.neighbors), 2)
        # Check connectivity
        neighbor_vals = {nb.val for nb in cloned_g.neighbors}
        self.assertEqual(neighbor_vals, {2, 4})


if __name__ == "__main__":
    unittest.main()
