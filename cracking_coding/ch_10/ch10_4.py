def sorted_nosize_search(listy, num):
    exp_off = index = 0
    limit = False
    while not limit:
        try:
            temp = listy[index]
            if temp > num:
                limit = True
            else:
                index = 2**exp_off
                exp_off += 1
        except:
            limit = True
    return bi_search(listy, num, index // 2, index)


def bi_search(listy, num, low, high):
    while low <= high:
        middle = (high + low) // 2
        try:
            value_at = listy[middle]
        except:
            value_at = -1
        if num < value_at or value_at == -1:
            high = middle - 1
        elif num > value_at:
            low = middle + 1
        else:
            return middle
    return -1


test_cases = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 6),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 7),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
]

for test in test_cases:
    print(sorted_nosize_search(test[0], test[1]))
