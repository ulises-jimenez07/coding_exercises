from coding_interview.CrackingCoding.ch_2.linked_list import LinkedList


def sum_lists(ll1, ll2):
    res_list = LinkedList()
    n1 = ll1.head
    n2 = ll2.head
    carry = 0

    while n1 or n2:
        part_res = carry
        if n1:
            part_res += int(n1.value)
            n1 = n1.next
        if n2:
            part_res += int(n2.value)
            n2 = n2.next
        res_list.add(part_res % 10)
        carry = part_res // 10

    if carry:
        res_list.add(carry)
    return res_list


def sum_lists_rec(ll1, ll2):
    n1 = ll1.head
    n2 = ll2.head
    res_list = LinkedList()
    add_helper(n1, n2, 0, res_list)


def add_helper(n1, n2, carry, res_list):
    if (n1 is None) and (n2 is None) and (carry == 0):
        return None

    part_res = carry
    if n1:
        part_res += int(n1.value)
        n1 = n1.next
    if n2:
        part_res += int(n2.value)
        n2 = n2.next
    res_list.add(part_res % 10)
    carry = part_res // 10
    if (n1 is not None) or (n2 is not None):
        add_helper(None if n1 is None else n1.next, None if n2 is None else n2.next, carry, res_list)


ll1 = LinkedList()
ll1.add_multiple([1, 2, 3, 4])
ll2 = LinkedList()
ll2.add_multiple([5, 6, 7])

print(ll1)
print(ll2)

print(sum_lists(ll1, ll2))
print(sum_lists_rec(ll1, ll2))
