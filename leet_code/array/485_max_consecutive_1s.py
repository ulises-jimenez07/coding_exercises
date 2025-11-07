"""
Problem: Find the maximum number of consecutive 1s in a binary array

Approach:
- Track current consecutive count and max count seen
- Reset count when 0 is encountered
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Finds the maximum number of consecutive 1s in a binary array."""
        count = max_count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0

        return max(max_count, count)


class TestFindMaxConsecutiveOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_example(self):
        """Basic example."""
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)

    def test_all_zeros(self):
        """All zeros."""
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0, 0, 0, 0]), 0)

    def test_all_ones(self):
        """All ones."""
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1, 1, 1]), 4)

    def test_empty_list(self):
        """Empty list."""
        self.assertEqual(self.solution.findMaxConsecutiveOnes([]), 0)

    def test_single_one(self):
        """Single one."""
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1]), 1)


if __name__ == "__main__":
    unittest.main()
