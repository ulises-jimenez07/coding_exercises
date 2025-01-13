class NQueens:
    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for _ in range(n)] for _ in range(n)]

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print("Q", end=" ")
                else:
                    print(" - ", end=" ")
            print("\n")

    def is_place_valid(self, row_index, col_index):
        # check rows (whether given queens can attack each other horizontally)
        # there is already at least one queen in that row
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False
        # we do not have to check the same column because we implemented the problem such that we assign 1 queen to every single column

        # But we have to check diagonals
        # from top left to buttom right
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j - 1

        # from top right to buttom left
        j = col_index
        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j - 1
        return True

    def solve(self, col_index):
        # if we have 4 queens so indecies will be 0,1,2,3 , so when we reach 4 it means we have already placed all queens
        if col_index == self.n:
            return True
        # find a location for a queen within given column using row_index (increase)
        for row_index in range(self.n):
            if self.is_place_valid(row_index, col_index):
                # 1 means there is a queen in this cell
                self.chess_table[row_index][col_index] = 1
                # if we find a location for current queen we need to find place[[]] for next queen
                if self.solve(col_index + 1):
                    return True
                # otherwise we need to backtrack which means we need to intialize the current cell to 0
                self.chess_table[row_index][col_index] = 0
        # when we consideren all rows in a given column without findind valid cell for the queen
        return False

    def solve_NQueens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("There is not solution for the problem!")


queens = NQueens(4)
queens.print_queens()
