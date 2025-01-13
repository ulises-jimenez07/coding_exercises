'''
Middle of a Singly Linked List
Write a function to find and return the middle node of a singly linked list. 
If the list has an even number of nodes, return the second of the two middle nodes.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def find_middle(self):
        mid_idx = self.length//2        
        if self.length == 0:
            return None
        
        mid_node = self.head        
        if self.length == 1:
            return mid_node
            
        for _ in range(mid_idx -1):
            mid_node = mid_node.next
        return mid_node.next