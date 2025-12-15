"""
Problem: You are given an m x n grid rooms initialized with these three possible values.
         -1 A wall or an obstacle.
         0 A gate.
         INF Infinity means an empty room.

         Fill each empty room with the distance to its nearest gate.
         If it is impossible to reach a gate, it should be filled with INF.

Approach:
- Use Multi-Source BFS starting from all gates simultaneously.
- Since BFS guarantees the shortest path in an unweighted grid, the first time we reach a room, it is via the shortest path from a gate.
- Initialize the queue with all gates.
- Update neighbors with distance + 1.

- Time Complexity: O(M * N) since each cell is visited at most once.
- Space Complexity: O(M * N) for the queue.
"""

import unittest
from collections import deque
from typing import (
    List,
    Tuple,
)


class Solution:
    """Solves the Walls and Gates problem using Multi-Source BFS."""

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Modifies rooms in-place to store the distance to the nearest gate for each empty room.
        """
        if not rooms:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue: deque[Tuple[int, int]] = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        GATE = 0
        EMPTY = 2147483647

        # 1. Initialize Queue with all Gates
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == GATE:
                    queue.append((i, j))

        # 2. Perform Multi-Source BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds and if the room is empty (unvisited)
                # We only visit 'EMPTY' rooms, which ensures we don't revisit walls/gates or already visited rooms.
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == EMPTY:
                    # The distance is the distance of the previous room + 1
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))


class TestWallsAndGates(unittest.TestCase):
    """Test cases for Walls and Gates."""

    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        """Test the standard example case."""
        inf = 2147483647
        rooms = [
            [inf, -1, 0, inf],
            [inf, inf, inf, -1],
            [inf, -1, inf, -1],
            [0, -1, inf, inf],
        ]
        # Distances:
        # 3, -1, 0, 1
        # 2, 2, 1, -1
        # 1, -1, 2, -1
        # 0, -1, 3, 4
        expected = [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ]
        self.solution.wallsAndGates(rooms)
        self.assertEqual(rooms, expected)

    def test_no_gates(self):
        """Test grid with no gates."""
        inf = 2147483647
        rooms = [[inf, inf], [inf, inf]]
        expected = [[inf, inf], [inf, inf]]
        self.solution.wallsAndGates(rooms)
        self.assertEqual(rooms, expected)

    def test_no_rooms(self):
        """Test empty grid."""
        rooms = []
        self.solution.wallsAndGates(rooms)
        self.assertEqual(rooms, [])

    def test_unreachable_room(self):
        """Test room surrounded by walls."""
        inf = 2147483647
        rooms = [[0, -1, inf], [-1, -1, -1], [inf, inf, inf]]
        # Only the top-left 0 is a gate. The 'inf' at (0,2) is blocked.
        # Bottom row is also blocked.
        expected = [[0, -1, inf], [-1, -1, -1], [inf, inf, inf]]
        self.solution.wallsAndGates(rooms)
        self.assertEqual(rooms, expected)


if __name__ == "__main__":
    unittest.main()
