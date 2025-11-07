"""
Problem: Find the duplicate number in an array containing n+1 integers (1 to n)

Approach:
- Binary search on value range (1 to n), not array indices
- Count elements <= mid; if count > mid, duplicate is in lower half
- Time complexity: O(n log n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1
        ans = -1

        while start <= end:
            mid = (start + end) // 2

            # Count how many numbers are <= mid
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count <= mid:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        return ans


# --- Unit Tests ---


class TestFindDuplicate(unittest.TestCase):
    """
    Unit tests for the findDuplicate method in the Solution class.
    """

    def setUp(self):
        self.sol = Solution()

    def test_single_duplicate(self):
        """Tests a basic case with one duplicate number."""
        self.assertEqual(self.sol.findDuplicate([1, 3, 4, 2, 2]), 2)

    def test_another_single_duplicate(self):
        """Tests a different case with a single duplicate number."""
        self.assertEqual(self.sol.findDuplicate([3, 1, 3, 4, 2]), 3)

    def test_duplicate_at_boundaries(self):
        """Tests cases where the duplicate is at the beginning or end of the range."""
        # Duplicate is the smallest possible number
        self.assertEqual(self.sol.findDuplicate([2, 1, 1]), 1)
        # Duplicate is the largest possible number
        self.assertEqual(self.sol.findDuplicate([1, 2, 3, 4, 5, 5]), 5)

    def test_larger_list(self):
        """Tests with a larger list of numbers."""
        self.assertEqual(self.sol.findDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]), 9)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
