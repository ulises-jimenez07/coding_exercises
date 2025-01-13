import unittest


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Searches for a target value in a sorted 2D matrix.

        The matrix has the following properties:
            - Integers in each row are sorted from left to right.
            - The first integer of each row is greater than the last integer of the previous row.

        Args:
            matrix: A list of lists representing the 2D matrix.
            target: The integer value to search for.

        Returns:
            True if the target is found in the matrix, False otherwise.
        """
        top = 0
        bot = len(matrix) - 1

        # Binary search to find the potential row
        while top <= bot:
            mid = (top + bot) // 2
            if (
                matrix[mid][0] <= target <= matrix[mid][-1]
            ):  # Check if target falls within the row's range
                break  # Found potential row
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1

        row = (top + bot) // 2
        # Check if the calculated row index is valid.
        # This is particularly important when the target is not in any rows, such as when the matrix is empty.
        if not (0 <= row < len(matrix)):
            return False

        left = 0
        right = len(matrix[row]) - 1

        # Binary search within the row
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
    def test_empty_matrix(self):
        self.assertFalse(Solution().searchMatrix([], 5))

    def test_target_present(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(Solution().searchMatrix(matrix, 3))
        self.assertTrue(Solution().searchMatrix(matrix, 11))
        self.assertTrue(Solution().searchMatrix(matrix, 60))

    def test_target_absent(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

        self.assertFalse(Solution().searchMatrix(matrix, 13))
        self.assertFalse(
            Solution().searchMatrix(matrix, 0)
        )  # Test value less than first element
        self.assertFalse(
            Solution().searchMatrix(matrix, 70)
        )  # Test value greater than last element

    def test_single_row_matrix(self):
        matrix = [[1, 3, 5, 7]]
        self.assertTrue(Solution().searchMatrix(matrix, 3))
        self.assertFalse(Solution().searchMatrix(matrix, 0))

    def test_single_element_matrix(self):
        matrix = [[5]]
        self.assertTrue(Solution().searchMatrix(matrix, 5))
        self.assertFalse(Solution().searchMatrix(matrix, 3))

    def test_target_first_element(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(Solution().searchMatrix(matrix, 1))
        self.assertTrue(Solution().searchMatrix(matrix, 10))
        self.assertTrue(Solution().searchMatrix(matrix, 23))


if __name__ == "__main__":
    unittest.main()
