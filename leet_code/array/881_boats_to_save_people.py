"""
Problem: Calculate minimum number of boats needed to save people with weight limit

Approach:
- Sort people by weight, use two pointers from lightest and heaviest
- Pair lightest with heaviest if possible, otherwise send heaviest alone
- Time complexity: O(n log n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """Calculates minimum number of boats needed to save people."""
        people.sort()

        smallest = 0
        biggest = len(people) - 1
        boats = 0

        while biggest >= smallest:
            if people[biggest] + people[smallest] <= limit:
                biggest -= 1
                smallest += 1
            else:
                biggest -= 1
            boats += 1

        return boats


class TestNumRescueBoats(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example."""
        self.assertEqual(self.solution.numRescueBoats([1, 2, 2, 3], 3), 3)

    def test_everyone_pairs(self):
        """Everyone can fit in pairs."""
        self.assertEqual(self.solution.numRescueBoats([2, 3, 3, 4], 5), 3)

    def test_mixed_weights(self):
        """Mixed weights."""
        self.assertEqual(self.solution.numRescueBoats([5, 1, 4, 2], 6), 2)

    def test_same_weight(self):
        """All people same weight."""
        self.assertEqual(self.solution.numRescueBoats([3, 3, 3, 3], 6), 2)

    def test_empty_list(self):
        """Empty list."""
        self.assertEqual(self.solution.numRescueBoats([], 5), 0)

    def test_single_person(self):
        """Single person."""
        self.assertEqual(self.solution.numRescueBoats([7], 8), 1)


if __name__ == "__main__":
    unittest.main()
