# write and algorigm that every time we see a cell with value zero
# set the row to value zero
def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    # sets of zero columns and zero row
    rows = set()
    cols = set()

    # look for zeros first
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # tranverse the matrix and if the cell
    # is in the zero row or column set it to zero
    for i in range(m):
        for j in range(n):
            if (i in rows) or (j in cols):
                matrix[i][j] = 0

    return matrix


print(
    zero_matrix([[1, 2, 3, 4, 0], [6, 0, 8, 9, 10], [11, 12, 13, 14, 15], [16, 0, 18, 19, 20], [21, 22, 23, 24, 25]])
)
