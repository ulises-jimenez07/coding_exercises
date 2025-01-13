from linkedlist import LinkedList


def nth_to_last(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for _ in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1


customLL = LinkedList()
customLL.generate(10, 0, 100)
print(customLL)
print(nth_to_last(customLL, 3))
