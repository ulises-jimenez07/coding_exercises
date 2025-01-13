#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# Minimal Binary Search Tree


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minimalTree(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])

    mid = len(sortedArray) // 2
    left = minimalTree(sortedArray[:mid])
    right = minimalTree(sortedArray[mid + 1 :])

    return BSTNode(sortedArray[mid], left, right)
