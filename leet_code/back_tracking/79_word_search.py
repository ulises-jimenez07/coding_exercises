"""
Problem: Search for a word in a 2D grid using adjacent cells

Approach:
- Use backtracking with DFS to explore all paths
- Mark visited cells temporarily to avoid reuse in same path
- Try all 4 directions (up, down, left, right) from each cell
- Time complexity: O(m*n*4^L) where m,n are grid dimensions, L is word length
- Space complexity: O(L) for recursion stack
"""


class Solution:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def exist(self, board, word):
        if len(word) == 0:
            return True

        rows = len(board)
        # Try starting from each cell
        for i in range(rows):
            cols = len(board[i])
            for j in range(cols):
                if word[0] == board[i][j] and self.back_tracking(board, word, i, j, 0):
                    return True
        return False

    def back_tracking(self, board, word, x, y, k):
        # Found complete word
        if k == len(word):
            return True

        # Check boundaries and character match
        if (
            x < 0
            or x >= len(board)
            or y < 0
            or y >= len(board[x])
            or board[x][y] != word[k]
            or board[x][y] == " "  # Already visited
        ):
            return False

        temp = board[x][y]
        board[x][y] = " "  # Mark visited

        # Try all 4 directions
        for i in range(4):
            if self.back_tracking(board, word, x + self.dx[i], y + self.dy[i], k + 1):
                return True

        board[x][y] = temp  # Backtrack
        return False


import unittest


class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.maxDiff = None

    def test_word_exists(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCEFSADEESE"
        self.assertFalse(self.solution.exist(board, word))

    def test_word_does_not_exist(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        self.assertFalse(self.solution.exist(board, word))

    def test_empty_word(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = ""
        self.assertTrue(self.solution.exist(board, word))

    def test_word_exists_see(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word))

    def test_word_exists_abcced(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        self.assertTrue(self.solution.exist(board, word))


if __name__ == "__main__":
    unittest.main()
