"""
Problem: Determine if a robot returns to the origin after executing a sequence of moves

Approach:
- Track x and y coordinates starting from (0, 0)
- Process each move (U/D/L/R) and update coordinates
- Time complexity: O(n) where n is number of moves
- Space complexity: O(1)
"""

import unittest


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
            elif move == "R":
                x += 1

        return x == 0 and y == 0  # Check if back at origin


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_returns_to_origin_ud(self):
        """Test with moves 'UD' which should return to origin."""
        moves = "UD"
        expected = True
        self.assertEqual(self.solution.judgeCircle(moves), expected)

    def test_does_not_return_to_origin_ldrrlr_uulr(self):
        """Test with moves 'LDRRLRUULR' which should not return to origin."""
        moves = "LDRRLRUULR"
        expected = False
        self.assertEqual(self.solution.judgeCircle(moves), expected)

    def test_does_not_return_to_origin_ll(self):
        """Test with moves 'LL' which should not return to origin."""
        moves = "LL"
        expected = False
        self.assertEqual(self.solution.judgeCircle(moves), expected)

    def test_empty_moves(self):
        """Test with empty moves, should return to origin."""
        moves = ""
        expected = True
        self.assertEqual(self.solution.judgeCircle(moves), expected)

    def test_circular_movement(self):
        """Test with circular movement 'ULDR' which should return to origin."""
        moves = "ULDR"
        expected = True
        self.assertEqual(self.solution.judgeCircle(moves), expected)


if __name__ == "__main__":
    unittest.main()
