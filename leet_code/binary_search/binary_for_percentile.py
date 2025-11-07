"""
Problem: Binary search variant for finding percentile position in sorted array

Approach:
- Modified binary search to find insertion position for percentile calculation
- Returns index where value fits or closest position
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def binary_search(self, array, value):
        start = 0
        end = len(array) - 1
        while start <= end:
            middle = (start + end) // 2
            if value == array[middle]:
                return middle
            elif value < array[middle]:
                # Check if value fits between previous and current
                if middle > 0 and value > array[middle - 1]:
                    return middle
                end = middle - 1
            else:
                # Check if value fits between current and next
                if middle < len(array) - 1 and value < array[middle + 1]:
                    return middle
                start = middle + 1
        return -1


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_value_found(self):
        cust_array = [8, 9, 12, 15, 17, 19, 20, 21, 28]
        self.assertEqual(self.solution.binary_search(cust_array, 15), 3)
        self.assertEqual(self.solution.binary_search(cust_array, 8), 0)
        self.assertEqual(self.solution.binary_search(cust_array, 28), 8)

    def test_value_not_found(self):
        cust_array = [8, 9, 12, 15, 17, 19, 20, 21, 28]
        # Value 10 fits between 9 and 12 (index 1)
        self.assertEqual(self.solution.binary_search(cust_array, 10), 1)
        # Value 7 is less than minimum
        self.assertEqual(self.solution.binary_search(cust_array, 7), -1)
        # Value 29 is greater than maximum
        self.assertEqual(self.solution.binary_search(cust_array, 29), -1)

    def test_empty_array(self):
        self.assertEqual(self.solution.binary_search([], 5), -1)

    def test_single_element_array(self):
        self.assertEqual(self.solution.binary_search([10], 10), 0)
        self.assertEqual(self.solution.binary_search([10], 5), -1)


if __name__ == "__main__":
    unittest.main()
