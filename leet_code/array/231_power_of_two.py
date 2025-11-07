"""
Problem: Determine if an integer is a power of two

Approach:
- Repeatedly divide by 2 while number is even
- Check if final result is 1
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 2 == 0:
            n //= 2

        return n == 1


class TestIsPowerOfTwo(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_powers_of_two(self):
        """Tests powers of two."""
        self.assertTrue(self.solution.isPowerOfTwo(1))
        self.assertTrue(self.solution.isPowerOfTwo(2))
        self.assertTrue(self.solution.isPowerOfTwo(4))
        self.assertTrue(self.solution.isPowerOfTwo(16))
        self.assertTrue(self.solution.isPowerOfTwo(1024))

    def test_non_powers_of_two(self):
        """Tests non-powers of two."""
        self.assertFalse(self.solution.isPowerOfTwo(3))
        self.assertFalse(self.solution.isPowerOfTwo(6))
        self.assertFalse(self.solution.isPowerOfTwo(15))
        self.assertFalse(self.solution.isPowerOfTwo(1023))
        self.assertFalse(self.solution.isPowerOfTwo(5))

    def test_edge_cases(self):
        """Tests edge cases."""
        self.assertFalse(self.solution.isPowerOfTwo(0))
        self.assertFalse(self.solution.isPowerOfTwo(-2))
        self.assertFalse(self.solution.isPowerOfTwo(-16))


if __name__ == "__main__":
    unittest.main()
