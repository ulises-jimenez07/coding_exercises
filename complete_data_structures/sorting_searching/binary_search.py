def binary_search(array, value):
    start = 0
    end = len(array) - 1
    middle = (start + end) // 2
    while not array[middle] == value and start <= end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start + end) // 2
    if array[middle] == value:
        return middle
    return -1


cust_array = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binary_search(cust_array, 15))


# O (logN)
