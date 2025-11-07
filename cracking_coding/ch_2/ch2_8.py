from coding_interview.CrackingCoding.ch_2.linked_list import LinkedList


def loop_detection(ll):
    fast = ll.head
    slow = ll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    if fast is None or fast.next is None:
        return None
    slow = ll.head

    while fast is not slow:
        slow = slow.next
        fast = fast.next
    return fast


looped_list = LinkedList(["A", "B", "C", "D", "E"])
loop_start_node = looped_list.head.next.next
looped_list.tail.next = loop_start_node

print(loop_detection(looped_list))
print(loop_detection(LinkedList((1, 2, 3))))
