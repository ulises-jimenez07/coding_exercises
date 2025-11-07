from coding_interview.CrackingCoding.ch_2.linked_list import LinkedList


def intersection(list1, list2):
    if list1.tail != list2.tail:
        return None
    len1 = len(list1)
    len2 = len(list2)
    if len1 < len2:
        shorter = list1.head
        longer = list2.head
    else:
        shorter = list2.head
        longer = list1.head

    diff = abs(len1 - len2)
    for i in range(diff):
        longer = longer.next

    while shorter is not longer:
        shorter = shorter.next
        longer = longer.next
    return shorter


shared = LinkedList()
shared.add_multiple([1, 2, 3, 4])

a = LinkedList([10, 11, 12, 13, 14, 15])
b = LinkedList([20, 21, 22])

a.tail.next = shared.head
a.tail = shared.tail

b.tail.next = shared.head
b.tail = shared.tail

print(intersection(a, b))
