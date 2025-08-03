from typing import List
import unittest

class Solution:
    """
    Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in-place.
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modifies the matrix in-place by setting entire rows and columns to zero
        if any element in that row or column is zero.

        The algorithm uses the first row and first column of the matrix itself
        to store information about which rows and columns need to be zeroed out.
        This avoids using extra space, achieving an O(1) space complexity.

        Args:
            matrix: A list of lists of integers, representing the matrix.
        """

        # flags to track if the first row or first column originally contained a zero
        first_row_has_zero = False
        first_col_has_zero = False

        rows = len(matrix)
        if rows == 0:
            return
        cols = len(matrix[0])
        if cols == 0:
            return

        # Check if the first row has a zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # Check if the first column has a zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Use the first row and first column as markers
        # Iterate from the second row and second column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the corresponding row
                    matrix[0][j] = 0  # Mark the corresponding column

        # Zero out rows and columns based on the markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if it originally had a zero
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        # Zero out the first column if it originally had a zero
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

class TestSolution(unittest.TestCase):
    def test_basic_case(self):
        """
        Test a standard case with zeros in multiple locations.
        """
        solution = Solution()
        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        expected_matrix = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, expected_matrix)

    def test_multiple_zeros(self):
        """
        Test a case with multiple zeros in different rows and columns.
        """
        solution = Solution()
        matrix = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
        expected_matrix = [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, expected_matrix)

    def test_zero_in_first_row_only(self):
        """
        Test a case where the zero is in the first row.
        """
        solution = Solution()
        matrix = [
            [1, 0, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        expected_matrix = [
            [0, 0, 0],
            [1, 0, 1],
            [1, 0, 1]
        ]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, expected_matrix)

    def test_zero_in_first_col_only(self):
        """
        Test a case where the zero is in the first column.
        """
        solution = Solution()
        matrix = [
            [1, 1, 1],
            [0, 1, 1],
            [1, 1, 1]
        ]
        expected_matrix = [
            [0, 1, 1],
            [0, 0, 0],
            [0, 1, 1]
        ]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, expected_matrix)

    def test_zero_at_0_0(self):
        """
        Test a case where the zero is at matrix[0][0].
        """
        solution = Solution()
        matrix = [
            [0, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        expected_matrix = [
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 1]
        ]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, expected_matrix)

    def test_empty_matrix(self):
        """
        Test an empty matrix.
        """
        solution = Solution()
        matrix = []
        expected_matrix = []
        solution.setZeroes(matrix)
        self.assertEqual(matrix, expected_matrix)

    def test_single_element_matrix(self):
        """
        Test a single-element matrix.
        """
        solution = Solution()
        matrix = [[5]]
        expected_matrix = [[5]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, expected_matrix)

    def test_single_element_zero_matrix(self):
        """
        Test a single-element matrix with a zero.
        """
        solution = Solution()
        matrix = [[0]]
        expected_matrix = [[0]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, expected_matrix)
    
    def test_zero_in_first_row_and_first_col(self):
        """
        Test a case where there are zeros in both the first row and first column
        (but not necessarily at [0][0]).
        """
        solution = Solution()
        matrix = [
            [1, 1, 0],
            [1, 1, 1],
            [0, 1, 1]
        ]
        expected_matrix = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, expected_matrix)

if __name__ == '__main__':
    unittest.main()