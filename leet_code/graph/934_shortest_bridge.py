"""
Problem: In a given 2D binary grid, there are two islands. (An island is a 4-directionally connected group of
         1s not connected to any other 1s.)

         Change at least one 0 to a 1 to connect the two islands to form one island.
         Return the smallest number of 0s that must be flipped. (Shortest bridge).

Approach:
- Use DFS to find the first island and mark all its component cells. Collect these cells into a queue.
- Use Multi-Source BFS starting from the first island to find the shortest path to the second island.
- The first time we reach a cell belonging to the second island (value 1), the current steps is the answer.

- Time Complexity: O(N * N) as we visit each cell at most a constant number of times.
- Space Complexity: O(N * N) for the queue and recursion stack (DFS).
"""

import unittest
from collections import deque
from typing import (
    List,
    Tuple,
)


class Solution:
    """Solves the Shortest Bridge problem using DFS and BFS."""

    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        Finds the smallest number of 0s to flip to connect two islands.
        """
        n = len(grid)
        first_x, first_y = -1, -1

        # 1. Find the first island's starting point
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    found = True
                    break
            if found:
                break

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        bfs_queue: deque[Tuple[int, int]] = deque()

        # 2. Use DFS to mark the first island and add it to BFS queue
        def dfs(r, c):
            grid[r][c] = 2  # Mark as visited/part of first island
            bfs_queue.append((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)

        # Start DFS from the first found component of the island
        dfs(first_x, first_y)

        # 3. BFS to expand from the first island until reaching the second island
        distance = 0
        while bfs_queue:
            # Process level by level
            for _ in range(len(bfs_queue)):
                r, c = bfs_queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            # Found the second island
                            return distance
                        if grid[nr][nc] == 0:
                            # Expand bridge into water
                            grid[nr][nc] = -1  # Mark as visited
                            bfs_queue.append((nr, nc))
            distance += 1

        return 0


class TestShortestBridge(unittest.TestCase):
    """Test cases for Shortest Bridge."""

    def setUp(self):
        self.solution = Solution()

    def test_example_case_1(self):
        """Test simple case with bridge length 1."""
        grid = [[0, 1], [1, 0]]
        # Flipping either (0, 0) or (1, 1) connects the islands.
        expected = 1
        self.assertEqual(self.solution.shortestBridge(grid), expected)

    def test_example_case_2(self):
        """Test case with bridge length 2."""
        grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
        expected = 2
        self.assertEqual(self.solution.shortestBridge(grid), expected)

    def test_example_case_3(self):
        """Test case with concentric islands (bridge length 1)."""
        grid = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
        # The center 1 is one island, the outer ring is another.
        # They are separated by one layer of 0s.
        expected = 1
        self.assertEqual(self.solution.shortestBridge(grid), expected)


if __name__ == "__main__":
    unittest.main()
