class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)

    def is_empty(self):
        if not self.list:
            return True
        return False

    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        return False

    def push(self, value):
        if self.is_full():
            return "The stack is full"
        self.list.append(value)
        return "The element has been successfully inserted"

    def peek(self):
        if self.is_empty():
            return "There is no element in the stack"
        return self.list[-1]

    def delete(self):
        self.list = None


custom_stack = Stack(4)
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
print(custom_stack)
custom_stack.push(4)
# print(custom_stack)
custom_stack.push(5)
