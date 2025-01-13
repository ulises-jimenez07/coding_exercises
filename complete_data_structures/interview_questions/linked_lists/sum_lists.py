"""
You have two numbers respresented by a linked list, where each node
contains a sigle digit. The digits are soreted in reverse order, such that
1's digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list.
"""

from linkedlist import LinkedList


def sum_list(ll1, ll2):
    n1 = ll1.head
    n2 = ll2.head

    carry = 0
    result_ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        result_ll.add(int(result % 10))
        carry = result // 10
    if carry:
        result_ll.add(carry)
    return result_ll


lla = LinkedList()
lla.add(7)
lla.add(1)
lla.add(6)

llb = LinkedList()
llb.add(5)
llb.add(9)
llb.add(2)

print(lla)
print(llb)
print(sum_list(lla, llb))
