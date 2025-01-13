# Sinking sort or bubble sort
# repeatly compare each pair of adjacent itmes and swamp them
# O(n^2)

# Space efficient
# easy to implement


def bubble_sort(custom_list):
    for i in range(len(custom_list) - 1):
        for j in range(len(custom_list) - i - 1):
            if custom_list[j] > custom_list[j + 1]:
                custom_list[j], custom_list[j + 1] = custom_list[j + 1], custom_list[j]
    return custom_list


c_list = [2, 1, 7, 8, 9, 3, 2]

print(bubble_sort(c_list))
