"""
Problem: Find the ordering of courses to finish all, given prerequisites (Topological Sort).

Approach:
- Model as directed graph.
- Use DFS with 3-color state tracking (UNVISITED, VISITING, VISITED).
- Detect cycles: if we see a node that is VISITING, a cycle exists.
- Post-order DFS traversal gives reverse topological order.
- Time complexity: O(V + E)
- Space complexity: O(V + E)
"""

import unittest
from collections import defaultdict
from typing import List


class Solution:
    """
    Solves Course Schedule II using DFS to perform a topological sort.
    Returns the order of courses or an empty list if a cycle exists.
    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Derives a valid course order.
        """
        # 0=unvisited, 1=visiting, 2=visited
        UNVISITED, VISITING, VISITED = 0, 1, 2

        # Build adjacency list: src -> list of dests
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topo_order = []
        is_possible = True
        state = {i: UNVISITED for i in range(numCourses)}

        def dfs(node: int) -> None:
            nonlocal is_possible
            if not is_possible:
                return

            # Mark as visiting (gray)
            state[node] = VISITING

            for neighbor in adj_list[node]:
                if state[neighbor] == UNVISITED:
                    dfs(neighbor)
                elif state[neighbor] == VISITING:
                    # Cycle detected (back edge)
                    is_possible = False

            # Mark as visited (black) and add to order (post-order)
            state[node] = VISITED
            topo_order.append(node)

        for vertex in range(numCourses):
            if state[vertex] == UNVISITED:
                dfs(vertex)

        # Reverse the post-order to get topological sort
        return topo_order[::-1] if is_possible else []


class TestCourseScheduleII(unittest.TestCase):
    """
    Unit tests for the findOrder method of the Solution class.
    """

    def test_basic_success(self):
        sol = Solution()
        # 1 -> 0 (0 is prereq for 1)
        # Expected: [0, 1]
        self.assertEqual(sol.findOrder(2, [[1, 0]]), [0, 1])

    def test_cycle(self):
        sol = Solution()
        # 0 -> 1 -> 0
        self.assertEqual(sol.findOrder(2, [[1, 0], [0, 1]]), [])

    def test_complex_success(self):
        sol = Solution()
        # 0->1, 0->2, 1->3, 2->3
        # 3 must come after 1 and 2. 1 and 2 must come after 0.
        # Order: 0 -> 1,2 -> 3
        result = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])

        # Verify valid topological sort
        index = {node: i for i, node in enumerate(result)}
        self.assertTrue(index[0] < index[1])
        self.assertTrue(index[0] < index[2])
        self.assertTrue(index[1] < index[3])
        self.assertTrue(index[2] < index[3])
        self.assertEqual(len(result), 4)

    def test_no_prerequisites(self):
        sol = Solution()
        result = sol.findOrder(2, [])
        # Any valid permutation is fine, usually [0, 1] or [1, 0]
        self.assertEqual(len(result), 2)
        self.assertIn(0, result)
        self.assertIn(1, result)


if __name__ == "__main__":
    unittest.main()
