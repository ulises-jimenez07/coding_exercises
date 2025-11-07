"""
Problem: Count the number of 1 bits in binary representation (Hamming Weight)

Approach:
- Check each of 32 bits using bit shifting and AND operation
- Count set bits where (n & (1 << i)) is non-zero
- Time complexity: O(1) - always check 32 bits
- Space complexity: O(1)
"""

import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if n & (1 << i):  # Check if bit i is set
                count += 1
        return count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_integer_with_multiple_set_bits(self):
        """Test with 11 (binary 1011), which has 3 set bits."""
        self.assertEqual(self.solution.hammingWeight(11), 3)

    def test_power_of_two(self):
        """Test with 8 (binary 1000), which has 1 set bit."""
        self.assertEqual(self.solution.hammingWeight(8), 1)

    def test_zero(self):
        """Test with 0, which has 0 set bits."""
        self.assertEqual(self.solution.hammingWeight(0), 0)

    def test_large_number_with_single_set_bit(self):
        """Test with 128 (binary 10000000), which has 1 set bit."""
        self.assertEqual(self.solution.hammingWeight(128), 1)

    def test_all_bits_set(self):
        """Test with 4294967295 (all 32 bits set), which has 32 set bits."""
        self.assertEqual(self.solution.hammingWeight(4294967295), 32)


if __name__ == "__main__":
    unittest.main()
