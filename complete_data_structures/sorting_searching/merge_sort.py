# divide and conquer algorithm
# divide in halves


def merge(custom_list, left, middle, right):
    num_elem_1 = middle - left + 1
    num_elem_2 = right - middle

    left_list = [0] * num_elem_1
    right_list = [0] * num_elem_2

    for i in range(num_elem_1):
        left_list[i] = custom_list[left + i]
    for j in range(num_elem_2):
        right_list[j] = custom_list[middle + 1 + j]

    i = 0
    j = 0
    k = left

    while i < num_elem_1 and j < num_elem_2:
        if left_list[i] <= right_list[j]:
            custom_list[k] = left_list[i]
            i += 1
        else:
            custom_list[k] = right_list[j]
            j += 1
        k += 1
    while i < num_elem_1:
        custom_list[k] = left_list[i]
        i += 1
        k += 1
    while j < num_elem_2:
        custom_list[k] = right_list[j]
        j += 1
        k += 1


def merge_sort(custom_list, left, right):
    if left < right:
        middle = (left + (right - 1)) // 2
        merge_sort(custom_list, left, middle)
        merge_sort(custom_list, middle + 1, right)
        merge(custom_list, left, middle, right)
    return custom_list


c_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]

print(merge_sort(c_list, 0, len(c_list) - 1))


# stable sort
# when avergae expected time is O(NlogN)
