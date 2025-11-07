"""
Remove Duplicates from a Singly Linked List
Given a singly linked list, write a function that removes all the duplicates. use this linked list .

Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"

Result Linked List - "1 -> 2 -> 4 -> 3
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove_duplicates(self):
        unique_vals = set()
        if self.head is None:
            return
        curr = self.head
        unique_vals.add(curr.value)
        while curr and curr.next:
            if curr.next.value in unique_vals:
                curr.next = curr.next.next
                self.length -= 1
            else:
                unique_vals.add(curr.next.value)
                curr = curr.next

        self.tail = curr
