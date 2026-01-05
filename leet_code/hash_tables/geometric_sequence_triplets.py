"""
Problem: Count triplets in geometric sequence (a, a*r, a*r*r)

Approach:
- Use two maps: left_map (numbers before current) and right_map (numbers after current)
- For each number x, check if x/r exists in left_map and x*r exists in right_map
- Time complexity: O(n)
- Space complexity: O(n)
"""

import unittest
from collections import (
    Counter,
    defaultdict,
)
from typing import List


def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    """
    Count triplets forming geometric sequence with ratio r.
    """
    left_map: dict[int, int] = defaultdict(int)
    count = 0

    # Initialize right_map with all numbers
    right_map = Counter(nums)

    for x in nums:
        # Remove current number from right_map (it's now the middle element)
        right_map[x] -= 1

        # Check if x can be middle element: x/r must exist before, x*r after
        if x % r == 0:
            count += left_map[x // r] * right_map[x * r]

        # Add current number to left_map for future iterations
        left_map[x] += 1

    return count


class TestGeometricSequenceTriplets(unittest.TestCase):
    """Test cases for geometric_sequence_triplets function."""

    def setUp(self):
        pass

    def test_simple_case(self):
        self.assertEqual(geometric_sequence_triplets([1, 2, 4], 2), 1)

    def test_multiple_triplets(self):
        self.assertEqual(geometric_sequence_triplets([1, 2, 2, 4], 2), 2)

    def test_no_triplets(self):
        self.assertEqual(geometric_sequence_triplets([1, 2, 3], 2), 0)

    def test_empty_list(self):
        self.assertEqual(geometric_sequence_triplets([], 2), 0)

    def test_single_element(self):
        self.assertEqual(geometric_sequence_triplets([1], 2), 0)

    def test_ratio_one(self):
        self.assertEqual(geometric_sequence_triplets([1, 1, 1], 1), 1)

    def test_large_ratio(self):
        self.assertEqual(geometric_sequence_triplets([1, 3, 9, 9, 27], 3), 4)

    def test_negative_numbers(self):
        self.assertEqual(geometric_sequence_triplets([-2, -4, -8], 2), 1)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
