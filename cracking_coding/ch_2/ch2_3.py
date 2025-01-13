from coding_interview.CrackingCoding.ch_2.linked_list import LinkedList


def delete_middle_node(node):
    if (node is None) or (node.next is None):
        return False
    else:
        node.value=node.next.value
        node.next= node.next.next
        return True
    

ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
delete_middle_node(middle_node)
print(ll)