import unittest
from typing import List


class Solution:
    def selectionSort(self, arr: List[int]) -> None:
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        """Test with an empty list."""
        arr = []
        self.solution.selectionSort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        """Test with an already sorted list."""
        arr = [1, 2, 3, 4, 5]
        self.solution.selectionSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """Test with a reverse sorted list."""
        arr = [5, 4, 3, 2, 1]
        self.solution.selectionSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        """Test with a general unsorted list."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.solution.selectionSort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate elements."""
        arr = [5, 1, 4, 2, 8, 1]
        self.solution.selectionSort(arr)
        self.assertEqual(arr, [1, 1, 2, 4, 5, 8])

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        arr = [42]
        self.solution.selectionSort(arr)
        self.assertEqual(arr, [42])

    def test_list_with_zeros(self):
        """Test with a list containing zero."""
        arr = [0, 5, 1, 2, 0, 3]
        self.solution.selectionSort(arr)
        self.assertEqual(arr, [0, 0, 1, 2, 3, 5])

    def test_list_with_negative_numbers(self):
        """Test with a list containing negative numbers."""
        arr = [-5, -1, -4, -2, -8, -1]
        self.solution.selectionSort(arr)
        self.assertEqual(arr, [-8, -5, -4, -2, -1, -1])

    def test_list_with_mixed_numbers(self):
        """Test with a list containing mixed positive, negative and zero numbers."""
        arr = [-5, 0, 1, -2, 8, -1]
        self.solution.selectionSort(arr)
        self.assertEqual(arr, [-5, -2, -1, 0, 1, 8])


if __name__ == "__main__":
    unittest.main()
