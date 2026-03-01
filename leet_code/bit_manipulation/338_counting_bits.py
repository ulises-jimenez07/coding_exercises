"""
Problem: Return array where each index i contains count of 1s in binary of i

Approach 1 (Solution class):
- For each number from 0 to n, count set bits
- Check all 32 bits using bit shifting and AND operation
- Time complexity: O(n * 32) = O(n)
- Space complexity: O(1) excluding output array

Approach 2 (hamming_weights_of_integers):
- For each number from 0 to n, count set bits
- Use a while loop to check only the bits until the number becomes 0
- Time complexity: O(n * log(number))
- Space complexity: O(1) excluding output array
"""

import unittest
from typing import List


class Solution:
    """
    LeetCode solution for counting bits using a bit-by-bit approach.
    """

    def countBits(self, n: int) -> List[int]:
        return [self.get_no_of_set_bits(num) for num in range(n + 1)]

    def get_no_of_set_bits(self, num: int) -> int:
        count = 0
        for i in range(32):
            if (num & (1 << i)) > 0:  # Check if bit i is set
                count += 1
        return count


def hamming_weights_of_integers(n: int) -> List[int]:
    """
    Counts the number of set bits for each integer from 0 to n.
    """
    return [count_set_bit(x) for x in range(n + 1)]


def count_set_bit(x: int) -> int:
    """
    Counts the number of set bits (1s) in the binary representation of x.
    """
    count = 0
    while x > 0:
        count += x & 1
        x >>= 1
    return count


class TestSolution(unittest.TestCase):
    """
    Unit tests for both bit counting implementations.
    """

    def setUp(self):
        self.solution = Solution()

    def test_count_bits_zero(self):
        """Tests countBits with n=0."""
        self.assertEqual(self.solution.countBits(0), [0])

    def test_count_bits_one(self):
        """Tests countBits with n=1."""
        self.assertEqual(self.solution.countBits(1), [0, 1])

    def test_count_bits_two(self):
        """Tests countBits with n=2."""
        self.assertEqual(self.solution.countBits(2), [0, 1, 1])

    def test_count_bits_five(self):
        """Tests countBits with n=5."""
        self.assertEqual(self.solution.countBits(5), [0, 1, 1, 2, 1, 2])

    def test_get_no_of_set_bits_zero(self):
        """Tests get_no_of_set_bits with num=0."""
        self.assertEqual(self.solution.get_no_of_set_bits(0), 0)

    def test_get_no_of_set_bits_one(self):
        """Tests get_no_of_set_bits with num=1."""
        self.assertEqual(self.solution.get_no_of_set_bits(1), 1)

    def test_get_no_of_set_bits_seven(self):
        """Tests get_no_of_set_bits with num=7 (binary 111)."""
        self.assertEqual(self.solution.get_no_of_set_bits(7), 3)

    def test_get_no_of_set_bits_sixteen(self):
        """Tests get_no_of_set_bits with num=16 (binary 10000)."""
        self.assertEqual(self.solution.get_no_of_set_bits(16), 1)

    def test_hamming_weights_of_integers(self):
        """Tests hamming_weights_of_integers with n=5."""
        self.assertEqual(hamming_weights_of_integers(5), [0, 1, 1, 2, 1, 2])

    def test_count_set_bit(self):
        """Tests count_set_bit with various inputs."""
        self.assertEqual(count_set_bit(0), 0)
        self.assertEqual(count_set_bit(1), 1)
        self.assertEqual(count_set_bit(7), 3)
        self.assertEqual(count_set_bit(16), 1)


if __name__ == "__main__":
    unittest.main()
