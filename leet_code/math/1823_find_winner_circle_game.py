"""
Problem: Find the winner in a circle game. n friends sit in a circle, count k each turn,
remove the k-th person. Last remaining wins. Players are numbered 1 to n.

Approach:
- Josephus problem: iterative recurrence J(n,k) = (J(n-1,k) + k) % n
- Start with J(1,k) = 0 (0-based index), build up to n
- Convert to 1-based for result (LeetCode uses 1..n)
- Time complexity: O(n)
- Space complexity: O(1)

Example: n=5, k=2 -> winner is 3; n=6, k=5 -> winner is 1
"""

import unittest


class Solution:
    """
    Iterative Josephus: build survivor index from n=1 up to n.
    """

    def findTheWinner(self, n: int, k: int) -> int:
        # Base: with 1 person, survivor is at 0-based index 0
        res = 0

        # Build up: knowing survivor for circle of size i-1, compute for size i
        # After removing k-th person from circle of i, we have i-1 people left.
        # The "next" starting position shifts by k; survivor index shifts: (res + k) % i
        for i in range(2, n + 1):
            res = (res + k) % i

        # LeetCode uses 1-based player numbers
        return res + 1


class SolutionV2:
    """
    Recursive Josephus: J(n,k) = (J(n-1,k) + k) % n.
    """

    def findTheWinner(self, n: int, k: int) -> int:
        return self._josephus(n, k) + 1

    def _josephus(self, n: int, k: int) -> int:
        # Base: single person survives at index 0
        if n == 1:
            return 0
        # Recurrence: solve for n-1, then account for the k-step removal
        # that "rotates" the circle before the subproblem
        return (self._josephus(n - 1, k) + k) % n


class TestFindTheWinner(unittest.TestCase):
    """Unit tests for Find the Winner of the Circular Game."""

    def setUp(self):
        self.solutions = [Solution(), SolutionV2()]

    def test_example_n5_k2(self):
        """Tests LeetCode example: n=5, k=2 -> 3."""
        for sol in self.solutions:
            self.assertEqual(sol.findTheWinner(5, 2), 3, f"Failed with {sol.__class__.__name__}")

    def test_example_n6_k5(self):
        """Tests LeetCode example: n=6, k=5 -> 1."""
        for sol in self.solutions:
            self.assertEqual(sol.findTheWinner(6, 5), 1, f"Failed with {sol.__class__.__name__}")

    def test_single_player(self):
        """Tests single player always wins."""
        for sol in self.solutions:
            self.assertEqual(sol.findTheWinner(1, 1), 1, f"Failed with {sol.__class__.__name__}")

    def test_two_players_k1(self):
        """Tests n=2, k=1: count 1, remove 1, player 2 wins."""
        for sol in self.solutions:
            self.assertEqual(sol.findTheWinner(2, 1), 2, f"Failed with {sol.__class__.__name__}")

    def test_two_players_k2(self):
        """Tests n=2, k=2: count 2, remove 2, player 1 wins."""
        for sol in self.solutions:
            self.assertEqual(sol.findTheWinner(2, 2), 1, f"Failed with {sol.__class__.__name__}")

    def test_three_players_k2(self):
        """Tests n=3, k=2: winner is 3."""
        for sol in self.solutions:
            self.assertEqual(sol.findTheWinner(3, 2), 3, f"Failed with {sol.__class__.__name__}")


if __name__ == "__main__":
    unittest.main()
