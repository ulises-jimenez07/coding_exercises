"""
Problem: Cutting Wood (EKO)
Given heights of trees and a required amount of wood 'k', find the maximum
integer height 'H' the saw should be set to such that at least 'k' wood is collected.

Approach:
- Binary Search on the possible height range [0, max(heights)].
- We want to find the largest height 'H' where cuts_enough_wood(H) is True.
- Time Complexity: O(N log(max_height)), where N is the number of trees.
- Space Complexity: O(1).
"""

import unittest
from typing import List


def cutting_wood(heights: List[int], k: int) -> int:
    """
    Finds the maximum height to set the saw to collect at least k wood.

    - Starting range: left = 0, right = max(heights).
    - Stop condition: left == right (loop runs while left < right).
    - Mid calculation: (left + right) // 2 + 1. The '+ 1' makes it right-biased,
      which is necessary when we update 'left = mid' to avoid an infinite loop
      when left and right are adjacent (e.g., left=2, right=3 -> mid=3).
    - Condition to move:
        - If we collect enough wood at 'mid', we try higher (left = mid).
        - If we don't collect enough, we must go lower (right = mid - 1).
    """
    if not heights:
        return 0

    left, right = 0, max(heights)

    while left < right:
        # We use right-biased mid calculation to prevent infinite loops.
        # If left = 2 and right = 3, standard mid = 2. If left = mid,
        # it stays 2 forever. +1 makes mid = 3, allowing progress.
        mid = (left + right) // 2 + 1

        if cuts_enough_wood(mid, k, heights):
            # If mid works, it might be the answer, so we keep it (left = mid).
            # We look for a potentially higher height in [mid, right].
            left = mid
        else:
            # If mid doesn't work, we must look in the lower range [left, mid - 1].
            right = mid - 1

    return left


def cuts_enough_wood(set_h: int, k: int, heights: List[int]) -> bool:
    """
    Helper function to check if setting the saw at 'set_h' collects at least 'k' wood.
    """
    wood_collected = 0
    for tree_h in heights:
        if tree_h > set_h:
            wood_collected += tree_h - set_h
            # Optional optimization: break early if we already have enough wood
            if wood_collected >= k:
                return True
    return wood_collected >= k


class TestCuttingWood(unittest.TestCase):
    """
    Unit tests for the cutting_wood function.
    """

    def test_standard_cases(self):
        """Test with typical inputs."""
        self.assertEqual(cutting_wood([20, 15, 10, 17], 7), 15)
        self.assertEqual(cutting_wood([4, 42, 40, 26, 46], 20), 36)

    def test_exact_match(self):
        """Test cases where the required wood is exactly provided by a height."""
        self.assertEqual(cutting_wood([10, 10, 10], 15), 5)

    def test_no_wood_needed(self):
        """Test when k is 0, the height should be the tallest tree."""
        self.assertEqual(cutting_wood([10, 20, 30], 0), 30)

    def test_cannot_collect_enough(self):
        """Test when even height 0 doesn't give enough wood (unlikely but possible)."""
        # Sum is 6, we need 7. Height 0 is the lowest possible.
        self.assertEqual(cutting_wood([1, 2, 3], 10), 0)

    def test_single_tree(self):
        """Test with only one tree."""
        self.assertEqual(cutting_wood([10], 5), 5)
        self.assertEqual(cutting_wood([10], 11), 0)


if __name__ == "__main__":
    unittest.main()
