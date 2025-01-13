import heapq
import unittest
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the kth largest element in an unsorted integer array.

        Uses a min-heap to efficiently track the k largest elements encountered so far.

        Args:
            nums: The input list of integers.
            k: The desired kth largest element (1-indexed).

        Returns:
            The kth largest element in nums.
            Returns None if nums is empty or k is invalid.
        """
        if not nums:  # Handle empty input
            return None
        if k > len(nums) or k < 0:  # Handle invalid k values
            return None

        heap = []  # Initialize a min-heap
        for num in nums:
            heapq.heappush(heap, num)  # Add element to the heap
            if len(heap) > k:  # Maintain heap size at most k
                heapq.heappop(
                    heap
                )  # Remove the smallest element if heap size exceeds k

        return heap[0]  # The smallest element in the heap is the kth largest


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
        self.assertEqual(
            self.solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4
        )

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
