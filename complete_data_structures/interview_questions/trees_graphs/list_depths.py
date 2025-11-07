#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.


# List of Depth
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next is None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    left_d = 1 + depth(tree.left)
    right_d = 1 + depth(tree.right)

    if left_d > right_d:
        return left_d
    return right_d


def treeToLinkedList(tree, custDict=None, d=None):
    if custDict is None:
        custDict = {}
    if d is None:
        d = depth(tree)
    if custDict.get(d):
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
    else:
        custDict[d] = LinkedList(tree.val)

    if tree.left is not None:
        custDict = treeToLinkedList(tree.left, custDict, d - 1)
    if tree.right is not None:
        custDict = treeToLinkedList(tree.right, custDict, d - 1)
    return custDict
