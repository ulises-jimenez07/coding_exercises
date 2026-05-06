"""
Problem: Find the kth smallest element in a sorted matrix.

Approach:
- Binary search on value range (matrix[0][0] to matrix[n-1][n-1]), not array indices
- Count elements <= mid; if count >= k, the element is in the lower half
- Time complexity: O(n log(max_val - min_val))
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Provides a method to find the kth smallest element in a sorted matrix."""

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Finds the kth smallest element in an n x n matrix where each row and column
        is sorted in ascending order.
        """
        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]

        def count_less_equal(target):
            """Counts how many numbers in the matrix are less than or equal to target."""
            col, row = 0, n - 1
            count = 0

            # Start from bottom-left corner
            while 0 <= row and col < n:
                if matrix[row][col] <= target:
                    # All elements in this column up to the current row are <= target
                    count += row + 1
                    col += 1
                else:
                    row -= 1

            return count

        while left < right:
            mid = (right + left) // 2

            # If there are at least k elements <= mid, answer is <= mid
            if count_less_equal(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return right


# --- Unit Tests ---


class TestKthSmallest(unittest.TestCase):
    """
    Unit tests for the kthSmallest method in the Solution class.
    """

    def setUp(self):
        self.sol = Solution()

    def test_basic_matrix(self):
        """Tests a basic case with a 3x3 matrix."""
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        k = 8
        self.assertEqual(self.sol.kthSmallest(matrix, k), 13)

    def test_single_element(self):
        """Tests a case with a 1x1 matrix."""
        matrix = [[-5]]
        k = 1
        self.assertEqual(self.sol.kthSmallest(matrix, k), -5)

    def test_duplicate_elements(self):
        """Tests a case with duplicate elements in the matrix."""
        matrix = [[1, 2], [1, 3]]
        k = 2
        self.assertEqual(self.sol.kthSmallest(matrix, k), 1)

    def test_larger_matrix(self):
        """Tests a larger matrix with k=1."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 1
        self.assertEqual(self.sol.kthSmallest(matrix, k), 1)

    def test_largest_element(self):
        """Tests finding the largest element in the matrix."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 9
        self.assertEqual(self.sol.kthSmallest(matrix, k), 9)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
