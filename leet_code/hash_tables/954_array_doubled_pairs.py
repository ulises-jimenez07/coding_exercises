"""
Problem: Given an integer array of even length arr, return true if it is possible to reorder arr
such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

Approach:
- Use a hash table to count the frequency of each number.
- Sort the array by absolute values to process elements from smallest to largest magnitude.
- For each element, check if its double exists in the count map.
- Time complexity: O(n log n) due to sorting.
- Space complexity: O(n) for the frequency map.
"""

import unittest
from collections import Counter
from typing import List


class Solution:
    """Solution for the array doubled pairs problem."""

    def canReorderDoubled(self, arr: List[int]) -> bool:
        """Check if array can be reordered into pairs where one is double the other."""
        count = Counter(arr)

        # Sort by absolute value to handle negative numbers correctly
        # This ensures we move from smaller to larger magnitudes
        arr.sort(key=abs)

        for x in arr:
            # Skip if this number has already been used in a pair
            if count[x] == 0:
                continue

            # If the double doesn't exist, we can't form the required pair
            if count[2 * x] == 0:
                return False

            # Decrement counts for both the current number and its double
            count[x] -= 1
            count[2 * x] -= 1

        return True


class TestArrayDoubledPairs(unittest.TestCase):
    """Unit tests for the canReorderDoubled solution."""

    def setUp(self):
        """Set up the Solution instance."""
        self.solution = Solution()

    def test_example_1(self):
        """Test example 1 from LeetCode."""
        arr = [3, 1, 3, 6]
        self.assertFalse(self.solution.canReorderDoubled(arr))

    def test_example_2(self):
        """Test example 2 from LeetCode."""
        arr = [2, 1, 2, 6]
        self.assertFalse(self.solution.canReorderDoubled(arr))

    def test_example_3(self):
        """Test example 3 from LeetCode."""
        arr = [4, -2, 2, -4]
        self.assertTrue(self.solution.canReorderDoubled(arr))

    def test_empty_list(self):
        """Test with an empty list."""
        arr = []
        self.assertTrue(self.solution.canReorderDoubled(arr))

    def test_zeros(self):
        """Test with zero values."""
        arr = [0, 0, 0, 0]
        self.assertTrue(self.solution.canReorderDoubled(arr))

    def test_negative_doubles(self):
        """Test with negative numbers and their doubles."""
        arr = [-1, -2, -4, -8]
        self.assertTrue(self.solution.canReorderDoubled(arr))

    def test_mixed_values(self):
        """Test mixed positive and negative values."""
        arr = [1, 2, -3, -6, 0, 0]
        self.assertTrue(self.solution.canReorderDoubled(arr))

    def test_single_element(self):
        """Test with a single element (odd length)."""
        arr = [1]
        self.assertFalse(self.solution.canReorderDoubled(arr))


if __name__ == "__main__":
    unittest.main()
