def binary_search(array, value):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        if value == array[middle]:
            return middle
        elif value < array[middle]:
            if value > array[middle - 1]:
                return middle
            end = middle - 1
        else:
            if value < array[middle + 1]:
                return middle
            start = middle + 1
    return -1


cust_array = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binary_search(cust_array, 15))
