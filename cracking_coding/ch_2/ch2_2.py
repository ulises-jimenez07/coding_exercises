from coding_interview.CrackingCoding.ch_2.linked_list import LinkedList


def kth_last_recursive(ll, k):
    head = ll.head
    counter = 0

    def helper(head, k):
        nonlocal counter
        if head is None:
            return None
        helper_node = helper(head.next, k)
        counter = counter + 1
        if counter == k:
            return head
        return helper_node

    return helper(head, k)


test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)

# for linked_list_values, k, expected in test_cases:
#    ll = LinkedList(linked_list_values)
#    print(kth_last_recursive(ll, k))

ll = LinkedList((10, 20, 30, 40, 50))
kth_last_recursive(ll, 2)
