import heapq
import unittest
from typing import List
from collections import Counter # Imported for cleaner unittest setup, but not used in the Solution class logic

class Solution:
    """
    Implements a method to find the k most frequent elements in an array of integers 'nums'.
    It uses a min-heap to efficiently track the k largest frequencies encountered so far.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements using a frequency map and a min-heap.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The number of most frequent elements to return.

        Returns:
            List[int]: A list containing the k most frequent elements.
        """
        # Edge case: If k is equal to the total number of unique elements, return all elements.
        # Note: This is a safe guard, but based on constraints, k is usually smaller.
        if k == len(nums):
            return nums
        
        # --- Step 1: Count Frequencies ---
        # Initialize a dictionary to store the frequency of each number.
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        # --- Step 2: Use a Min-Heap (Priority Queue) ---
        # Initialize an empty list to be used as a min-heap.
        # This heap will maintain the k elements with the smallest frequencies 
        # among the currently observed top k, ensuring the overall k most frequent 
        # elements remain. The heap stores tuples: (frequency, number).
        heap = []
        for num, freq in counter.items():
            # Add the (frequency, number) pair to the min-heap.
            heapq.heappush(heap, (freq, num))
            
            # If the size of the heap exceeds k, remove the smallest element.
            # Since it's a min-heap, this removes the element with the lowest frequency 
            # (i.e., the one that is NOT among the top k).
            if len(heap) > k:
                heapq.heappop(heap)
        
        # --- Step 3: Extract Results ---
        # Extract just the numbers from the remaining (freq, num) tuples in the heap.
        res = [num for (freq, num) in heap]

        # The result list contains the k most frequent elements.
        return res

# --- Unit Tests ---

class TestTopKFrequent(unittest.TestCase):
    """
    Unit tests for the topKFrequent method in the Solution class.
    """

    def _assert_results(self, result: List[int], expected: List[int], msg: str):
        """Helper to assert that two lists contain the same elements, regardless of order."""
        self.assertCountEqual(result, expected, msg)

    def test_example_one(self):
        """Standard test case with clear top k elements."""
        solution = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        # Frequencies: 1:3, 2:2, 3:1. Top 2 are 1 and 2.
        self._assert_results(solution.topKFrequent(nums, k), [1, 2], "Top 2 should be 1 and 2.")

    def test_example_two(self):
        """Test case where k=1."""
        solution = Solution()
        nums = [1]
        k = 1
        # Frequencies: 1:1. Top 1 is 1.
        self._assert_results(solution.topKFrequent(nums, k), [1], "Top 1 should be 1.")

    def test_many_elements_same_freq(self):
        """Test case where many elements have the same frequency."""
        solution = Solution()
        nums = [5, 2, 5, 3, 5, 2, 3, 1]
        k = 2
        # Frequencies: 5:3, 2:2, 3:2, 1:1. Top 2 is 5 and either 2 or 3.
        # The choice between 2 and 3 is implementation-dependent, but both are valid.
        result = solution.topKFrequent(nums, k)
        self.assertEqual(len(result), 2)
        self.assertIn(5, result)
        self.assertTrue(2 in result or 3 in result)
        self.assertNotIn(1, result)

    # CHANGE THE test_k_equals_len_nums METHOD
    def test_k_equals_len_nums(self):
        """Test case where k equals the total number of elements (edge case)."""
        solution = Solution()
        nums = [4, 4, 3, 3, 2, 1]
        k = 6 
        self._assert_results(solution.topKFrequent(nums, k), [4, 4, 3, 3, 2, 1], "Result should be the original list.")

        self._assert_results(solution.topKFrequent(nums, 4), [4, 3, 2, 1], "Result should contain the 4 most frequent elements.")

    def test_large_input(self):
        """Test with a larger, more complex input."""
        solution = Solution()
        nums = [7, 7, 7, 7, 8, 8, 8, 9, 9, 10]
        k = 3
        # Frequencies: 7:4, 8:3, 9:2, 10:1. Top 3 are 7, 8, 9.
        self._assert_results(solution.topKFrequent(nums, k), [7, 8, 9], "Top 3 should be 7, 8, 9.")

if __name__ == '__main__':
    # Run tests only if the script is executed directly
    unittest.main(argv=['first-arg-is-ignored'], exit=False)