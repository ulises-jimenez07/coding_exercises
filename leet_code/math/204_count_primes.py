"""
Problem: Count the number of prime numbers less than a non-negative integer n

Approach:
- Use Sieve of Eratosthenes algorithm
- Mark all multiples of each prime as composite
- Time complexity: O(n log log n)
- Space complexity: O(n)
"""

import math
import unittest


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0  # 0 and 1 are not prime

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if is_prime[i]:
                # Mark all multiples of i as composite
                for multiple_of_i in range(i**2, n, i):
                    is_prime[multiple_of_i] = 0

        return sum(is_prime)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_is_ten(self):
        """Test with n = 10."""
        n = 10
        expected = 4
        self.assertEqual(self.solution.countPrimes(n), expected)

    def test_n_is_zero(self):
        """Test with n = 0."""
        n = 0
        expected = 0
        self.assertEqual(self.solution.countPrimes(n), expected)

    def test_n_is_one(self):
        """Test with n = 1."""
        n = 1
        expected = 0
        self.assertEqual(self.solution.countPrimes(n), expected)

    def test_n_is_two(self):
        """Test with n = 2."""
        n = 2
        expected = 0
        self.assertEqual(self.solution.countPrimes(n), expected)

    def test_n_is_three(self):
        """Test with n = 3."""
        n = 3
        expected = 1
        self.assertEqual(self.solution.countPrimes(n), expected)

    def test_larger_number(self):
        """Test with a larger number, n = 50."""
        n = 50
        expected = 15
        self.assertEqual(self.solution.countPrimes(n), expected)


if __name__ == "__main__":
    unittest.main()
