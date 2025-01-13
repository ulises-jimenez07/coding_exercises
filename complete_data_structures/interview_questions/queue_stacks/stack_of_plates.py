class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)

    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) > 0 and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1].pop()

    def pop_at(self, stack_num):
        if len(self.stacks[stack_num]) > 0:
            return self.stacks[stack_num].pop()
        return None


custom_stack = PlateStack(2)
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(4)
print(custom_stack)
print(custom_stack.pop_at(0))
print(custom_stack)
