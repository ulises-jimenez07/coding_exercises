class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    """Implements a singly linked list with various operations."""

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
        """Appends a new node with the given value to the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Adds a new node with the given value to the beginning of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        """Inserts a new node with the given value at the specified index."""
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def traverse(self):
        """Traverses the list from head to tail, printing each node's value."""
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        """Searches for a target value in the list and returns its index, or -1 if not found."""
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, index):
        """Retrieves the node at the specified index."""
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set(self, index, value):
        """Sets the value of the node at the specified index."""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

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
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        """Removes and returns the last node from the list."""
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        """Removes and returns the node at the specified index."""
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index in (self.length - 1, -1):
            return self.pop()

        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        """Deletes all nodes from the list, making it empty."""
        self.head = None
        self.tail = None
        self.length = 0

    def reverse(self):
        """Reverses the linked list in-place."""
        curr_node = self.head
        prev_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head, self.tail = self.tail, self.head

    def find_middle(self):
        """Returns the middle node of the linked list. If even, returns the second middle node."""
        mid_idx = self.length // 2

        if self.length == 0:
            return None

        mid_node = self.head

        if self.length == 1:
            return mid_node

        for _ in range(mid_idx - 1):
            mid_node = mid_node.next
        return mid_node.next


new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)

new_linked_list.prepend(40)
print(new_linked_list)
# new_linked_list.traverse()


print(new_linked_list.get(2))
print(new_linked_list.set(2, 50))

print(new_linked_list.pop_first())
print(new_linked_list.remove(1))
print(new_linked_list)
