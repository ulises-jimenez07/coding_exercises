# repeately find the mininum element and move it
# to the sorted part of the array to make unserted part sorted


# in place sorted
# poor effiency O(n^2)
# few elements in random order


def selection_sort(custom_list):
    for i, _ in enumerate(custom_list):
        min_index = i
        for j in range(i + 1, len(custom_list)):
            if custom_list[min_index] > custom_list[j]:
                min_index = j
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
    return custom_list


c_list = [2, 1, 7, 8, 9, 3, 2]

print(selection_sort(c_list))


# it is space efficient
# easy to implement

# avoid when time is a concer
