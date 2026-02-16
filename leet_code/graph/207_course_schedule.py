"""
Problem: Determine if it's possible to finish all courses given prerequisites (cycle detection).

Approach:
- Solution 1 (DFS): Use 3-color state tracking to detect cycles in a directed graph.
- Solution 2 (BFS): Kahn's Algorithm (Topological Sort). If we can't visit all nodes, there's a cycle.

Complexity:
- Time: O(V + E) where V is courses and E is prerequisites.
- Space: O(V + E) for the adjacency list and O(V) for state tracking.
"""

import unittest
from collections import (
    defaultdict,
    deque,
)
from typing import (
    DefaultDict,
    Deque,
    List,
)


class SolutionV1:
    """
    Solves the Course Schedule problem using DFS with integer state tracking.
    Uses 0 (unvisited), 1 (visiting), and 2 (visited) to detect cycles.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if it's possible to finish all courses using DFS.
        """
        # Build adjacency list: course -> list of its prerequisites.
        # This mapping allows us to traverse from a course to its dependencies.
        graph: DefaultDict[int, List[int]] = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # State tracking: 0 = unvisited, 1 = visiting (in current path), 2 = visited (processed).
        state = [0] * numCourses
        UNVISITED, VISITING, VISITED = 0, 1, 2

        def has_cycle(node):
            # If we encounter a node already in 'VISITING' state, a back-edge (cycle) exists.
            if state[node] == VISITING:
                return True
            # If already fully processed, no need to re-check this branch.
            if state[node] == VISITED:
                return False

            # Mark current node as 'visiting' to track the current recursion depth.
            state[node] = VISITING

            for prereq in graph[node]:
                if has_cycle(prereq):
                    return True

            # Mark as 'visited' once all paths from this node are explored.
            state[node] = VISITED
            return False

        # Start DFS traversal from every unvisited course to ensure we cover disconnected components.
        for course in range(numCourses):
            if state[course] == UNVISITED:
                if has_cycle(course):
                    return False
        return True


class SolutionV2:
    """
    Solves the Course Schedule problem using Kahn's Algorithm (BFS).
    Computes in-degrees and uses a queue to process nodes with zero in-degree.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if it's possible to finish all courses using BFS (Kahn's Algorithm).
        """
        # Build graph: prereq -> list of courses that depend on it.
        # Simultaneously track how many dependencies (in-degree) each course has.
        graph: DefaultDict[int, List[int]] = defaultdict(list)
        in_degrees = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degrees[course] += 1

        # Queue contains all courses that have NO dependencies and can be taken immediately.
        queue: Deque[int] = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        enrolled_courses = 0

        while queue:
            node = queue.popleft()
            enrolled_courses += 1

            # For each dependent course, reduce its in-degree as the prerequisite is now 'taken'.
            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1
                # If a course's in-degree drops to zero, it's ready to be enrolled.
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        # If we couldn't enroll in all courses, a cycle must have prevented in-degrees from reaching zero.
        return enrolled_courses == numCourses


# -------------------------------------------------------------------------------------
## Unit Tests


class TestCanFinish(unittest.TestCase):
    """
    Unit tests for the canFinish method of the Solution classes.
    """

    def test_no_prerequisites(self):
        """
        Tests a case with no prerequisites. All courses should be finishable.
        """
        for SolClass in [SolutionV1, SolutionV2]:
            with self.subTest(impl=SolClass.__name__):
                solution = SolClass()
                self.assertTrue(solution.canFinish(2, []))

    def test_finishable_courses(self):
        """
        Tests a valid sequence of prerequisites (no cycles).
        """
        for SolClass in [SolutionV1, SolutionV2]:
            with self.subTest(impl=SolClass.__name__):
                solution = SolClass()
                # Prerequisites: 1 -> 0 (to take course 0, you must first take course 1).
                self.assertTrue(solution.canFinish(2, [[0, 1]]))

    def test_cycle_prerequisites(self):
        """
        Tests a case with a cycle, making it impossible to finish.
        """
        for SolClass in [SolutionV1, SolutionV2]:
            with self.subTest(impl=SolClass.__name__):
                solution = SolClass()
                # Prerequisites: 1 -> 0 and 0 -> 1 (a cycle).
                self.assertFalse(solution.canFinish(2, [[1, 0], [0, 1]]))

    def test_complex_graph_with_cycle(self):
        """
        Tests a more complex graph with a cycle.
        """
        for SolClass in [SolutionV1, SolutionV2]:
            with self.subTest(impl=SolClass.__name__):
                solution = SolClass()
                # Prerequisites: 1->0, 2->1, 3->2, 1->3
                # The path 1->3->2->1 forms a cycle.
                self.assertFalse(solution.canFinish(4, [[0, 1], [1, 2], [2, 3], [3, 1]]))

    def test_complex_graph_no_cycle(self):
        """
        Tests a more complex graph without a cycle.
        """
        for SolClass in [SolutionV1, SolutionV2]:
            with self.subTest(impl=SolClass.__name__):
                solution = SolClass()
                # Prerequisites: 1->0, 2->0, 3->1, 3->2, 4->3
                # No cycles here.
                self.assertTrue(solution.canFinish(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]))


if __name__ == "__main__":
    unittest.main()
