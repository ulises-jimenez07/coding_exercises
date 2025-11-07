from coding_interview.CrackingCoding.ch_2.linked_list import LinkedList


def is_palindrome(ll):
    fast = slow = ll.head
    stack = []
    while fast and fast.next:
        stack.append(slow.value)
        fast = fast.next.next
        slow = slow.next

    if fast:
        slow = slow.next

    while slow:
        if slow.value != stack.pop():
            return False
        slow = slow.next

    return True


test_cases = [
    ([1, 2, 3, 4, 3, 2, 1], True),
    ([1], True),
    (["a", "a"], True),
    ("aba", True),
    ([], True),
    ([1, 2, 3, 4, 5], False),
    ([1, 2], False),
]

for test in test_cases:
    list = LinkedList(test[0])
    print(is_palindrome(list))
