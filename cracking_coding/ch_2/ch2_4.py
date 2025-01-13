from coding_interview.CrackingCoding.ch_2.linked_list import LinkedList

def partition(ll, x):
    current=ll.tail=ll.head
    while current:
        next= current.next
        current.next=None
        if current.value < x :
            current.next=ll.head
            ll.head=current
        else:
            ll.tail.next=current
            ll.tail=current
        current=next
    ll.tail.next=None



ll = LinkedList()
ll.add_multiple([3,5,8,5,10,2,1])

print(ll)
partition(ll, 5)
print(ll)