def swap_numbers_diff(a, b):
    a = a - b
    b = a + b
    a = b - a
    return a, b


test_cases = [[1, 2], [10, 3], [4, 4], [1, 0], [7, -4], [-7, -4]]
for case in test_cases:
    print(swap_numbers_diff(case[0], case[1]))
