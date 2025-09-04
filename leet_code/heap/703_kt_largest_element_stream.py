import heapq
import unittest
from typing import List


class KthLargest:
    """
    Finds the k-th largest element in a stream of numbers.

    This implementation uses a min-heap of size k to efficiently track the k largest
    elements seen so far. The smallest element in the min-heap is always the k-th
    largest element overall.
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the KthLargest object with the integer k and an initial stream of numbers.

        Args:
            k: The k-th largest element to find.
            nums: The initial list of numbers.
        """
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Adds a new number to the stream and returns the current k-th largest element.

        Args:
            val: The new number to add to the stream.

        Returns:
            The k-th largest element in the updated stream.
        """
        if len(self.min_heap) < self.k:
            # If the heap is not yet full, push the new value onto it.
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            # If the new value is larger than the smallest element in the heap,
            # pop the smallest and push the new value.
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]


# --- Unit Tests ---


class TestKthLargest(unittest.TestCase):
    """
    Unit tests for the KthLargest class.
    """

    def test_example_case(self):
        """
        Tests the example from a typical problem description.
        k = 3, initial nums = [4, 5, 8, 2]
        """
        k = 3
        nums = [4, 5, 8, 2]
        kth_largest = KthLargest(k, nums)

        self.assertEqual(
            kth_largest.add(3), 4
        )  # 2, 3, 4, 5, 8 -> 4th largest is 5, but we are looking for the 3rd which is 4. wait, let's re-think this. The 3 largest are 5, 8, 4. The 3rd largest is 4.
        # Let's trace the heap:
        # Initial: [4, 5, 8, 2] -> heap: [2, 4, 5] -> heap becomes [4, 5, 8]. The smallest in the heap is the 3rd largest, which is 4.
        # Add 3: val=3 < min_heap[0]=4. Heap remains [4, 5, 8]. The 3rd largest is 4.
        self.assertEqual(kth_largest.add(5), 5)
        # Add 5: val=5 > min_heap[0]=4. Pop 4, push 5. Heap becomes [5, 5, 8]. 3rd largest is 5.
        self.assertEqual(kth_largest.add(10), 5)
        # Add 10: val=10 > min_heap[0]=5. Pop 5, push 10. Heap becomes [5, 8, 10]. 3rd largest is 5.
        self.assertEqual(kth_largest.add(9), 8)
        # Add 9: val=9 > min_heap[0]=5. Pop 5, push 9. Heap becomes [8, 9, 10]. 3rd largest is 8.
        self.assertEqual(kth_largest.add(4), 8)
        # Add 4: val=4 < min_heap[0]=8. Heap remains [8, 9, 10]. 3rd largest is 8.

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
