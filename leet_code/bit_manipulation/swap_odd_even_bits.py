"""
Problem: Swap odd and even bits in an integer.

Approach:
- Use masks to extract even (0x55...) and odd (0xAA...) bits
- Shift even bits left by 1 and odd bits right by 1
- Combine them with OR to get the result
- Time complexity: O(1)
- Space complexity: O(1)
"""

import unittest


class Solution:
    """
    A class to swap odd and even bits of a 32-bit integer.
    """

    def swapOddAndEvenBits(self, n: int) -> int:
        """
        Swaps all odd bits with even bits and vice-versa.
        """
        # Mask 0x5... extracts even bits (0, 2, 4, ...)
        # Mask 0xA... extracts odd bits (1, 3, 5, ...)
        even_mask = 0x55555555
        odd_mask = 0xAAAAAAAA

        even_bits = n & even_mask
        odd_bits = n & odd_mask

        # Move even bits left to odd positions, and odd bits right to even positions
        return (even_bits << 1) | (odd_bits >> 1)


# -----------------------------------------------------------------------------


class TestSwapBits(unittest.TestCase):
    """
    Unit tests for the Solution class's swapOddAndEvenBits method.
    """

    def setUp(self):
        self.solution = Solution()

    def test_basic_swap_one(self):
        """Test swapping bits of 1 (01 -> 10)."""
        n = 1
        expected = 2
        result = self.solution.swapOddAndEvenBits(n)
        self.assertEqual(result, expected)

    def test_basic_swap_two(self):
        """Test swapping bits of 2 (10 -> 01)."""
        n = 2
        expected = 1
        result = self.solution.swapOddAndEvenBits(n)
        self.assertEqual(result, expected)

    def test_basic_swap_ten(self):
        """Test swapping bits of 10 (1010 -> 0101)."""
        n = 10
        expected = 5
        result = self.solution.swapOddAndEvenBits(n)
        self.assertEqual(result, expected)

    def test_zero(self):
        """Test swapping bits of 0."""
        n = 0
        expected = 0
        result = self.solution.swapOddAndEvenBits(n)
        self.assertEqual(result, expected)

    def test_all_ones(self):
        """Test swapping bits of 0xFFFFFFFF (all ones stay all ones)."""
        n = 0xFFFFFFFF
        expected = 0xFFFFFFFF
        result = self.solution.swapOddAndEvenBits(n)
        self.assertEqual(result, expected)

    def test_large_number(self):
        """Test swapping bits of a large arbitrary number."""
        # Binary: 1100 0011 -> Expected: 1100 0011 (wait, 1100 is bit 1,0 at 1,1. 0011 is bit 1,0 at 1,1)
        # 0xC3 = 11000011
        # positions: 76543210
        # bits:      11000011
        # even (0,2,4,6): bits 1, 0, 0, 1 -> 0x41
        # odd (1,3,5,7):  bits 1, 0, 0, 1 -> 0x82
        # even << 1: 10000010 (0x82)
        # odd >> 1: 01000001 (0x41)
        # result: 11000011 (0xC3)
        n = 0xC3
        expected = 0xC3
        result = self.solution.swapOddAndEvenBits(n)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
