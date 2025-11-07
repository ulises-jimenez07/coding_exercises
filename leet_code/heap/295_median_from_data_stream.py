"""
Problem: Find the median from a data stream of integers.

Approach:
- Use two heaps: max-heap for smaller half, min-heap for larger half
- Balance heaps to keep sizes within 1 of each other
- Median is either top of larger heap or average of both tops
- Time complexity: O(log n) per add, O(1) for median
- Space complexity: O(n)
"""

import heapq
import unittest


class MedianFinder:
    def __init__(self):
        self.min_heap = []  # Larger half (negated for max-heap)
        self.max_heap = []  # Smaller half

    def addNum(self, num: int) -> None:
        # Add to min_heap first, then balance
        heapq.heappush(self.min_heap, -num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        # Keep min_heap size >= max_heap size
        if len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return -self.min_heap[0]
        return float(-self.min_heap[0] + self.max_heap[0]) / 2


# Unit test for the MedianFinder class.
class TestMedianFinder(unittest.TestCase):

    def test_odd_number_of_elements(self):
        median_finder = MedianFinder()
        median_finder.addNum(1)
        median_finder.addNum(2)
        median_finder.addNum(3)
        self.assertEqual(median_finder.findMedian(), 2.0)

    def test_even_number_of_elements(self):
        median_finder = MedianFinder()
        median_finder.addNum(1)
        median_finder.addNum(2)
        median_finder.addNum(3)
        median_finder.addNum(4)
        self.assertEqual(median_finder.findMedian(), 2.5)

    def test_single_element(self):
        median_finder = MedianFinder()
        median_finder.addNum(5)
        self.assertEqual(median_finder.findMedian(), 5.0)

    def test_negative_numbers(self):
        median_finder = MedianFinder()
        median_finder.addNum(-1)
        median_finder.addNum(-2)
        median_finder.addNum(-3)
        self.assertEqual(median_finder.findMedian(), -2.0)

    def test_mixed_numbers(self):
        median_finder = MedianFinder()
        median_finder.addNum(1)
        median_finder.addNum(-2)
        median_finder.addNum(3)
        median_finder.addNum(-4)
        self.assertEqual(median_finder.findMedian(), -0.5)


if __name__ == "__main__":
    unittest.main()
