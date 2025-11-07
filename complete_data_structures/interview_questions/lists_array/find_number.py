import numpy as np

myArray = np.array([1, 2, 3, 6, 4, 5, 5, 5])


def findNumber(array, number):
    """Finds the index of a number in an array."""
    for i in range(len(array)):
        if array[i] == number:
            print(i)


def max_product(arr):
    """Finds the maximum product of two elements in an array."""
    max1 = max2 = 0
    for elem in arr:
        if elem > max1:
            max2 = max1
            max1 = elem
        elif elem > max2:
            max2 = elem
    return max1 * max2


arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))
