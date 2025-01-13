"""
Same Frequency
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
Output:

False
"""


def check_same_frequency(list1, list2):
    # TODO
    freq = {}
    for item in list1:
        freq[item] = freq.get(item, 0) + 1

    for item in list2:
        freq[item] = freq.get(item, 0) - 1
        if freq[item] < 0:
            return False

    return True
