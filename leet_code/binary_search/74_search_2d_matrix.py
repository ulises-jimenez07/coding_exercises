"""
Problem: Search for a target value in a 2D matrix sorted row-wise and column-wise

Approach:
- First binary search to find the correct row
- Second binary search within that row to find target
- Time complexity: O(log m + log n)
- Space complexity: O(1)
"""

import unittest


class Solution:
    def searchMatrix(self, matrix, target):
        top = 0
        bot = len(matrix) - 1

        # Find the correct row
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1

        row = (top + bot) // 2
        if not (0 <= row < len(matrix)):
            return False

        # Binary search within the row
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


class TestSearchMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_matrix(self):
        self.assertFalse(self.solution.searchMatrix([], 5))

    def test_target_present(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 3))
        self.assertTrue(self.solution.searchMatrix(matrix, 11))
        self.assertTrue(self.solution.searchMatrix(matrix, 60))

    def test_target_absent(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

        self.assertFalse(self.solution.searchMatrix(matrix, 13))
        self.assertFalse(self.solution.searchMatrix(matrix, 0))
        self.assertFalse(self.solution.searchMatrix(matrix, 70))

    def test_single_row_matrix(self):
        matrix = [[1, 3, 5, 7]]
        self.assertTrue(self.solution.searchMatrix(matrix, 3))
        self.assertFalse(self.solution.searchMatrix(matrix, 0))

    def test_single_element_matrix(self):
        matrix = [[5]]
        self.assertTrue(self.solution.searchMatrix(matrix, 5))
        self.assertFalse(self.solution.searchMatrix(matrix, 3))

    def test_target_first_element(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 1))
        self.assertTrue(self.solution.searchMatrix(matrix, 10))
        self.assertTrue(self.solution.searchMatrix(matrix, 23))


if __name__ == "__main__":
    unittest.main()
