"""Module for random index picking based on weights."""

import random
import unittest
from typing import List


class Solution:
    """Pick an index with probability proportional to its weight."""

    def __init__(self, w: List[int]):
        """Initialize with a list of weights by building a prefix sum array."""
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        """Pick a random index using binary search on prefix sums."""
        target = random.uniform(0, self.total_sum)
        left, right = 0, len(self.prefix_sums) - 1

        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


class TestRandomPickWithWeight(unittest.TestCase):
    """Unit tests for the Random Pick with Weight solution."""

    def test_single_weight(self):
        """Case with only one weight."""
        solution = Solution([1])
        # With only one element, it must always return index 0
        for _ in range(10):
            self.assertEqual(solution.pickIndex(), 0)

    def test_uniform_distribution(self):
        """Standard distribution check."""
        weights = [1, 3]
        solution = Solution(weights)
        counts = {0: 0, 1: 0}
        for _ in range(1000):
            counts[solution.pickIndex()] += 1

        # Index 1 should appear roughly 3x more than index 0
        self.assertGreater(counts[1], counts[0])

    def test_complex_weights(self):
        """Check if indices with 0 weight are never picked (if any)."""
        # Note: LeetCode weights are usually positive, but let's test a biased set
        solution = Solution([1, 10, 1])
        counts = {0: 0, 1: 0, 2: 0}
        for _ in range(1000):
            counts[solution.pickIndex()] += 1

        # Index 1 should be the most frequent
        self.assertGreater(counts[1], counts[0])
        self.assertGreater(counts[1], counts[2])


if __name__ == "__main__":
    unittest.main()
