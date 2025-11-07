import unittest
from typing import List


class Solution:
    def quickSort(self, arr: List[int]) -> None:
        if not arr:
            return
        self._quickSort_recursive(arr, 0, len(arr) - 1)

    def _quickSort_recursive(self, arr: List[int], low: int, high: int) -> None:
        if low < high:
            # pi is partitioning index, arr[pi] is now at right place
            pi = self._partition(arr, low, high)

            # Separately sort elements before partition and after partition
            self._quickSort_recursive(arr, low, pi - 1)
            self._quickSort_recursive(arr, pi + 1, high)

    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]  # pivot
        i = low - 1  # Index of smaller element

        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # swap

        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap pivot to its correct position
        return i + 1


class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        """Test with an empty list."""
        arr = []
        self.solution.quickSort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        """Test with an already sorted list."""
        arr = [1, 2, 3, 4, 5]
        self.solution.quickSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """Test with a reverse sorted list."""
        arr = [5, 4, 3, 2, 1]
        self.solution.quickSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        """Test with a general unsorted list."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.solution.quickSort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate elements."""
        arr = [5, 1, 4, 2, 8, 1]
        self.solution.quickSort(arr)
        self.assertEqual(arr, [1, 1, 2, 4, 5, 8])

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        arr = [42]
        self.solution.quickSort(arr)
        self.assertEqual(arr, [42])

    def test_list_with_zeros(self):
        """Test with a list containing zero."""
        arr = [0, 5, 1, 2, 0, 3]
        self.solution.quickSort(arr)
        self.assertEqual(arr, [0, 0, 1, 2, 3, 5])

    def test_list_with_negative_numbers(self):
        """Test with a list containing negative numbers."""
        arr = [-5, -1, -4, -2, -8, -1]
        self.solution.quickSort(arr)
        self.assertEqual(arr, [-8, -5, -4, -2, -1, -1])

    def test_list_with_mixed_numbers(self):
        """Test with a list containing mixed positive, negative and zero numbers."""
        arr = [-5, 0, 1, -2, 8, -1]
        self.solution.quickSort(arr)
        self.assertEqual(arr, [-5, -2, -1, 0, 1, 8])


if __name__ == "__main__":
    unittest.main()
