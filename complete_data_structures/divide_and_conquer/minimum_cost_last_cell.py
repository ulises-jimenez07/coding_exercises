def find_min_cost(two_d_array, row, col):
    if row == -1 or col == -1:
        return float("inf")
    if row == 0 and col == 0:
        return two_d_array[row][col]
    op1 = find_min_cost(two_d_array, row - 1, col)
    op2 = find_min_cost(two_d_array, row, col - 1)
    return two_d_array[row][col] + min(op1, op2)


TwoDList = [[4, 7, 8, 6, 4], [6, 7, 3, 9, 2], [3, 8, 1, 2, 4], [7, 1, 7, 3, 7], [2, 9, 8, 9, 3]]

print(find_min_cost(TwoDList, 4, 4))
