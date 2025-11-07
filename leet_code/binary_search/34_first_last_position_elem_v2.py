"""
Problem: Find frequency of a number in a sorted array

Approach:
- Find leftmost and rightmost positions using binary search
- Calculate frequency as (right - left + 1)
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest


def sortedFrequency(arr, num):
    left_index = search_left(arr, num)
    right_index = search_right(arr, num)
    if left_index == -1 or right_index == -1:
        return -1
    return right_index - left_index + 1


def search_left(arr, num):
    # Find leftmost occurrence
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == num:
            if mid == 0 or arr[mid - 1] != num:
                result = mid
            right = mid - 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return result


def search_right(arr, num):
    # Find rightmost occurrence
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == num:
            if mid == len(arr) - 1 or arr[mid + 1] != num:
                result = mid
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return result


class TestSortedFrequency(unittest.TestCase):

    def test_sorted_frequency(self):
        self.assertEqual(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 2), 4)
        self.assertEqual(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 3), 1)
        self.assertEqual(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 1), 2)
        self.assertEqual(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 4), -1)
        self.assertEqual(sortedFrequency([], 1), -1)
        self.assertEqual(sortedFrequency([1, 2, 3, 4, 5], 3), 1)
        self.assertEqual(sortedFrequency([5, 5, 5, 5, 5], 5), 5)


if __name__ == "__main__":
    unittest.main()
