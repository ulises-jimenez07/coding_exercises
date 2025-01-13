import unittest


class Solution(object):
    def uniquePaths(self, m, n):
        """
        A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

        The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

        How many possible unique paths are there?

        :type m: int
        :type n: int
        :rtype: int
        """
        # Create a 2D array to store the number of ways to reach each cell
        ways = [[0] * n for _ in range(m)]

        # Initialize the first column to 1, as there's only 1 way to reach any cell in the first column
        for i in range(m):
            ways[i][0] = 1

        # Initialize the first row to 1, as there's only 1 way to reach any cell in the first row
        for j in range(n):
            ways[0][j] = 1

        # Iterate through the remaining cells, calculating the number of ways to reach each cell
        # by summing the ways to reach the cell above and the cell to the left
        for i in range(1, m):
            for j in range(1, n):
                ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

        # Return the number of ways to reach the bottom-right cell
        return ways[m - 1][n - 1]


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.uniquePaths(3, 7), 28)

    def test_example_2(self):
        self.assertEqual(self.solution.uniquePaths(3, 2), 3)

    def test_square_grid(self):
        self.assertEqual(self.solution.uniquePaths(3, 3), 6)

    def test_single_row(self):
        self.assertEqual(self.solution.uniquePaths(1, 5), 1)

    def test_single_column(self):
        self.assertEqual(self.solution.uniquePaths(5, 1), 1)

    def test_large_grid(self):
        self.assertEqual(self.solution.uniquePaths(10, 10), 48620)


if __name__ == "__main__":
    unittest.main()
