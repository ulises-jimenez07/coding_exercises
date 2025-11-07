def magic_index(array, min_index=0, max_index=None):
    if max_index is None:
        max_index = len(array) - 1

    if max_index < min_index:
        return -1

    mid = (max_index + min_index) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return magic_index(array, mid + 1, max_index)
    else:
        return magic_index(array, min_index, mid - 1)


test_cases = [
    ([-14, -12, 0, 1, 2, 5, 9, 10, 23, 25], 5),
    ([-14, -12, 0, 1, 2, 7, 9, 10, 23, 25], -1),
    ([0, 1, 2, 3, 4], 2),
    ([], -1),
]


for array, expected in test_cases:
    print(magic_index(array))


def magic_index_not_distinct(array, min_index=0, max_index=None):
    if max_index is None:
        max_index = len(array) - 1

    if max_index < min_index:
        return -1

    mid = (max_index + min_index) // 2
    if array[mid] == mid:
        return mid

    left_index = min(mid - 1, array[mid])
    left = magic_index_not_distinct(array, min_index, left_index)

    if left >= 0:
        return left

    right_index = max(array[mid], mid + 1)
    return magic_index_not_distinct(array, right_index, max_index)


followup_test_cases = test_cases + [
    ([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13], 2),
]


for array, expected in followup_test_cases:
    print(magic_index_not_distinct(array))
