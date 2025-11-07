"""
Remove Duplicates
Write a function to remove duplicates from an unsorted linked list.
Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 Output 1 -> 2 -> 3 -> 4 -> 5
"""

from linkedlist import LinkedList


def remove_duplicates(ll):
    unique = set()
    if ll.head is None:
        return
    curr = ll.head
    unique.add(curr.value)

    while curr and curr.next:
        if curr.next.value in unique:
            curr.next = curr.next.next
        else:
            unique.add(curr.next.value)
            curr = curr.next

    ll.tail = curr


customLL = LinkedList()
customLL.generate(10, 0, 100)
print(customLL)
remove_duplicates(customLL)
print(customLL)
