import unittest
from typing import List


class Solution:
    def bubbleSort(self, arr: List[int]) -> None:
        n = len(arr)
        for i in range(n):
            # Last i elements are already in place
            for j in range(n - i - 1):
                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        """Test with an empty list."""
        arr = []
        self.solution.bubbleSort(arr)
        self.assertEqual(arr, [])

    def test_sorted_list(self):
        """Test with an already sorted list."""
        arr = [1, 2, 3, 4, 5]
        self.solution.bubbleSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """Test with a reverse sorted list."""
        arr = [5, 4, 3, 2, 1]
        self.solution.bubbleSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        """Test with a general unsorted list."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.solution.bubbleSort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate elements."""
        arr = [5, 1, 4, 2, 8, 1]
        self.solution.bubbleSort(arr)
        self.assertEqual(arr, [1, 1, 2, 4, 5, 8])

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        arr = [42]
        self.solution.bubbleSort(arr)
        self.assertEqual(arr, [42])


if __name__ == "__main__":
    unittest.main()
