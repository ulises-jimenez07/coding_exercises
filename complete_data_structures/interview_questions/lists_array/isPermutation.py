def permutation(list1, list2):
    """Checks if two lists are permutations of each other."""
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    return list1 == list2
