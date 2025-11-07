import unittest
from typing import List


class Solution:
    def mergeSort(self, arr: List[int]) -> None:
        if not arr:
            return
        self._mergeSort_recursive(arr, 0, len(arr) - 1)

    def _mergeSort_recursive(self, arr: List[int], left: int, right: int) -> None:
        if left < right:
            mid = (left + right) // 2
            self._mergeSort_recursive(arr, left, mid)
            self._mergeSort_recursive(arr, mid + 1, right)
            self._merge(arr, left, mid, right)

    def _merge(self, arr: List[int], start: int, mid: int, end: int) -> None:
        i = start
        j = mid + 1
        k = 0
        temp = [0] * (end - start + 1)

        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j <= end:
            temp[k] = arr[j]
            j += 1
            k += 1

        for i in range(len(temp)):
            arr[start + i] = temp[i]


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        """Test with an empty list."""
        arr = []
        self.solution.mergeSort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        """Test with an already sorted list."""
        arr = [1, 2, 3, 4, 5]
        self.solution.mergeSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """Test with a reverse sorted list."""
        arr = [5, 4, 3, 2, 1]
        self.solution.mergeSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        """Test with a general unsorted list."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.solution.mergeSort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate elements."""
        arr = [5, 1, 4, 2, 8, 1]
        self.solution.mergeSort(arr)
        self.assertEqual(arr, [1, 1, 2, 4, 5, 8])

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        arr = [42]
        self.solution.mergeSort(arr)
        self.assertEqual(arr, [42])

    def test_list_with_zeros(self):
        """Test with a list containing zero."""
        arr = [0, 5, 1, 2, 0, 3]
        self.solution.mergeSort(arr)
        self.assertEqual(arr, [0, 0, 1, 2, 3, 5])

    def test_list_with_negative_numbers(self):
        """Test with a list containing negative numbers."""
        arr = [-5, -1, -4, -2, -8, -1]
        self.solution.mergeSort(arr)
        self.assertEqual(arr, [-8, -5, -4, -2, -1, -1])

    def test_list_with_mixed_numbers(self):
        """Test with a list containing mixed positive, negative and zero numbers."""
        arr = [-5, 0, 1, -2, 8, -1]
        self.solution.mergeSort(arr)
        self.assertEqual(arr, [-5, -2, -1, 0, 1, 8])


if __name__ == "__main__":
    unittest.main()
