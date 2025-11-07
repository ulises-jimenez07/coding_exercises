class Queue:
    """Implements a queue using a Python list without a fixed size."""

    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_empty(self):
        """Checks if the queue is empty."""
        if not self.items:
            return True
        return False

    def enqueue(self, value):
        """Adds an element to the rear of the queue."""
        self.items.append(value)
        return "The element is inserted at the end of the queue"

    def dequeue(self):
        """Removes and returns the element from the front of the queue."""
        if self.is_empty():
            return "There is not any element in the Queue"
        return self.items.pop(0)

    def peek(self):
        """Returns the element at the front of the queue without removing it."""
        if self.is_empty():
            return "There is not any element in the Queue"
        return self.items[0]

    def delete(self):
        """Deletes the entire queue."""
        self.items = None


custom_queue = Queue()
print(custom_queue.is_empty())
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
print(custom_queue)
custom_queue.dequeue()
print(custom_queue)
print(custom_queue.peek())
