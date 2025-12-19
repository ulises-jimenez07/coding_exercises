"""
Problem: Find all possible paths from source (0) to target (n-1) in a Directed Acyclic Graph (DAG).

Approach:
- Use DFS (Backtracking) to explore every branch.
- Since it's a DAG, we don't need a visited set to avoid infinite cycles.
- Can also use Top-Down DP (Memoization) to cache paths from intermediate nodes.
- Time complexity: O(2^N * N)
- Space complexity: O(2^N * N)
"""

import unittest
from typing import (
    Dict,
    List,
)


class Solution:
    """
    Solves All Paths Source to Target using DFS Backtracking.
    Standard approach, constructing paths incrementally.
    """

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Finds all paths from node 0 to node n-1.
        """
        target = len(graph) - 1
        results = []

        def backtrack(curr_node, path):
            # If we reached the target, save the current path
            if curr_node == target:
                results.append(list(path))
                return

            # Explore all neighbors
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)
                # Backtrack: remove last node to explore other branches
                path.pop()

        # Start from node 0
        path = [0]
        backtrack(0, path)

        return results


class SolutionMemo:
    """
    Solves All Paths Source to Target using Top-Down DP (Memoization).
    Avoids re-calculating paths from the same node multiple times.
    """

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Finds all paths using memoization.
        """
        target = len(graph) - 1
        memo: Dict[int, List[List[int]]] = {}

        def all_paths_to_target(curr_node):
            # Return cached result if we've solved this node already
            if curr_node in memo:
                return memo[curr_node]

            # Base case: reached target
            if curr_node == target:
                return [[target]]

            results = []
            for next_node in graph[curr_node]:
                # Recursively find paths from neighbor to target
                for path in all_paths_to_target(next_node):
                    # Prepend current node to those paths
                    results.append([curr_node] + path)

            # Cache the result
            memo[curr_node] = results
            return results

        return all_paths_to_target(0)


class TestAllPaths(unittest.TestCase):
    """
    Unit tests for All Paths Source to Target solution.
    """

    def test_basic_graph(self):
        # 0->1, 0->2, 1->3, 2->3. Target 3.
        # Expected paths: [0,1,3], [0,2,3]
        graph = [[1, 2], [3], [3], []]
        expected = [[0, 1, 3], [0, 2, 3]]

        for SolClass in [Solution, SolutionMemo]:
            sol = SolClass()
            result = sol.allPathsSourceTarget(graph)
            self.assertEqual(sorted(result), sorted(expected))

    def test_linear(self):
        # 0->1->2->3->4.
        graph = [[1], [2], [3], [4], []]
        expected = [[0, 1, 2, 3, 4]]

        for SolClass in [Solution, SolutionMemo]:
            sol = SolClass()
            self.assertEqual(sol.allPathsSourceTarget(graph), expected)

    def test_single_step(self):
        # 0->1
        graph = [[1], []]
        expected = [[0, 1]]

        for SolClass in [Solution, SolutionMemo]:
            sol = SolClass()
            self.assertEqual(sol.allPathsSourceTarget(graph), expected)

    def test_disconnected(self):
        # 0->1, 2->3. Target 3. 0 cannot reach 3.
        graph = [[1], [], [3], []]
        expected = []

        for SolClass in [Solution, SolutionMemo]:
            sol = SolClass()
            self.assertEqual(sol.allPathsSourceTarget(graph), expected)


if __name__ == "__main__":
    unittest.main()
