"""
Problem: Rotting Oranges - Determine minimum time for all oranges to rot.

Approach:
- Use BFS (multi-source) starting from all initially rotten oranges
- Process level by level (each level represents one minute)
- Track fresh oranges and return minutes elapsed, or -1 if fresh oranges remain
- Time complexity: O(m * n)
- Space complexity: O(m * n) for the queue

Grid values:
- 0: empty cell
- 1: fresh orange
- 2: rotten orange
"""

import unittest
from collections import deque
from typing import List


class Solution:
    """
    This class contains a method to solve the 'Rotting Oranges' problem.
    The goal is to determine the minimum number of minutes that must elapse
    until no cell has a fresh orange. If this is impossible, return -1.

    Every minute, any fresh orange that is 4-directionally adjacent to a
    rotten orange becomes rotten.
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Calculates the minimum time for all fresh oranges to rot.

        Strategy:
        1. Initialize a queue with all initially rotten oranges (multi-source BFS).
        2. Count all fresh oranges.
        3. Process the queue level by level (each level = 1 minute):
           - For each rotten orange, rot all adjacent fresh oranges.
           - Add newly rotten oranges to the queue.
        4. Return the total minutes elapsed, or -1 if fresh oranges remain.
        """
        # Get dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Initialize queue for BFS and counter for fresh oranges
        queue: deque = deque()
        fresh = 0
        minutes = 0

        # Four directional movements: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 1: Scan the grid to:
        # - Add all initially rotten oranges (value=2) to the queue
        # - Count all fresh oranges (value=1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Step 2: BFS - Process all rotten oranges level by level
        # Each level represents one minute of time passing
        while queue and fresh > 0:
            # Process all oranges that are rotten at the current minute
            levels = len(queue)
            for _ in range(levels):
                r, c = queue.popleft()

                # Check all 4 adjacent cells
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # If the adjacent cell is within bounds and contains a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # Rot the fresh orange
                        grid[nr][nc] = 2
                        fresh -= 1

                        # Add newly rotten orange to queue for next minute
                        queue.append((nr, nc))

            # One minute has passed after processing all oranges at this level
            minutes += 1

        # Step 3: Return result
        # If all fresh oranges have rotted, return minutes elapsed
        # Otherwise, return -1 (some fresh oranges are unreachable)
        return minutes if fresh == 0 else -1


# -----------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def test_example_case_1(self):
        """
        Test case where all oranges rot in 4 minutes.
        """
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        expected = 4
        result = Solution().orangesRotting(grid)
        self.assertEqual(result, expected, "Should return 4 minutes for all oranges to rot.")

    def test_impossible_case(self):
        """
        Test case where a fresh orange cannot be reached.
        """
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        expected = -1
        result = Solution().orangesRotting(grid)
        self.assertEqual(result, expected, "Should return -1 when fresh orange is unreachable.")

    def test_no_fresh_oranges(self):
        """
        Test case where there are no fresh oranges initially.
        """
        grid = [[0, 2]]
        expected = 0
        result = Solution().orangesRotting(grid)
        self.assertEqual(result, expected, "Should return 0 when no fresh oranges exist.")

    def test_all_fresh_no_rotten(self):
        """
        Test case where all oranges are fresh and none are rotten.
        """
        grid = [[1, 1, 1], [1, 1, 1]]
        expected = -1
        result = Solution().orangesRotting(grid)
        self.assertEqual(result, expected, "Should return -1 when no rotten oranges to start.")

    def test_single_rotten_orange(self):
        """
        Test case with single rotten orange and no fresh oranges.
        """
        grid = [[2]]
        expected = 0
        result = Solution().orangesRotting(grid)
        self.assertEqual(result, expected, "Should return 0 for single rotten orange.")

    def test_multiple_sources(self):
        """
        Test case with multiple initially rotten oranges (multi-source BFS).
        """
        grid = [[2, 1, 1], [1, 1, 1], [1, 1, 2]]
        expected = 2
        result = Solution().orangesRotting(grid)
        self.assertEqual(result, expected, "Should handle multiple initial rotten oranges correctly.")


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # boilerplate code to run the tests when the script is executed
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
