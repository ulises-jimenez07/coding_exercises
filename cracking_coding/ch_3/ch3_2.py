from coding_interview.CrackingCoding.ch_3.stack import Stack


class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minvals =Stack()

    def minimum(self):
        return self.minvals.peek()

    def push(self,value):
        super().push(value)
        if not self.minvals or value <= self.minimum():
            self.minvals.push(value)
    
    def pop(self):
        value = super().pop()
        if value == self.minimum():
            self.minvals.pop()
        return value
    

newstack = MinStack()
newstack.push(5)
newstack.minimum()
newstack.push(6)
newstack.push(3)
newstack.push(7)
newstack.push(3)
newstack.minimum()
newstack.pop()
newstack.minimum()
newstack.pop()
newstack.minimum()
newstack.pop()
newstack.minimum()
newstack.push(1)
newstack.minimum()

