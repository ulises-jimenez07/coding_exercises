def number_of_paths(two_d_array, row, col, cost):
    if cost < 0:
        return 0
    if row == 0 and col == 0:
        if two_d_array[0][0] - cost == 0:
            return 1
        else:
            return 0
    if row == 0:
        return number_of_paths(two_d_array, row, col - 1, cost - two_d_array[row][col])
    if col == 0:
        return number_of_paths(two_d_array, row - 1, col, cost - two_d_array[row][col])

    op1 = number_of_paths(two_d_array, row - 1, col, cost - two_d_array[row][col])
    op2 = number_of_paths(two_d_array, row, col - 1, cost - two_d_array[row][col])
    return op1 + op2


TwoDList = [[4, 7, 1, 6], [5, 7, 3, 9], [3, 2, 1, 2], [7, 1, 6, 3]]

print(number_of_paths(TwoDList, 3, 3, 25))
