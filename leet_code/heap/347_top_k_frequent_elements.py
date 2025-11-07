"""
Problem: Find the k most frequent elements in an array.

Approach:
- Count frequencies using a hash map
- Use a min-heap of size k to track top k frequencies
- Keep heap size at k by removing smallest frequency
- Time complexity: O(n log k)
- Space complexity: O(n)
"""

import heapq
import unittest
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        counter: dict[int, int] = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # Maintain min-heap of size k
        heap: list[tuple[int, int]] = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract numbers from heap
        res = [num for (freq, num) in heap]
        return res


class TestTopKFrequent(unittest.TestCase):
    """
    Unit tests for the topKFrequent method in the Solution class.
    """

    def setUp(self):
        self.solution = Solution()

    def _assert_results(self, result: List[int], expected: List[int], msg: str):
        """Helper to assert that two lists contain the same elements, regardless of order."""
        self.assertCountEqual(result, expected, msg)

    def test_example_one(self):
        """Standard test case with clear top k elements."""
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        self._assert_results(self.solution.topKFrequent(nums, k), [1, 2], "Top 2 should be 1 and 2.")

    def test_example_two(self):
        """Test case where k=1."""
        nums = [1]
        k = 1
        self._assert_results(self.solution.topKFrequent(nums, k), [1], "Top 1 should be 1.")

    def test_many_elements_same_freq(self):
        """Test case where many elements have the same frequency."""
        nums = [5, 2, 5, 3, 5, 2, 3, 1]
        k = 2
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(len(result), 2)
        self.assertIn(5, result)
        self.assertTrue(2 in result or 3 in result)
        self.assertNotIn(1, result)

    def test_k_equals_unique_elements_count(self):
        """Test case where k equals the total number of unique elements."""
        nums = [4, 4, 3, 3, 2, 1]
        k = 4  # There are 4 unique elements: 4, 3, 2, 1
        self._assert_results(
            self.solution.topKFrequent(nums, k), [4, 3, 2, 1], "Result should be all unique elements."
        )

    def test_large_input(self):
        """Test with a larger, more complex input."""
        nums = [7, 7, 7, 7, 8, 8, 8, 9, 9, 10]
        k = 3
        self._assert_results(self.solution.topKFrequent(nums, k), [7, 8, 9], "Top 3 should be 7, 8, 9.")

    def test_k_greater_than_unique_elements(self):
        """Test case where k is greater than the number of unique elements."""
        nums = [1, 1, 2]
        k = 3
        self._assert_results(self.solution.topKFrequent(nums, k), [1, 2], "Should return all unique elements.")


if __name__ == "__main__":
    # Run tests only if the script is executed directly
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
