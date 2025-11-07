"""This module implements a Double Linked List."""


class Node:
    """Represents a node in a double linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class DoubleLinkedList:
    """Implements a double linked list with various operations."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " <-> "
            temp_node = temp_node.next
        return result

    def append(self, value):
        """Appends a new node with the given value to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Adds a new node with the given value to the beginning of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def traverse(self):
        """Traverses the list from head to tail, printing each node's value."""
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def reverse_traverse(self):
        """Traverses the list from tail to head, printing each node's value."""
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search(self, target):
        """Searches for a target value in the list and returns its index, or -1 if not found."""
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def get(self, index):
        """Retrieves the node at the specified index."""
        if index < 0 or index >= self.length:
            return None
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
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        """Inserts a new node with the given value at the specified index."""
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        temp_node = self.get(index - 1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
        return True

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
            self.head.prev = None
            popped_node.next = None
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
            self.tail.next = None
            popped_node.prev = None
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


new_dll = DoubleLinkedList()
new_dll.append(10)
new_dll.append(20)
new_dll.append(30)
new_dll.prepend(5)
print(new_dll)
new_dll.pop_first()
print(new_dll)
