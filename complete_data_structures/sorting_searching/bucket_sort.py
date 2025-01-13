# create buckets and distribute elements of array into buckets
# sort buckets individually
# merg bucket after sorting

import math


def insertion_sort(custom_list):
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i - 1
        while j >= 0 and key < custom_list[j]:
            custom_list[j + 1] = custom_list[j]
            j -= 1
        custom_list[j + 1] = key
    return custom_list


def bucket_sort(custom_list):
    number_of_buckets = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    arr = []

    for i in range(number_of_buckets):
        arr.append([])
    for j in custom_list:
        index_b = math.ceil(j * number_of_buckets / max_value)
        arr[index_b - 1].append(j)

    for i in range(number_of_buckets):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            custom_list[k] = arr[i][j]
            k += 1
    return custom_list


c_list = [2, 1, 7, 8, 9, 3, 2]

print(bucket_sort(c_list))

# numbers uniformly distributed
