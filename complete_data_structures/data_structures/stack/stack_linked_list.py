class Node:
    """Represents a node in a linked list."""

    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    """Implements a singly linked list."""

    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    """Implements a stack using a linked list."""

    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        """Checks if the stack is empty."""
        if not self.linked_list.head:
            return True
        return False

    def __str__(self):
        values = [str(x.value) for x in self.linked_list]
        return "\n".join(values)

    def push(self, value):
        """Pushes an element onto the top of the stack."""
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self):
        """Removes and returns the top element from the stack."""
        if self.is_empty():
            return "There is no element in the stack"
        node = self.linked_list.head
        self.linked_list.head = self.linked_list.head.next
        return node.value

    def peek(self):
        """Returns the top element of the stack without removing it."""
        if self.is_empty():
            return "There is no element in the stack"
        node = self.linked_list.head
        return node.value

    def delete(self):
        """Deletes the entire stack."""
        self.linked_list.head = None


custom_stack = Stack()
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
print(custom_stack)
custom_stack.pop()
print(custom_stack)
