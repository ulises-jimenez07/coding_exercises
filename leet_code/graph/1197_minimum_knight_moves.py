"""LeetCode 1197 - Minimum Knight Moves.

Find the minimum number of moves for a knight to reach (x, y) from (0, 0)
on an infinite chessboard using BFS.
"""

import unittest
from collections import deque


class Solution:
    """Solves the minimum knight moves problem using BFS."""

    def minKnightMoves(self, x: int, y: int) -> int:
        """Return the minimum number of knight moves to reach (x, y) from (0, 0)."""
        directions = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        queue: deque[tuple[int, int, int]] = deque()
        queue.append((0, 0, 0))
        visited = set()
        visited.add((0, 0))

        while queue:
            r, c, steps = queue.popleft()
            if (r, c) == (x, y):
                return steps
            # Explore all 8 knight moves from current position
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))

        return -1


class TestMinKnightMoves(unittest.TestCase):
    """Unit tests for Solution.minKnightMoves."""

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # LeetCode example: one move away
        self.assertEqual(self.solution.minKnightMoves(2, 1), 1)

    def test_example_2(self):
        # LeetCode example: four moves needed
        self.assertEqual(self.solution.minKnightMoves(5, 5), 4)

    def test_origin(self):
        # Already at target
        self.assertEqual(self.solution.minKnightMoves(0, 0), 0)

    def test_negative_coordinates(self):
        # Board is infinite; symmetry means same cost as positive coords
        self.assertEqual(self.solution.minKnightMoves(-2, -1), 1)

    def test_adjacent_square(self):
        # (1, 0) requires 3 moves — a common tricky case
        self.assertEqual(self.solution.minKnightMoves(1, 0), 3)

    def test_far_target(self):
        self.assertEqual(self.solution.minKnightMoves(100, 100), 68)


if __name__ == "__main__":
    unittest.main()
