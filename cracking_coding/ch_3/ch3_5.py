from coding_interview.CrackingCoding.ch_3.stack import Stack


class SortedStack(Stack):
    def __init__(self):
        super().__init__()
        self.temp_stack = Stack()

    def sort(self):
        while not self.is_empty():
            tmp = self.pop()
            while (not self.temp_stack.is_empty()) and (self.temp_stack.peek() > tmp):
                self.push(self.temp_stack.pop())

            self.temp_stack.push(tmp)

        while not self.temp_stack.is_empty():
            self.push(self.temp_stack.pop())


queue = SortedStack()
queue.push(3)
queue.push(2)
queue.push(1)
queue.push(4)

queue.sort()
print(queue)
