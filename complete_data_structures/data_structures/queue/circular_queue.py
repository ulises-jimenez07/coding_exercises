class Queue:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def enqueue(self, value):
        if self.is_full():
            return "The Queue is full"

        if self.top + 1 == self.max_size:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value
        return "The element is inserted at the end of the Queue"

    def dequeue(self):
        if self.is_empty():
            return "There is not any element in the Queue"
        first_element = self.items[self.start]
        start = self.start
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start + 1 == self.max_size:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return first_element

    def peek(self):
        if self.is_empty():
            return "There is not any element in the Queue"
        return self.items[self.start]

    def delete(self):
        self.items = self.max_size * [None]
        self.top = -1
        self.start = -1


custom_queue = Queue(3)
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
print(custom_queue.is_full())
