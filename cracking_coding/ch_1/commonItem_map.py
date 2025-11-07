array1 = ["a", "b", "c", "x"]
array2 = ["x", "y", "z"]


def containsCommonItemBruteForce(array1, array2):
    for elem1 in array1:
        for elem2 in array2:
            if elem1 == elem2:
                return True

    return False


def containsCommonItem(array1, array2):
    map = {}
    for elem1 in array1:
        if not elem1 in map:
            map[elem1] = True
    for elem2 in array2:
        if elem2 in map:
            return True
    return False


print(containsCommonItem(array1, array2))
