import unittest
from typing import List


class Solution:
    def countingSort(self, arr: List[int]) -> None:
        if not arr:
            return

        max_element = max(arr)
        min_element = min(arr)
        range_of_elements = max_element - min_element + 1

        count = [0] * range_of_elements
        output = [0] * len(arr)

        # Store count of each character
        for i in range(len(arr)):
            count[arr[i] - min_element] += 1

        # Store cumulative count
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_element] - 1] = arr[i]
            count[arr[i] - min_element] -= 1

        # Copy the output array to arr, so that arr now contains sorted elements
        for i in range(len(arr)):
            arr[i] = output[i]


class TestCountingSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        """Test with an empty list."""
        arr = []
        self.solution.countingSort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        """Test with an already sorted list."""
        arr = [1, 2, 3, 4, 5]
        self.solution.countingSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """Test with a reverse sorted list."""
        arr = [5, 4, 3, 2, 1]
        self.solution.countingSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        """Test with a general unsorted list."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.solution.countingSort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate elements."""
        arr = [5, 1, 4, 2, 8, 1]
        self.solution.countingSort(arr)
        self.assertEqual(arr, [1, 1, 2, 4, 5, 8])

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        arr = [42]
        self.solution.countingSort(arr)
        self.assertEqual(arr, [42])

    def test_list_with_zeros(self):
        """Test with a list containing zero."""
        arr = [0, 5, 1, 2, 0, 3]
        self.solution.countingSort(arr)
        self.assertEqual(arr, [0, 0, 1, 2, 3, 5])

    def test_list_with_negative_numbers(self):
        """Test with a list containing negative numbers."""
        arr = [-5, -1, -4, -2, -8, -1]
        self.solution.countingSort(arr)
        self.assertEqual(arr, [-8, -5, -4, -2, -1, -1])

    def test_list_with_mixed_numbers(self):
        """Test with a list containing mixed positive, negative and zero numbers."""
        arr = [-5, 0, 1, -2, 8, -1]
        self.solution.countingSort(arr)
        self.assertEqual(arr, [-5, -2, -1, 0, 1, 8])


if __name__ == "__main__":
    unittest.main()
