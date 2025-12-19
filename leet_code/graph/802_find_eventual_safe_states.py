"""
Problem: Find all "safe" nodes in a directed graph. A node is safe if every path starting from it leads to a terminal node (no cycles).

Approach:
- Use DFS with 3-color state tracking (UNVISITED, UNSAFE/VISITING, SAFE/VISITED).
- A node is unsafe if it is part of a cycle or leads to a cycle.
- Marking nodes:
    - 0 (UNVISITED): Not processed yet.
    - 1 (VISITING): Currently exploring or confirmed part of a cycle/unsafe path.
    - 2 (VISITED): Confirmed safe (all paths lead to terminal nodes).
- Time complexity: O(V + E)
- Space complexity: O(V)
"""

import unittest
from typing import List


class Solution:
    """
    Solves Evenual Safe States using DFS cycle detection.
    """

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Returns a sorted list of all safe nodes in the graph.
        """
        n = len(graph)
        state = [0] * n
        UNVISITED, VISITING, VISITED = 0, 1, 2

        def has_cycle(node):
            # If node is currently being visited, we found a back-edge (cycle)
            if state[node] == VISITING:
                return True
            # If node is already marked safe, no cycle here
            if state[node] == VISITED:
                return False

            # Mark as visiting (potentially unsafe)
            state[node] = VISITING
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True

            # If no cycle found in any path, mark as safe
            state[node] = VISITED
            return False

        for i in range(n):
            if state[i] == UNVISITED:
                has_cycle(i)

        # Collect all nodes marked as safe (VISITED)
        return [i for i in range(n) if state[i] == VISITED]


class TestEventualSafeNodes(unittest.TestCase):
    """
    Unit tests for Find Eventual Safe States.
    """

    def test_example_1(self):
        # Graph: 0->1, 0->2, 1->2, 1->3, 2->5, 3->0, 4->5, 5->(terminal)
        # Cycle: 0->1->3->0. Nodes 0, 1, 3 are unsafe.
        # Node 2->5 (safe). Node 4->5 (safe). Node 5 (safe). Node 6 (isolated safe).
        sol = Solution()
        graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
        # Expected safe nodes: 2, 4, 5, 6
        self.assertEqual(sol.eventualSafeNodes(graph), [2, 4, 5, 6])

    def test_example_2(self):
        # Graph: 0->1, 1->2, 2->0, 3->0
        # Cycle: 0->1->2->0. Nodes 0, 1, 2 are unsafe.
        # Node 3 leads to 0 (unsafe), so 3 is unsafe.
        # Node 4 (isolated safe).
        sol = Solution()
        graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
        # Wait, let's trace properly:
        # 0->1, 0->2, 0->3, 0->4
        # 1->1 (self loop!), 1->2
        # 2->3, 2->4
        # 3->0, 3->4
        # 4->[]
        # Cycles?
        # 1->1 is a cycle. 1 is unsafe.
        # 0->1 (unsafe) => 0 is unsafe.
        # 3->0 (unsafe) => 3 is unsafe.
        # 2->3 (unsafe) => 2 is unsafe.
        # 4 is terminal. Safe.
        # So only 4 is safe.
        self.assertEqual(sol.eventualSafeNodes(graph), [4])

    def test_no_cycle(self):
        sol = Solution()
        # 0->1, 1->2. All safe.
        graph = [[1], [2], []]
        self.assertEqual(sol.eventualSafeNodes(graph), [0, 1, 2])

    def test_full_cycle(self):
        sol = Solution()
        # 0->1, 1->0
        graph = [[1], [0]]
        self.assertEqual(sol.eventualSafeNodes(graph), [])

    def test_disconnected_safe(self):
        sol = Solution()
        # 0->1, 2->3. All safe.
        graph = [[1], [], [3], []]
        self.assertEqual(sol.eventualSafeNodes(graph), [0, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()
