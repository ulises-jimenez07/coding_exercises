"""
Problem: Determine if a graph of n nodes and edges is a valid tree.

Approach:
- A valid tree must be fully connected and have no cycles.
- A graph with n nodes is a tree if and only if it has exactly n - 1 edges and is connected.
- We check edge count first, then use DFS to check connectivity and cycle detection.
- Time complexity: O(V + E)
- Space complexity: O(V + E)
"""

import unittest
from collections import defaultdict
from typing import List


class Solution:
    """
    Solves the Valid Tree problem using DFS for cycle detection and connectivity check.
    """

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Determines if the given edges form a valid tree with n nodes.
        """
        # A tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list: node -> neighbors
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def has_cycle(node, parent):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                # If neighbor is already visited, we found a cycle
                if neighbor in visited:
                    return True
                if has_cycle(neighbor, node):
                    return True
            return False

        # Start DFS from node 0. If cycle found, checking returns False.
        # Note: With n-1 edges, if there's no cycle AND we visit all nodes, it's a tree.
        if has_cycle(0, -1):
            return False

        # Ensure graph is fully connected (all nodes visited)
        return len(visited) == n


class TestValidTree(unittest.TestCase):
    """
    Unit tests for the Valid Tree solution.
    """

    def test_valid_tree(self):
        sol = Solution()
        # 0-1, 0-2, 0-3, 1-4. 5 nodes, 4 edges. Connected, No Cycle.
        self.assertTrue(sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))

    def test_cycle(self):
        sol = Solution()
        # 0-1-2-3-1 (Cycle 1-2-3-1). 5 nodes, 5 edges -> len check fails immediately?
        # Wait, if edges = [[0,1], [1,2], [2,3], [1,3], [1,4]] -> 5 edges. n=5. len!=n-1.
        # Let's test standard cycle case that passes len check:
        # n=5. Edges must be 4.
        # Disconnected with cycle? e.g. 0 isolated. 1-2-3-1 (3 edges). 4 isolated?
        # Edges: [1,2], [2,3], [3,1], [3,4] -> 4 edges.
        # Cycle 1-2-3. Connected component {1,2,3,4}. Node 0 isolated.
        self.assertFalse(sol.validTree(5, [[1, 2], [2, 3], [3, 1], [3, 4]]))

    def test_disconnected(self):
        sol = Solution()
        # 0-1, 2-3. 4 nodes, 2 edges.
        # Fails length check (2 != 3).
        self.assertFalse(sol.validTree(4, [[0, 1], [2, 3]]))

    def test_disconnected_passing_length(self):
        # Can we have disconnected, n-1 edges, no cycle? Impossible mathematically?
        # n=4, edges=3.
        # Comp A: 3 nodes, 2 edges (Tree). Comp B: 1 node, 0 edges. Total 3 nodes used? No total 4.
        # A tree of 3 nodes has 2 edges. One isolated node. Total edges = 2.
        # To get 3 edges with 4 nodes without cycle, impossible if disconnected?
        # Actually yes: forest with k components has n-k edges.
        # If edges = n-1, then n-k = n-1 => k=1.
        # So it must be connected if acyclic and edges=n-1.
        # So we only need to test connectivity OR cycle if length is correct.
        # But our code checks both just in case or for robustness.
        pass

    def test_simple_cycle(self):
        sol = Solution()
        # 0-1, 1-2, 2-0. 3 nodes. 3 edges. Fails len check.
        self.assertFalse(sol.validTree(3, [[0, 1], [1, 2], [2, 0]]))

    def test_single_node(self):
        sol = Solution()
        self.assertTrue(sol.validTree(1, []))


if __name__ == "__main__":
    unittest.main()
