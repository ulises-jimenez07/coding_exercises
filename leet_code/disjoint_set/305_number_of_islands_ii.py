"""
Problem: 305. Number of Islands II (Hard)

You are given an empty 2D binary grid of size `m x n`. The grid represents a 2D map where 0 is water and 1 is land.
Initially, all cells are water. You are given an array `positions` where `positions[i] = [ri, ci]` is the position (ri, ci) at which you should add a piece of land to the water at the i-th step.
Return an array of integers `ans` where `ans[i]` is the number of islands after adding a piece of land at the i-th step.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Approach:
- Use Union-Find data structure to maintain connected components of land.
- For each new land position:
  - Check if it's already land (if positions can have duplicates).
  - Increment island count.
  - Check 4 neighbors.
  - If a neighbor is land, union the current position with that neighbor.
  - If union is successful, decrement island count.
- Time complexity: O(L * alpha(m*n)) where L is number of positions, and alpha is inverse Ackermann function.
- Space complexity: O(m*n) for DSU.
"""

import unittest
from typing import List


class DSU:
    """
    Disjoint Set Union (DSU) data structure to maintain connected components.
    """

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.count = 0

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            self.count -= 1
            return True
        return False


class Solution:
    """
    Solution for Number of Islands II problem.
    """

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = DSU(m * n)
        grid = [[0] * n for _ in range(m)]
        ans = []

        for r, c in positions:
            if grid[r][c] == 1:
                ans.append(dsu.count)
                continue

            grid[r][c] = 1
            dsu.count += 1

            curr_idx = r * n + c
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    dsu.union(curr_idx, nr * n + nc)

            ans.append(dsu.count)

        return ans


class TestNumberIslandsII(unittest.TestCase):
    """
    Unit tests for Number of Islands II.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        m, n = 3, 3
        positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
        expected = [1, 1, 2, 3]
        self.assertEqual(self.solution.numIslands2(m, n, positions), expected)

    def test_example_2(self):
        m, n = 1, 1
        positions = [[0, 0]]
        expected = [1]
        self.assertEqual(self.solution.numIslands2(m, n, positions), expected)

    def test_with_duplicates(self):
        m, n = 3, 3
        positions = [[0, 0], [0, 1], [0, 1], [1, 2], [2, 1]]
        expected = [1, 1, 1, 2, 3]
        self.assertEqual(self.solution.numIslands2(m, n, positions), expected)


if __name__ == "__main__":
    unittest.main()
