"""
Describe how you could use a sigle Python list to implement
three stacks
"""


class MultiStack:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.cust_list = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks  # keep stack sizes
        self.stack_size = stack_size

    def is_full(self, stack_num):
        if self.sizes[stack_num] == self.stack_size:
            return True
        return False

    def is_empty(self, stack_num):
        if self.sizes[stack_num] == 0:
            return True
        return False

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def push(self, item, stack_num):
        if self.is_full(stack_num):
            return "The stack is full"
        self.sizes[stack_num] += 1
        self.cust_list[self.index_of_top(stack_num)] = item

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return "The stack is empty"
        value = self.cust_list[self.index_of_top(stack_num)]
        self.cust_list[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return "The stack is empty"
        value = self.cust_list[self.index_of_top(stack_num)]
        return value


custom_stack = MultiStack(6)
print(custom_stack.is_full(0))
print(custom_stack.is_empty(1))
custom_stack.push(1, 0)
custom_stack.push(2, 0)
custom_stack.push(3, 2)
print(custom_stack.peek(0))
