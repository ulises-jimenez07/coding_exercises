class Solution(object):
    dx = [0, 0, -1, 1]  # Possible moves in x-direction (right, left, up, down)
    dy = [1, -1, 0, 0]  # Possible moves in y-direction (right, left, up, down)

    def exist(self, board, word):
        """
        Checks if a given word exists in a 2D board of characters.

        Args:
            board: A list of lists of characters representing the board.
            word: The word to search for.

        Returns:
            True if the word exists in the board, False otherwise.
        """
        if len(word) == 0:  # Empty word always exists
            return True

        rows = len(board)
        for i in range(rows):
            cols = len(board[i])
            for j in range(cols):
                # Check if the first letter matches and start backtracking
                if word[0] == board[i][j] and self.back_tracking(board, word, i, j, ""):
                    return True
        return False  # Word not found after checking all starting points

    def back_tracking(self, board, word, x, y, curr):
        """
        Recursive backtracking helper function to explore the board.

        Args:
            board: The 2D board.
            word: The word to search for.
            x: The current row index.
            y: The current column index.
            curr: The current string being built.

        Returns:
            True if the word is found from the current position, False otherwise.
        """

        # Base cases for invalid moves or exceeding boundaries
        if (
            x < 0
            or x >= len(board)
            or y < 0
            or y >= len(board[x])
            or board[x][y] == " "
        ):
            return False

        curr += board[x][y]  # Add the current character to the string

        if len(curr) > len(word):  # Current string is longer than the target word
            return False

        if curr[len(curr) - 1] != word[len(curr) - 1]:  # Characters don't match
            return False

        if curr == word:  # Found the word
            return True

        temp = board[x][y]  # Store the original character
        board[x][y] = " "  # Mark the cell as visited

        # Explore adjacent cells
        for i in range(4):
            if self.back_tracking(board, word, x + self.dx[i], y + self.dy[i], curr):
                return True  # Word found from one of the adjacent cells

        board[x][y] = temp  # Backtrack: Restore the original character
        return False  # Word not found from this path


# Test cases
solution = Solution()

# Test case 1: Word exists
board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word1 = "ABCEFSADEESE"
print(solution.exist(board1, word1))  # Output: True

# Test case 2: Word doesn't exist
board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word2 = "ABCB"
print(solution.exist(board2, word2))  # Output: False

# Test case 3: Empty word
board3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word3 = ""
print(solution.exist(board3, word3))  # Output: True


# Test case 4: Word exists (See)
board4 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word4 = "SEE"
print(solution.exist(board4, word4))  # Output: True

# Test case 5: Word doesn't exist (ABCCED)
board5 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word5 = "ABCCED"
print(solution.exist(board5, word5))  # Output: True
