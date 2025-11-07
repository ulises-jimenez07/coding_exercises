class Node:
    """Represents a node in a linked list."""

    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    """Implements a singly linked list."""

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next


class Queue:
    """Implements a queue using a linked list."""

    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return " ".join(values)

    def enqueue(self, value):
        """Adds an element to the rear of the queue."""
        new_node = Node(value)
        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def is_empty(self):
        """Checks if the queue is empty."""
        if self.linked_list.head is None:
            return True
        return False

    def dequeue(self):
        """Removes and returns the element from the front of the queue."""
        if self.is_empty():
            return "There is not any element in the Queue"
        temp_node = self.linked_list.head
        if self.linked_list.head == self.linked_list.tail:
            self.linked_list.head = None
            self.linked_list.tail = None
        else:
            self.linked_list.head = self.linked_list.head.next
        return temp_node

    def peek(self):
        """Returns the element at the front of the queue without removing it."""
        if self.is_empty():
            return "There is not any element in the Queue"
        return self.linked_list.head

    def delete(self):
        """Deletes the entire queue."""
        self.linked_list.head = None
        self.linked_list.tail = None


cust_queue = Queue()
cust_queue.enqueue(1)
cust_queue.enqueue(2)
cust_queue.enqueue(3)
print(cust_queue)
cust_queue.peek()
print(cust_queue)
