"""This module implements a Circular Singly Linked List."""


class Node:
    """Represents a node in a circular singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CSLinkedList:
    """Implements a circular singly linked list."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += "->"
        return result

    def append(self, value):
        """Appends a new node with the given value to the end of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
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
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):
        """Inserts a new node with the given value at the specified index."""
        new_node = Node(value)
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        """Traverses the list from head to tail, printing each node's value."""
        current = self.head
        while current:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def search(self, target):
        """Searches for a target value in the list."""
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get(self, index):
        """Retrieves the node at the specified index."""
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        """Sets the value of the node at the specified index."""
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def pop_first(self):
        """Removes and returns the first node from the list."""
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
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
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
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
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        """Deletes all nodes from the list, making it empty."""
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

    def delete_by_value(self, value):
        """Deletes the first occurrence of a node with the given value."""
        if self.length == 0:
            return False

        if self.head == self.tail and self.head.value == value:
            self.head = None
            self.tail = None
            self.length = 0
            return True

        prev = None
        curr = self.head

        while True:
            if curr.value == value:
                if curr == self.head:
                    self.head = curr.next
                    self.tail.next = self.head
                else:
                    prev.next = curr.next
                    if curr == self.tail:
                        self.tail = prev

                self.length -= 1
                return True

            prev = curr
            curr = curr.next
            if curr == self.head:
                break

        return False

    def split_list(self):
        """Splits the circular linked list into two new circular linked lists."""
        if self.length == 0:
            return None, None
        first_list = CSLinkedList()
        second_list = CSLinkedList()
        if self.length == 1:
            first_list.append(self.head.value)
            second_list.append(self.head.value)
        else:
            mid = self.length // 2 + self.length % 2
            curr = self.head
            for _ in range(mid):
                first_list.append(curr.value)
                curr = curr.next
            for _ in range(mid, self.length):
                second_list.append(curr.value)
                curr = curr.next

        return first_list, second_list

    def is_sorted(self):
        """Checks if the list is sorted in ascending order."""
        if self.head is None:
            return True
        curr = self.head
        while curr.next != self.head:
            if curr.value > curr.next.value:
                return False
            curr = curr.next
        return True

    def insert_into_sorted(self, data):
        """Inserts data into a sorted circular linked list while maintaining sort order."""
        if self.head is None:
            self.append(data)
        elif data <= self.head.value:
            self.prepend(data)
        else:
            curr = self.head
            while curr.next != self.head and curr.next.value < data:
                curr = curr.next

            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node


cslinkded = CSLinkedList()
cslinkded.append(10)
cslinkded.append(20)
cslinkded.append(30)
cslinkded.append(40)
print(cslinkded)
cslinkded.insert(0, 50)
print(cslinkded)
cslinkded.set_value(-1, 100)
print(cslinkded)
cslinkded.pop_first()
print(cslinkded)
