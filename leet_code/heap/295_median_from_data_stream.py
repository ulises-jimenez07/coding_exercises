import heapq
import unittest


# The MedianFinder class uses two heaps to efficiently find the median of a stream of numbers.
# The class maintains two heaps: a max-heap (implemented using a min-heap with negative values)
# to store the smaller half of the numbers, and a min-heap to store the larger half.
# This ensures that the median can be calculated quickly from the top elements of the heaps.
class MedianFinder:

    # Initializes the two heaps.
    # self.min_heap will store the larger half of the numbers.
    # self.max_heap will store the smaller half of the numbers.
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    # Adds a new number to the data structure.
    # It balances the heaps to maintain the median property.
    def addNum(self, num: int) -> None:
        # Push the new number onto the max-heap (min_heap with negative values).
        # This effectively places it in the smaller half.
        heapq.heappush(self.min_heap, -num)

        # Move the largest element from the max-heap to the min-heap.
        # This ensures the min-heap always contains the largest elements.
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        # If the max-heap has more elements than the min-heap,
        # move the smallest element from the max-heap back to the min-heap
        # to maintain a balanced size (or with at most one more element in the min-heap).
        if len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    # Finds the median of all the numbers added so far.
    def findMedian(self) -> float:
        # If the number of elements is odd, the median is the top element of the min-heap.
        # The min-heap will have one more element than the max-heap.
        if len(self.min_heap) > len(self.max_heap):
            return -self.min_heap[0]
        # If the number of elements is even, the median is the average of the
        # top elements of both heaps.
        else:
            return float(-self.min_heap[0] + self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# ---
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
