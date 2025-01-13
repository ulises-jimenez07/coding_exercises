def linear_search(array, value):
    for i, _ in enumerate(array):
        if array[i] == value:
            return i
    return -1


print(linear_search([20, 30, 40, 50, 90], 50))
