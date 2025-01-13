import unittest


class MinStack:
    """
    Implements a stack with constant time access to the minimum element.

    Each element in the stack is stored as a tuple (value, current_min),
    where current_min is the minimum value up to that point in the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.stack = []

    def push(self, val: int) -> None:
        """
        Pushes a value onto the stack.

        Args:
            val: The value to push.
        """
        curr_min = self.getMin()
        if curr_min is None or curr_min > val:
            curr_min = val
        self.stack.append([val, curr_min])

    def pop(self) -> None:
        """
        Removes and returns the top element from the stack.
        """
        if self.stack:  # Check for empty stack before popping
            self.stack.pop()

    def top(self) -> int:
        """
        Returns the value of the top element without removing it.

        Returns:
            The value of the top element, or None if the stack is empty.
        """
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        """
        Returns the minimum value in the stack.

        Returns:
            The minimum value, or None if the stack is empty.
        """
        return self.stack[-1][1] if self.stack else None


class TestMinStack(unittest.TestCase):
    def test_empty_stack(self):
        stack = MinStack()
        self.assertIsNone(stack.top())
        self.assertIsNone(stack.getMin())
        stack.pop()  # Test popping from an empty stack
        self.assertIsNone(stack.top())
        self.assertIsNone(stack.getMin())

    def test_push_pop(self):
        stack = MinStack()
        stack.push(3)
        self.assertEqual(stack.top(), 3)
        self.assertEqual(stack.getMin(), 3)
        stack.push(5)
        self.assertEqual(stack.top(), 5)
        self.assertEqual(stack.getMin(), 3)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.getMin(), 2)
        stack.push(7)
        self.assertEqual(stack.top(), 7)
        self.assertEqual(stack.getMin(), 2)

    def test_multiple_min(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(stack.getMin(), -3)
        stack.pop()
        self.assertEqual(stack.getMin(), -2)
        stack.push(-4)
        self.assertEqual(stack.top(), -4)
        self.assertEqual(stack.getMin(), -4)

    def test_positive_numbers(self):
        stack = MinStack()
        stack.push(5)
        stack.push(10)
        stack.push(2)
        self.assertEqual(stack.getMin(), 2)
        stack.pop()
        self.assertEqual(stack.getMin(), 5)


if __name__ == "__main__":
    unittest.main()
