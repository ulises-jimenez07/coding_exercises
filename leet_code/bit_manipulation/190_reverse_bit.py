"""
Problem: Reverse bits of a given 32-bit unsigned integer.

Approach:
- Iterate through bits of the input number
- Shift bits to their reversed positions (31 - original_index)
- Collect the result in a new integer
- Time complexity: O(1) as we always iterate 32 bits (or until n is 0)
- Space complexity: O(1)
"""

import unittest


class Solution:
    """
    A class to reverse bits of an unsigned 32-bit integer.
    """

    def reverseBits(self, n: int) -> int:
        """
        Reverses bits of the input 32-bit unsigned integer.
        """
        ret, power = 0, 31
        while n:
            # Extract the last bit and shift it to the reversed position
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret


# -----------------------------------------------------------------------------


class TestReverseBits(unittest.TestCase):
    """
    Unit tests for the Solution class's reverseBits method.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case from LeetCode example 1 (n=43261596)."""
        n = 43261596
        # Binary: 00000010100101000001111010011100
        # Expected: 964176192 (00111001011110000010100101000000)
        expected = 964176192
        result = self.solution.reverseBits(n)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """Test case from LeetCode example 2 (n=4294967293)."""
        n = 4294967293
        # Binary: 11111111111111111111111111111101
        # Expected: 3221225471 (10111111111111111111111111111111)
        expected = 3221225471
        result = self.solution.reverseBits(n)
        self.assertEqual(result, expected)

    def test_zero(self):
        """Test case with input 0."""
        n = 0
        expected = 0
        result = self.solution.reverseBits(n)
        self.assertEqual(result, expected)

    def test_all_ones(self):
        """Test case with all bits set to 1."""
        n = 4294967295  # 2^32 - 1
        expected = 4294967295
        result = self.solution.reverseBits(n)
        self.assertEqual(result, expected)

    def test_single_one_at_end(self):
        """Test case with only the lowest bit set."""
        n = 1
        expected = 2147483648  # 2^31
        result = self.solution.reverseBits(n)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
