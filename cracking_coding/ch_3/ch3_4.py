from coding_interview.CrackingCoding.ch_3.stack import Stack

class Queue_Stack:
    def __init__(self) :
        self.new_stack =Stack()
        self.old_stack= Stack()

    def __len__(self):
        return len(self.new_stack)+ len(self.old_stack)
    
    def add(self, value):
        self.new_stack.push(value)

    def is_empty(self):
        return len(self)==0
    
    def shift_stacks(self):
        if self.old_stack.is_empty():
            while not self.new_stack.is_empty():
                self.old_stack.push(self.new_stack.pop())
    
    def peek(self):
        if self.is_empty():
            return False
        self.shift_stacks()
        return self.old_stack.peek()
    
    def remove(self):
        if self.is_empty():
            return False
        self.shift_stacks()
        return self.old_stack.pop()
    
q = Queue_Stack()
for index, val in enumerate(["a", "b", "c", "d", "e", "f"], start=1):
    q.add(val)
    
q.remove()
