"""
Problem: 399. Evaluate Division (Medium)

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable.
You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the j-th query where you must find the answer for `Cj / Dj = ?`.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Approach:
- Model equations as a directed weighted graph.
- An equation A / B = value can be seen as:
  - An edge from A to B with weight `value`.
  - An edge from B to A with weight `1 / value`.
- To find C / D, we need to find a path from C to D.
- The weight of the path is the product of weights of the edges.
- Use DFS or BFS to find the path.
- Time complexity: O(Q * (V + E)) where Q is number of queries, V is number of variables, E is number of equations.
- Space complexity: O(V + E) to store the graph.
"""

import unittest
from collections import defaultdict
from typing import List


class Solution:
    """
    Solution for Evaluate Division problem.
    """

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the graph
        graph: dict[str, dict[str, float]] = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        def dfs(start, target, visited):
            if start not in graph or target not in graph:
                return -1.0
            if start == target:
                return 1.0

            visited.add(start)
            for neighbor, val in graph[start].items():
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:
                        return val * res
            return -1.0

        results = []
        for c, d in queries:
            results.append(dfs(c, d, set()))

        return results


class TestEvaluateDivision(unittest.TestCase):
    """
    Unit tests for Evaluate Division.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.0, 0.5, -1.0, 1.0, -1.0]
        self.assertEqual(self.solution.calcEquation(equations, values, queries), expected)

    def test_example_2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "e"], ["a", "a"], ["x", "x"]]
        expected = [3.75, 0.4, -1.0, 1.0, -1.0]
        self.assertEqual(self.solution.calcEquation(equations, values, queries), expected)


if __name__ == "__main__":
    unittest.main()
