"""
Given two singly linked lists, determine if the two lists intersect. 
Retrun the intersectiong node. 
"""

from linkedlist import LinkedList
from linkedlist import Node


def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longer_node = longer.head
    shorter_node = shorter.head

    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


# helper addition method
def add_same_node(llA, llB, value):
    temp = Node(value)
    llA.tail.next = temp
    llA.tail = temp
    llB.tail.next = temp
    llB.tail = temp


lla = LinkedList()
lla.generate(3, 0, 10)

llb = LinkedList()
llb.generate(4, 0, 10)

add_same_node(lla, llb, 11)
add_same_node(lla, llb, 5)
add_same_node(lla, llb, 6)

print(lla)
print(llb)
print(intersection(lla, llb))
