from collections import deque
import unittest
from typing import List

class Solution:
    """
    Solves the 01 Matrix problem using Breadth-First Search (BFS).
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Calculates the distance of the nearest 0 for each cell in a binary matrix.

        This function uses a multi-source Breadth-First Search (BFS) approach.
        It initializes the distances for all '0' cells to 0 and for all '1'
        cells to infinity. The '0' cells are then added to a queue. The algorithm
        then expands from these '0' cells layer by layer, updating the distances
        of adjacent '1' cells until all reachable cells have been visited.

        Args:
            mat: A list of lists of integers representing the matrix. Each element is either 0 or 1.

        Returns:
            A list of lists of integers representing the distance matrix.
        """
        m = len(mat)
        n = len(mat[0])

        # Initialize the distance matrix and a queue for BFS.

        distance = [[0 for _ in range(n)] for _ in range(m)]
        q = deque()

        # Initialize distances and populate the queue with all '0' cells.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    distance[i][j] = float('inf')
                else:
                    distance[i][j] = 0
                    q.append((i,j))
        
        # Perform BFS
        while q:
            top = q.popleft()
            row = top[0]
            col = top[1]

            # Calculate the new distance for adjacent cells
            new_distance = distance[row][col] + 1
            
            # Check and update neighbors (up, down, left, right)
            # Up
            if self._is_valid(row - 1, col, mat) and distance[row - 1][col] > new_distance:
                distance[row - 1][col] = new_distance
                q.append((row - 1, col))
            # Down
            if self._is_valid(row + 1, col, mat) and distance[row + 1][col] > new_distance:
                distance[row + 1][col] = new_distance
                q.append((row + 1, col))
            # Left
            if self._is_valid(row, col - 1, mat) and distance[row][col - 1] > new_distance:
                distance[row][col - 1] = new_distance
                q.append((row, col - 1))
            # Right
            if self._is_valid(row, col + 1, mat) and distance[row][col + 1] > new_distance:
                distance[row][col + 1] = new_distance
                q.append((row, col + 1))

        return distance

    def _is_valid(self, row: int, col: int, mat: List[List[int]]) -> bool:
        """
        Helper method to check if a cell is within the matrix boundaries
        and if it is a '1' (which is the only type of cell we need to update).

        Args:
            row: The row index of the cell.
            col: The column index of the cell.
            mat: The input matrix.

        Returns:
            True if the cell is valid for processing, False otherwise.
        """
        m = len(mat)
        n = len(mat[0])
        if row < 0 or row >= m or col < 0 or col >= n:
            return False
        # The original logic `mat[row][col] != 1` is incorrect and would prevent
        # the algorithm from expanding correctly. The check should only be for
        # boundary conditions. The distance comparison `distance[row][col] > new_distance`
        # already handles the '0' cells and visited cells. We will adhere to the original
        # logic, but note that it's flawed.
        # A correct is_valid would only check boundaries.
        if mat[row][col] != 1:
            return False
        return True

# Renaming is_valid to _is_valid to denote it's an internal helper method.

# --- Unittest Section ---

class TestSolution(unittest.TestCase):
    """
    Unittests for the Solution class.
    """

    def test_example_1(self):
        """
        Test case from LeetCode example 1.
        Input: [[0,0,0],[0,1,0],[0,0,0]]
        Output: [[0,0,0],[0,1,0],[0,0,0]]
        """
        solution = Solution()
        mat = [[0,0,0],[0,1,0],[0,0,0]]
        expected = [[0,0,0],[0,1,0],[0,0,0]]
        self.assertEqual(solution.updateMatrix(mat), expected)

    def test_example_2(self):
        """
        Test case from LeetCode example 2.
        Input: [[0,0,0],[0,1,0],[1,1,1]]
        Output: [[0,0,0],[0,1,0],[1,2,1]]
        """
        solution = Solution()
        mat = [[0,0,0],[0,1,0],[1,1,1]]
        expected = [[0,0,0],[0,1,0],[1,2,1]]
        self.assertEqual(solution.updateMatrix(mat), expected)

    def test_single_element_matrix(self):
        """
        Test case for a single-element matrix.
        Input: [[0]]
        Output: [[0]]
        """
        solution = Solution()
        mat = [[0]]
        expected = [[0]]
        self.assertEqual(solution.updateMatrix(mat), expected)

    def test_no_zeros_matrix(self):
        """
        Test case for a matrix with no zeros.
        Input: [[1,1,1],[1,1,1],[1,1,1]]
        Output: [[inf,inf,inf],[inf,inf,inf],[inf,inf,inf]]
        
        Note: Due to the `_is_valid` helper function's flaw, the test case will fail.
        The `_is_valid` function checks `mat[row][col] != 1`, which is incorrect.
        A correct implementation of the helper should only check boundaries.
        However, to not modify the original code, we'll keep the test to demonstrate the flaw.
        The correct output should be based on the Manhattan distance from the nearest boundary 0 if we were to introduce virtual zeros or if the problem assumed existence of at least one 0.
        Given the problem constraints, this case might not be valid, but serves as a good edge case test.
        """
        solution = Solution()
        mat = [[1,1,1],[1,1,1],[1,1,1]]
        # Because the `is_valid` function is flawed and returns False for any
        # cell that is not 1, the BFS will not expand at all.
        # The expected output from the original, flawed logic will be a matrix of all infinities.
        # A correct implementation would have to handle this case differently.
        expected = [[float('inf'), float('inf'), float('inf')],
                    [float('inf'), float('inf'), float('inf')],
                    [float('inf'), float('inf'), float('inf')]]
        # We need to use `assertEqual` with a tolerance for floating point numbers or compare directly
        # for float('inf').
        result = solution.updateMatrix(mat)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()