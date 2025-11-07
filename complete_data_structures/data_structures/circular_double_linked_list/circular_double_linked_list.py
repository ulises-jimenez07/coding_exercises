"""This module implements a Circular Double Linked List."""


class Node:
    """Represents a node in a circular double linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class CircularDoubleLinkedList:
    """Implements a circular double linked list."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current_node = self.head
        result = ""
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            result += " <-> "
        return result

    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     new_node.prev = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def append(self, value):
        """Appends a new node with the given value to the end of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Adds a new node with the given value to the beginning of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.head = new_node
        self.length += 1

    def traverse(self):
        """Traverses the list from head to tail, printing each node's value."""
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break

    def reverse_traverse(self):
        """Traverses the list from tail to head, printing each node's value."""
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break

    def search(self, target):
        """Searches for a target value in the list."""
        current_node = self.head
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
            if current_node == self.head:
                break
        return False

    def get(self, index):
        """Retrieves the node at the specified index."""
        if index < 0 or index >= self.length:
            return None
        current_node = None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node

    def set_value(self, index, value):
        """Sets the value of the node at the specified index."""
        target_node = self.get(index)
        if target_node:
            target_node.value = value
            return True
        return False

    def insert(self, index, value):
        """Inserts a new node with the given value at the specified index."""
        if index < 0 or index >= self.length:
            print("Error index out of bounds")
            return
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return
        new_node = Node(value)
        temp_node = self.get(index - 1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1

    def pop_first(self):
        """Removes and returns the first node from the list."""
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.prev = None
            popped_node.next = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return popped_node

    def pop(self):
        """Removes and returns the last node from the list."""
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.prev = None
            popped_node.next = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return popped_node

    def remove(self, index):
        """Removes and returns the node at the specified index."""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node


def delelete_all(self):
    """Deletes all nodes from the list, making it empty."""
    self.head = None
    self.tail = None
    self.length = 0


new_cdll = CircularDoubleLinkedList()
new_cdll.append(10)
new_cdll.append(20)
new_cdll.prepend(30)
new_cdll.prepend(50)
print(new_cdll)
new_cdll.insert(2, 50)
print(new_cdll)
new_cdll.pop_first()
print(new_cdll)
new_cdll.pop()
print(new_cdll)
new_cdll.remove(2)
print(new_cdll)
