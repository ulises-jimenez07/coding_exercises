"""
Problem: Find the kth largest element in an unsorted array.

Approach:
- Use a min-heap of size k to track the k largest elements
- Maintain heap by removing smaller elements as we iterate
- Time complexity: O(n log k)
- Space complexity: O(k)
"""

import heapq
import unittest
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Build min-heap with first k elements
        arr = nums[0:k]
        heapq.heapify(arr)

        # Process remaining elements
        for i in range(k, len(nums)):
            # Replace root if current element is larger
            if nums[i] > arr[0]:
                heapq.heappush(arr, nums[i])
                heapq.heappop(arr)

        # Root contains kth largest
        return arr[0]


# --- Unit Tests ---
class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def setUp(self):
        self.solution = Solution()

    def test_basic_cases(self):
        """
        Tests with typical arrays.
        """
        self.assertEqual(self.solution.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(self.solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_single_element(self):
        """
        Tests with an array of a single element.
        """
        self.assertEqual(self.solution.findKthLargest([1], 1), 1)

    def test_duplicates(self):
        """
        Tests with an array containing duplicate elements.
        """
        self.assertEqual(self.solution.findKthLargest([5, 5, 5, 5, 5], 3), 5)
        self.assertEqual(self.solution.findKthLargest([1, 1, 2, 2, 3, 3], 2), 3)

    def test_negative_numbers(self):
        """
        Tests with arrays containing negative numbers.
        """
        self.assertEqual(self.solution.findKthLargest([-1, -2, -3, -4, -5], 2), -2)
        self.assertEqual(self.solution.findKthLargest([1, -1, 2, -2, 3, -3], 3), 1)

    def test_large_k_value(self):
        """
        Tests with a large value for k.
        """
        self.assertEqual(self.solution.findKthLargest([10, 20, 30, 40, 50], 5), 10)


if __name__ == "__main__":
    unittest.main()
