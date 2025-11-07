"""
Problem: Design a class to find the kth largest element in a stream.

Approach:
- Maintain a min-heap of size k with the k largest elements
- Heap root is always the kth largest element
- Add new elements only if larger than root
- Time complexity: O(log k) per add operation
- Space complexity: O(k)
"""

import heapq
import unittest
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap: list[int] = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add to heap if size < k
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # Replace root if val is larger
        elif val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]


class TestKthLargest(unittest.TestCase):
    """
    Unit tests for the KthLargest class.
    """

    def test_example_case(self):
        """
        Tests the example from a typical problem description.
        """
        k = 3
        nums = [4, 5, 8, 2]
        kth_largest = KthLargest(k, nums)

        self.assertEqual(kth_largest.add(3), 4)
        self.assertEqual(kth_largest.add(5), 5)
        self.assertEqual(kth_largest.add(10), 5)
        self.assertEqual(kth_largest.add(9), 8)
        self.assertEqual(kth_largest.add(4), 8)

    def test_empty_initial_list(self):
        """
        Tests with an empty initial list of numbers.
        """
        k = 2
        kth_largest = KthLargest(k, [])
        self.assertEqual(kth_largest.add(10), 10)
        self.assertEqual(kth_largest.add(5), 5)
        self.assertEqual(kth_largest.add(12), 10)
        self.assertEqual(kth_largest.add(3), 10)

    def test_k_equals_1(self):
        """
        Tests the case where k is 1.
        """
        k = 1
        kth_largest = KthLargest(k, [1, 2, 3])
        self.assertEqual(kth_largest.add(4), 4)
        self.assertEqual(kth_largest.add(0), 4)
        self.assertEqual(kth_largest.add(5), 5)

    def test_negative_numbers(self):
        """
        Tests with negative numbers.
        """
        k = 3
        kth_largest = KthLargest(k, [-1, -2, -3])
        self.assertEqual(kth_largest.add(-4), -3)
        self.assertEqual(kth_largest.add(0), -2)


# This allows the tests to be run from the command line
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
