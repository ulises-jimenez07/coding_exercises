"""Module for finding minimum days to make m bouquets."""

import unittest
from typing import List


class Solution:
    """Find minimum days to make m bouquets with k flowers each."""

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """Calculate minimum days to harvest enough bouquets."""

        def get_num_of_bouquets(mid):
            """Count total bouquets possible by day 'mid'."""
            num_of_bouquets = 0
            count = 0

            # Iterate through flowers to check consecutive bloom status
            for day in bloomDay:
                if day <= mid:
                    count += 1
                else:
                    count = 0
                if count == k:
                    num_of_bouquets += 1
                    count = 0
            return num_of_bouquets

        # Check if enough flowers exist in total
        if m * k > len(bloomDay):
            return -1

        # Binary search range: from 1 day to maximum bloom day
        start = 1
        end = max(bloomDay)
        min_days = -1

        while start <= end:
            mid = (start + end) // 2
            if get_num_of_bouquets(mid) >= m:
                min_days = mid
                end = mid - 1
            else:
                start = mid + 1

        return min_days


class TestMinDays(unittest.TestCase):
    """Unit tests for the Minimum Days to Make Bouquets solution."""

    def test_examples(self):
        """Standard LeetCode examples."""
        solution = Solution()
        test_cases = [([1, 10, 3, 10, 2], 3, 1, 3), ([1, 10, 3, 10, 2], 3, 2, -1), ([7, 7, 7, 7, 12, 7, 7], 2, 3, 12)]
        for i, (bloom_day, m, k, expected) in enumerate(test_cases):
            with self.subTest(case=i):
                self.assertEqual(solution.minDays(bloom_day, m, k), expected)

    def test_empty_list(self):
        """Case with empty bloomDay list."""
        solution = Solution()
        self.assertEqual(solution.minDays([], 1, 1), -1)

    def test_single_element(self):
        """Case with single element."""
        solution = Solution()
        self.assertEqual(solution.minDays([1], 1, 1), 1)
        self.assertEqual(solution.minDays([1], 1, 2), -1)

    def test_not_enough_flowers(self):
        """Case where total flowers are less than required."""
        solution = Solution()
        self.assertEqual(solution.minDays([1, 2, 3], 2, 2), -1)


if __name__ == "__main__":
    unittest.main()
