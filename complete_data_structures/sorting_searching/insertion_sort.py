# divide given array into two parts
# take frist element forom unsorted array and find its correct position

# space efficiency


def insertion_sort(custom_list):
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i - 1
        while j >= 0 and key < custom_list[j]:
            custom_list[j + 1] = custom_list[j]
            j -= 1
        custom_list[j + 1] = key
    return custom_list


c_list = [2, 1, 7, 8, 9, 3, 2]

print(insertion_sort(c_list))


# when we have insuffcient memory
# easy to implement
# wehn we have continous inflow of numbers

# avoid when time is a concern
