def roteate_matrix(matrix):
    n=len(matrix)
    for layer in range(n//2):
        first=layer
        last= n-1-layer
        for i in range(first, last):
            offset=i-first
            top=matrix[first][i]

            #rotate matrix
            matrix[first][i]=matrix[last-offset][first]
            matrix[last-offset][first]=matrix[last][last-offset]
            matrix[last][last-offset]=matrix[i][last]
            matrix[i][last]=top
    return matrix


test_cases = [
    ([[1, 2, 3], 
      [4, 5, 6],
        [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    (
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ],
        [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5],
        ],
    ),
]


#for test in test_cases:
#    print(roteate_matrix(test))

print(roteate_matrix([[1, 2, 3], 
      [4, 5, 6],
        [7, 8, 9]],))

[[7, 4, 1], [8, 5, 2], [9, 6, 3]]