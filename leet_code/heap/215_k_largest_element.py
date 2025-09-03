import heapq
import unittest
from typing import List


class Solution:
    """
    Finds the k-th largest element in an array using a min-heap.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Calculates the k-th largest element efficiently.

        Args:
            nums: A list of integers.
            k: The k-th position to find.

        Returns:
            The k-th largest element.
        """
        # Create a min-heap from the first 'k' elements of the array.
        # This heap will store the 'k' largest elements seen so far.
        arr = nums[0:k]
        heapq.heapify(arr)

        # Iterate through the rest of the array.
        for i in range(k, len(nums)):
            # If the current element is greater than the smallest element in the heap (the root),
            # it means this new element should be part of our top 'k' list.
            if nums[i] > arr[0]:
                # Push the new element onto the heap.
                heapq.heappush(arr, nums[i])
                # Remove the smallest element from the heap (the old root).
                # This maintains the heap size at 'k' and keeps it as a min-heap of the largest elements.
                heapq.heappop(arr)

        # The root of the min-heap is now the k-th largest element.
        return arr[0]


# --- Unit Tests ---
class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def test_basic_cases(self):
        """
        Tests with typical arrays.
        """
        s = Solution()
        self.assertEqual(s.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_single_element(self):
        """
        Tests with an array of a single element.
        """
        s = Solution()
        self.assertEqual(s.findKthLargest([1], 1), 1)

    def test_duplicates(self):
        """
        Tests with an array containing duplicate elements.
        """
        s = Solution()
        self.assertEqual(s.findKthLargest([5, 5, 5, 5, 5], 3), 5)
        self.assertEqual(s.findKthLargest([1, 1, 2, 2, 3, 3], 2), 3)

    def test_negative_numbers(self):
        """
        Tests with arrays containing negative numbers.
        """
        s = Solution()
        self.assertEqual(s.findKthLargest([-1, -2, -3, -4, -5], 2), -2)
        self.assertEqual(s.findKthLargest([1, -1, 2, -2, 3, -3], 3), 1)

    def test_large_k_value(self):
        """
        Tests with a large value for k.
        """
        s = Solution()
        self.assertEqual(s.findKthLargest([10, 20, 30, 40, 50], 5), 10)


if __name__ == "__main__":
    unittest.main()
