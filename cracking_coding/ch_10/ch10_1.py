def sorted_merge(a, b):
    index = len(a) - 1
    index_b = len(b) - 1
    index_a = index - index_b - 1

    while index_b >= 0:
        if index_a >= 0 and a[index_a] > b[index_b]:
            a[index] = a[index_a]
            index_a -= 1
        else:
            a[index] = b[index_b]
            index_b -= 1
        index -= 1
    return a


a = [9, 10, 11, 12, 13, 0, 0, 0, 0]
b = [4, 5, 6, 7]
print(sorted_merge(a, b))
