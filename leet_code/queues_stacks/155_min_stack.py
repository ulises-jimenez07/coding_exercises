import unittest

class MinStackTwoLists:
    """
    Implements a stack with constant time access to the minimum element using two lists.
    One list ('a') stores all the elements of the stack.
    Another list ('b') stores the minimum elements encountered so far.
    """
    def __init__(self):
        """
        Initializes two empty lists.
        self.a: The main stack to store all elements.
        self.b: A secondary stack to keep track of the current minimum.
        """
        self.a = []
        self.b = []

    def push(self, val: int) -> None:
        """
        Pushes a value onto the stack.
        The value is always added to the main stack 'a'.
        It's added to the min-tracking stack 'b' only if 'b' is empty
        or the value is less than or equal to the current minimum in 'b'.

        Args:
            val: The integer value to push.
        """
        self.a.append(val)
        if len(self.b) == 0 or val <= self.b[-1]:
            self.b.append(val)

    def pop(self) -> None:
        """
        Removes the top element from the stack.
        If the element being popped from 'a' is also the current minimum
        (i.e., it's at the top of 'b'), it's also popped from 'b'.
        Does nothing if the stack 'a' is empty.
        """
        if len(self.a) > 0:
            if self.a[-1] == self.b[-1]: # Check if the top of 'a' is the current min
                self.b.pop()
            self.a.pop()

    def top(self) -> int:
        """
        Returns the value of the top element without removing it.

        Returns:
            The value of the top element of stack 'a', or raises IndexError if 'a' is empty.
        """
        if not self.a:
            # Consistent with MinStackTuple behavior for empty stack during tests
            # Or could raise an error: raise IndexError("top from empty stack")
            return None
        return self.a[-1]

    def getMin(self) -> int:
        """
        Returns the minimum value in the stack.

        Returns:
            The minimum value (top of stack 'b'), or raises IndexError if 'b' is empty.
        """
        if not self.b:
            # Consistent with MinStackTuple behavior for empty stack during tests
            # Or could raise an error: raise IndexError("getMin from empty stack")
            return None
        return self.b[-1]


class MinStackTuple:
    """
    Implements a stack with constant time access to the minimum element.

    Each element in the stack is stored as a tuple (value, current_min),
    where current_min is the minimum value up to that point in the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        self.stack: A list to store tuples of [value, current_minimum_at_this_point].
        """
        self.stack = []

    def push(self, val: int) -> None:
        """
        Pushes a value onto the stack.
        The current minimum is determined by comparing the new value
        with the minimum of the previous element (if any).

        Args:
            val: The integer value to push.
        """
        curr_min = self.getMin()
        if curr_min is None or val < curr_min: # Note: original had curr_min > val, which is the same logic
            curr_min = val
        self.stack.append([val, curr_min])

    def pop(self) -> None:
        """
        Removes the top element from the stack.
        Does nothing if the stack is empty.
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
            The minimum value (stored with the top element), or None if the stack is empty.
        """
        return self.stack[-1][1] if self.stack else None


class TestMinStacks(unittest.TestCase):
    def run_tests_for_stack_type(self, stack_class):
        """Helper method to run tests for a given stack implementation."""
        # Test Case 1: Empty stack
        stack = stack_class()
        self.assertIsNone(stack.top(), f"{stack_class.__name__}: Top of empty stack should be None")
        self.assertIsNone(stack.getMin(), f"{stack_class.__name__}: Min of empty stack should be None")
        stack.pop()  # Test popping from an empty stack
        self.assertIsNone(stack.top(), f"{stack_class.__name__}: Top after pop on empty stack should be None")
        self.assertIsNone(stack.getMin(), f"{stack_class.__name__}: Min after pop on empty stack should be None")

        # Test Case 2: Push, pop, top, getMin basic operations
        stack = stack_class()
        stack.push(3)
        self.assertEqual(stack.top(), 3, f"{stack_class.__name__}: Top should be 3")
        self.assertEqual(stack.getMin(), 3, f"{stack_class.__name__}: Min should be 3")

        stack.push(5)
        self.assertEqual(stack.top(), 5, f"{stack_class.__name__}: Top should be 5")
        self.assertEqual(stack.getMin(), 3, f"{stack_class.__name__}: Min should still be 3")

        stack.push(2)
        self.assertEqual(stack.top(), 2, f"{stack_class.__name__}: Top should be 2")
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should now be 2")

        stack.push(7)
        self.assertEqual(stack.top(), 7, f"{stack_class.__name__}: Top should be 7")
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should still be 2")

        # Test Case 3: Pop behavior
        stack.pop()  # Pop 7
        self.assertEqual(stack.top(), 2, f"{stack_class.__name__}: Top should be 2 after popping 7")
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should be 2 after popping 7")

        stack.pop()  # Pop 2
        self.assertEqual(stack.top(), 5, f"{stack_class.__name__}: Top should be 5 after popping 2")
        self.assertEqual(stack.getMin(), 3, f"{stack_class.__name__}: Min should be 3 after popping 2")

        stack.pop()  # Pop 5
        self.assertEqual(stack.top(), 3, f"{stack_class.__name__}: Top should be 3 after popping 5")
        self.assertEqual(stack.getMin(), 3, f"{stack_class.__name__}: Min should be 3 after popping 5")

        stack.pop()  # Pop 3
        self.assertIsNone(stack.top(), f"{stack_class.__name__}: Top should be None after popping last element")
        self.assertIsNone(stack.getMin(), f"{stack_class.__name__}: Min should be None after popping last element")

        # Test Case 4: Multiple minimums and negative numbers
        stack = stack_class()
        stack.push(-2)
        self.assertEqual(stack.getMin(), -2, f"{stack_class.__name__}: Min should be -2")
        stack.push(0)
        self.assertEqual(stack.getMin(), -2, f"{stack_class.__name__}: Min should still be -2")
        stack.push(-3)
        self.assertEqual(stack.getMin(), -3, f"{stack_class.__name__}: Min should be -3")

        stack.pop()  # Pop -3
        self.assertEqual(stack.top(), 0, f"{stack_class.__name__}: Top should be 0")
        self.assertEqual(stack.getMin(), -2, f"{stack_class.__name__}: Min should revert to -2")

        stack.push(-4)
        self.assertEqual(stack.top(), -4, f"{stack_class.__name__}: Top should be -4")
        self.assertEqual(stack.getMin(), -4, f"{stack_class.__name__}: Min should be -4")

        # Test Case 5: Positive numbers, ensuring min updates correctly after pops
        stack = stack_class()
        stack.push(5)
        stack.push(10)
        stack.push(2) # Min is 2
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should be 2")
        stack.pop() # Pop 2
        self.assertEqual(stack.getMin(), 5, f"{stack_class.__name__}: Min should be 5 after popping 2")
        stack.pop() # Pop 10
        self.assertEqual(stack.getMin(), 5, f"{stack_class.__name__}: Min should still be 5 after popping 10")
        stack.push(1) # Min is 1
        self.assertEqual(stack.getMin(), 1, f"{stack_class.__name__}: Min should be 1")
        stack.pop() # Pop 1
        self.assertEqual(stack.getMin(), 5, f"{stack_class.__name__}: Min should revert to 5")

        # Test Case 6: Popping all elements
        stack = stack_class()
        stack.push(10)
        stack.push(20)
        stack.pop()
        stack.pop()
        self.assertIsNone(stack.top(), f"{stack_class.__name__}: Top should be None after all elements popped")
        self.assertIsNone(stack.getMin(), f"{stack_class.__name__}: Min should be None after all elements popped")
        stack.pop() # Pop from empty again
        self.assertIsNone(stack.top(), f"{stack_class.__name__}: Top should remain None")
        self.assertIsNone(stack.getMin(), f"{stack_class.__name__}: Min should remain None")

        # Test Case 7: Duplicate minimum values
        stack = stack_class()
        stack.push(5)
        stack.push(2)
        stack.push(2) # Duplicate min
        stack.push(3)
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should be 2 with duplicates")
        stack.pop() # Pop 3
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should still be 2")
        stack.pop() # Pop 2 (one of the mins)
        # For MinStackTwoLists, if 2 was the only thing in b matching the top of a, it's removed.
        # The next min in b (if any) would be the one before it.
        # For MinStackTuple, the (value, min_so_far) is popped.
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should still be 2 after popping one duplicate min")
        stack.pop() # Pop the other 2
        self.assertEqual(stack.getMin(), 5, f"{stack_class.__name__}: Min should be 5 after all 2s are popped")


    def test_min_stack_two_lists(self):
        self.run_tests_for_stack_type(MinStackTwoLists)

    def test_min_stack_tuple(self):
        self.run_tests_for_stack_type(MinStackTuple)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # Using exit=False and argv to make it runnable in environments like Jupyter notebooks or IDEs
    # If running from command line, `unittest.main()` is sufficient.