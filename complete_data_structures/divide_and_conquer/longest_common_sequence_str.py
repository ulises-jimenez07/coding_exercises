# Function to find LCS of X[0..m-1] and Y[0..n-1]
def LCS(X, Y, m, n, T):

    # return empty string if we have reached the end of
    # either sequence
    if m == 0 or n == 0:
        return str()

    # if last character of X and Y matches
    if X[m - 1] == Y[n - 1]:
        # append current character (X[m-1] or Y[n-1]) to LCS of
        # substring X[0..m-2] and Y[0..n-2]
        return LCS(X, Y, m - 1, n - 1, T) + X[m - 1]

    # else when the last character of X and Y are different

    # if top cell of current cell has more value than the left
    # cell, then drop current character of X and find LCS
    # of substring X[0..m-2], Y[0..n-1]

    if T[m - 1][n] > T[m][n - 1]:
        return LCS(X, Y, m - 1, n, T)
    # if left cell of current cell has more value than the top
    # cell, then drop current character of Y and find LCS
    # of substring X[0..m-1], Y[0..n-2]
    return LCS(X, Y, m, n - 1, T)


# Function to fill lookup table by finding the length of LCS
# of substring X[0..m-1] and Y[0..n-1]
def LCSLength(X, Y, m, n, T):

    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # else if current character of X and Y don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])


X = "ABCBDAB"
Y = "BDCABA"
m = len(X)
n = len(Y)

# T[i][j] stores the length of LCS of substring X[0..i-1], Y[0..j-1]
T = [[0 for x in range(n + 1)] for y in range(m + 1)]

# fill lookup table
LCSLength(X, Y, m, n, T)
print(T)

# find longest common sequence

print(LCS(X, Y, m, n, T))
