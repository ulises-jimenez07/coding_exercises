"""
Pairs
Write a function to find all pairs of an integer array whose sum is equal to a given number.
Do not consider commutative pairs.

Example

pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']


Note:

4+3 comes from second and third elements from the main list.

3+4 comes from third and seventh elements from the main list.
"""


def pair_sum(myList, target_sum):
    result = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if (myList[i] + myList[j]) == target_sum:
                result.append(str(myList[i]) + "+" + str(myList[j]))

    return result
