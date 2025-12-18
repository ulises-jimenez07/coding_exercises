"""
Problem: Determine if it's possible to finish all courses given prerequisites (cycle detection).

Approach:
- Model as directed graph, use DFS with 3-color state tracking
- Detect cycles (visiting -> visiting edge indicates cycle)
- Time complexity: O(V + E) where V is courses and E is prerequisites
- Space complexity: O(V) for state tracking and recursion stack
"""

import unittest
from typing import (
    Dict,
    List,
)


class Solution_v1:
    """
    Solves the Course Schedule problem using Depth First Search (DFS) to detect cycles
    in a directed graph. A cycle indicates a dependency loop, meaning it's impossible
    to finish all courses.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if it's possible to finish all courses given the prerequisites.
        """
        # Adjacency list to represent the graph where an edge from 'b' to 'a' means
        # 'a' is a prerequisite for 'b'.
        self.adj: List[List[int]] = [[] for _ in range(numCourses)]  # pylint: disable=attribute-defined-outside-init
        # State of each node (course):
        # 'u' (unvisited): The node has not been visited yet.
        # 'v' (visiting): The node is currently being visited in the current DFS path.
        # 'p' (processed): The node and all its descendants have been visited.
        self.state = {i: "u" for i in range(numCourses)}  # pylint: disable=attribute-defined-outside-init

        # Build the adjacency list from the prerequisites.
        for to_node, from_node in prerequisites:
            self.adj[from_node].append(to_node)

        # Iterate through all courses and start a DFS traversal from unvisited nodes.
        for i in range(numCourses):
            if self.state[i] == "u":
                # If a cycle is detected during the DFS traversal, it's impossible to finish.
                if not self.dfs(i):
                    return False
        # If no cycles were found after visiting all nodes, it's possible to finish all courses.
        return True

    def dfs(self, node: int) -> bool:
        """
        Performs a Depth First Search from a given node to detect cycles.
        """
        # Mark the current node as 'visiting'.
        self.state[node] = "v"

        # Traverse all neighbors of the current node.
        for nei in self.adj[node]:
            # If a neighbor is in the 'visiting' state, a back-edge is found, which
            # indicates a cycle.
            if self.state[nei] == "v":
                return False  # Cycle detected
            # If an unvisited neighbor is found, recursively call DFS on it.
            if self.state[nei] == "u":
                if not self.dfs(nei):
                    return False

        # After visiting all neighbors and their subgraphs, mark the current node as 'processed'.
        self.state[node] = "p"
        return True


class Solution:
    """
    Solves the Course Schedule problem using DFS with integer state tracking.
    Uses 0 (unvisited), 1 (visiting), and 2 (visited) to detect cycles.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list: course -> list of prerequisites
        graph: Dict[int, List[int]] = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state: List[int] = [0] * numCourses

        def has_cycle(course):
            # If we see a node currently being visited, it's a cycle (back edge)
            if state[course] == 1:
                return True
            # If already fully processed, no cycle here
            if state[course] == 2:
                return False

            # Mark as visiting
            state[course] = 1
            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True

            # Mark as visited (processed)
            state[course] = 2

            return False

        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False

        return True


# -------------------------------------------------------------------------------------
## Unit Tests


class TestCanFinish(unittest.TestCase):
    """
    Unit tests for the canFinish method of the Solution class.
    """

    def test_no_prerequisites(self):
        """
        Tests a case with no prerequisites. All courses should be finishable.
        """
        for SolClass in [Solution, Solution_v1]:
            with self.subTest(impl=SolClass.__name__):
                solution = SolClass()
                self.assertTrue(solution.canFinish(2, []))

    def test_finishable_courses(self):
        """
        Tests a valid sequence of prerequisites (no cycles).
        """
        for SolClass in [Solution, Solution_v1]:
            with self.subTest(impl=SolClass.__name__):
                solution = SolClass()
                # Prerequisites: 1 -> 0 (to take course 0, you must first take course 1).
                self.assertTrue(solution.canFinish(2, [[0, 1]]))

    def test_cycle_prerequisites(self):
        """
        Tests a case with a cycle, making it impossible to finish.
        """
        for SolClass in [Solution, Solution_v1]:
            with self.subTest(impl=SolClass.__name__):
                solution = SolClass()
                # Prerequisites: 1 -> 0 and 0 -> 1 (a cycle).
                self.assertFalse(solution.canFinish(2, [[1, 0], [0, 1]]))

    def test_complex_graph_with_cycle(self):
        """
        Tests a more complex graph with a cycle.
        """
        for SolClass in [Solution, Solution_v1]:
            with self.subTest(impl=SolClass.__name__):
                solution = SolClass()
                # Prerequisites: 1->0, 2->1, 3->2, 1->3
                # The path 1->3->2->1 forms a cycle.
                self.assertFalse(solution.canFinish(4, [[0, 1], [1, 2], [2, 3], [3, 1]]))

    def test_complex_graph_no_cycle(self):
        """
        Tests a more complex graph without a cycle.
        """
        for SolClass in [Solution, Solution_v1]:
            with self.subTest(impl=SolClass.__name__):
                solution = SolClass()
                # Prerequisites: 1->0, 2->0, 3->1, 3->2, 4->3
                # No cycles here.
                self.assertTrue(solution.canFinish(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]))


if __name__ == "__main__":
    unittest.main()
