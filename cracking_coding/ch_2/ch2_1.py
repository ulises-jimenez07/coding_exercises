from coding_interview.CrackingCoding.ch_2.linked_list import LinkedList
#keep track of elements in a set
def remove_dups(ll):
    previous=None
    current= ll.head
    seen = set()

    while current:
        if current.value in seen:
            #skip that current
            previous.next=current.next
        else:
            seen.add(current.value)
            #move previous to the current positon
            previous=current
        #always move current
        current=current.next
    return ll

ll = LinkedList.generate(100, 0, 9)
print("==== Original ====")
print(ll)
remove_dups(ll)
print("==== New ====")
print(ll)