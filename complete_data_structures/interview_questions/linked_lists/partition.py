"""
write code to partition a linked list around a value x, 
suchat that all nodes less than x cmo before all nodes greater than or equal to x
"""

from linkedlist import LinkedList


def partition(ll, x):
    curr_node = ll.head
    ll.tail = ll.head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = None

        if curr_node.value < x:
            curr_node.next = ll.head
            ll.head = curr_node
        else:
            ll.tail.next = curr_node
            ll.tail = curr_node
        curr_node = next_node

    if ll.tail.next is not None:
        ll.tail.next = None


customLL = LinkedList()
customLL.generate(10, 0, 100)
print(customLL)
partition(customLL, 30)
print(customLL)
