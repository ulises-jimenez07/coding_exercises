from typing import (
    Optional,
    Sequence,
)


def search_rotated(array: Sequence[int], num: int) -> Optional[int]:
    if not array:
        return None
    return _recursive_search(array, num, 0, len(array) - 1)


def _recursive_search(array, num, start, end):
    middle = (end - start) // 2 + start

    if array[middle] == num:
        return middle
    if end - start <= 0:
        return None

    result = None

    if array[start] < array[middle]:  # left side is normal
        if array[start] <= num < array[middle]:
            result = _recursive_search(array, num, start, middle - 1)
        else:
            result = _recursive_search(array, num, middle + 1, end)
    elif array[end] > array[middle]:  # right side es normal
        if array[middle] < num <= array[end]:
            result = _recursive_search(array, num, middle + 1, end)
        else:
            result = _recursive_search(array, num, start, middle - 1)
    else:
        if array[middle] != array[end]:
            result = _recursive_search(array, num, middle + 1, end)
        else:
            result = _recursive_search(array, num, start, middle - 1)
            if result is None:
                result = _recursive_search(array, num, middle + 1, end)

    return result


# test_cases = [
#     # array, target, valid solutions
#     ([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5, 8),
#     ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 2, {0, 3, 4, 5, 6, 7, 8, 9}),
#     ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 3, 1),
#     ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 4, None),
#     ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 1, 2),
#     ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 8, None),
# ]

# testable_functions = [search_rotated]


# def test_index():
#     for array, target, expected in test_cases:
#         for method in testable_functions:
#             ind = method(array, target)
#             if isinstance(expected, set):
#                 assert ind in expected
#             else:
#                 error_msg = f"arr:{array} target:{target} calculated:{ind} expected:{expected}"
#                 assert ind == expected, error_msg


# if __name__ == "__main__":
#     test_index()

test_cases = [
    # array, target, valid solutions
    ([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 2),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 3),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 4),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 1),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 8),
]

for test in test_cases:
    print(search_rotated(test[0], test[1]))
