"""
Problem: Clone an undirected graph where each node contains a value and a list of neighbors.

Approach:
- Use BFS with a hash map to track original-to-clone node mappings
- Create clone nodes and connect neighbors during traversal
- Time complexity: O(N + E) where N is nodes and E is edges
- Space complexity: O(N) for the hash map and queue
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


import unittest  # Import unittest for testing
from collections import deque
from typing import Optional


class Solution:
    """
    A class to clone an undirected graph.
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


class TestCloneGraph(unittest.TestCase):
    """
    Unit tests for the Solution.cloneGraph method.
    """

    def setUp(self):
        self.sol = Solution()

    def test_empty_graph(self):
        self.assertIsNone(self.sol.cloneGraph(None))

    def test_single_node_graph(self):
        node1 = Node(1)
        cloned_node = self.sol.cloneGraph(node1)
        self.assertEqual(cloned_node.val, 1)
        self.assertEqual(len(cloned_node.neighbors), 0)

    def test_two_node_graph(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

        cloned_node = self.sol.cloneGraph(node1)

        self.assertEqual(cloned_node.val, 1)
        self.assertEqual(len(cloned_node.neighbors), 1)
        self.assertEqual(cloned_node.neighbors[0].val, 2)

        cloned_neighbor = cloned_node.neighbors[0]
        self.assertEqual(len(cloned_neighbor.neighbors), 1)
        self.assertEqual(cloned_neighbor.neighbors[0].val, 1)
        self.assertIsNot(cloned_neighbor.neighbors[0], node1)  # Ensure deep copy

    def test_complex_graph(self):
        # Construct a more complex graph for testing.
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]

        cloned_graph = self.sol.cloneGraph(node1)

        self.assertEqual(cloned_graph.val, 1)
        self.assertEqual(len(cloned_graph.neighbors), 2)


if __name__ == "__main__":
    unittest.main()
