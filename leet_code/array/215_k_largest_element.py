"""
Problem: Find the kth largest element in an unsorted array

Approach:
- Use min heap of size k to track k largest elements
- Keep heap size at k by removing smallest when exceeding
- Time complexity: O(n log k)
- Space complexity: O(k)
"""

import heapq
import unittest
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int | None:
        if not nums:
            return None
        if k > len(nums) or k < 0:
            return None

        heap: list[int] = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


class TestFindKthLargest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertIsNone(self.solution.findKthLargest([], 1))

    def test_k_larger_than_list_size(self):
        self.assertIsNone(self.solution.findKthLargest([1, 2, 3], 4))

    def test_basic_example(self):
        self.assertEqual(self.solution.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_duplicate_numbers(self):
        nums_with_duplicates = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        self.assertEqual(self.solution.findKthLargest(nums_with_duplicates, 4), 4)

    def test_all_same_numbers(self):
        self.assertEqual(self.solution.findKthLargest([5, 5, 5, 5, 5], 2), 5)

    def test_k_equals_1(self):
        self.assertEqual(self.solution.findKthLargest([1, 2, 3, 4, 5], 1), 5)

    def test_k_equals_list_size(self):
        self.assertEqual(self.solution.findKthLargest([1, 2, 3, 4, 5], 5), 1)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.findKthLargest([-1, -2, -3, -4, -5], 2), -2)


if __name__ == "__main__":
    unittest.main()
