"""
Problem: Consider a triangle where the top is 1. Each number is the sum of three
numbers above it: top-left, top, and top-right (0 if missing). Given a row number,
return the 1-indexed position of the first even number in that row.

Approach:
- Closed-form formula based on row parity: position depends on n mod 2 and n mod 4
- Odd n: first even at position 2
- n divisible by 4: first even at position 3
- n ≡ 2 (mod 4): first even at position 4
- Time complexity: O(1)
- Space complexity: O(1)

Example: n=3 (odd) -> 2; n=4 -> 3; n=6 (2 mod 4) -> 4
"""

import unittest


def triangle_numbers(n: int) -> int:
    """
    Returns the 1-indexed position of the first even number in row n.
    Uses closed-form: 2 for odd, 3 for n divisible by 4, 4 for n ≡ 2 (mod 4).
    """
    # Odd row numbers: first even at position 2
    if n % 2 != 0:
        return 2
    # Even: check divisibility by 4
    if n % 4 == 0:
        return 3
    # n ≡ 2 (mod 4): first even at position 4
    return 4


class TestTriangleNumbers(unittest.TestCase):
    """Unit tests for triangle_numbers."""

    def test_odd_rows(self):
        """Tests odd n returns 2."""
        self.assertEqual(triangle_numbers(1), 2)
        self.assertEqual(triangle_numbers(3), 2)
        self.assertEqual(triangle_numbers(5), 2)
        self.assertEqual(triangle_numbers(7), 2)

    def test_divisible_by_4(self):
        """Tests n divisible by 4 returns 3."""
        self.assertEqual(triangle_numbers(4), 3)
        self.assertEqual(triangle_numbers(8), 3)
        self.assertEqual(triangle_numbers(12), 3)

    def test_two_mod_four(self):
        """Tests n ≡ 2 (mod 4) returns 4."""
        self.assertEqual(triangle_numbers(2), 4)
        self.assertEqual(triangle_numbers(6), 4)
        self.assertEqual(triangle_numbers(10), 4)


if __name__ == "__main__":
    unittest.main()
