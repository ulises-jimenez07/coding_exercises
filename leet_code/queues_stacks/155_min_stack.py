"""
Problem: Min Stack - design stack with O(1) access to minimum element

Approach:
- Two implementations: dual lists or tuple per element
- Track minimum at each stack state
- Time complexity: O(1) for all operations
- Space complexity: O(n) where n is number of elements
"""

import unittest


class MinStackTwoLists:
    """
    Implements a stack with constant time access to the minimum element using two lists.
    One list ('a') stores all elements, and 'b' stores minimums encountered so far.
    """

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, val: int) -> None:
        """Pushes a value onto the stack."""
        self.a.append(val)
        if not self.b or val <= self.b[-1]:
            self.b.append(val)

    def pop(self) -> None:
        """Removes the top element from the stack."""
        if self.a:
            if self.a[-1] == self.b[-1]:
                self.b.pop()
            self.a.pop()

    def top(self) -> int:
        """Returns the value of the top element without removing it."""
        return self.a[-1] if self.a else None

    def getMin(self) -> int:
        """Returns the minimum value in the stack."""
        return self.b[-1] if self.b else None


class MinStackTuple:
    """
    Implements a stack with constant time access to the minimum element.
    Each element is stored as a tuple (value, current_min).
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        """Pushes a value onto the stack."""
        curr_min = self.getMin()
        if curr_min is None or val < curr_min:
            curr_min = val
        self.stack.append([val, curr_min])

    def pop(self) -> None:
        """Removes the top element from the stack."""
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        """Returns the value of the top element without removing it."""
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        """Returns the minimum value in the stack."""
        return self.stack[-1][1] if self.stack else None


class TestMinStacks(unittest.TestCase):
    def run_tests_for_stack_type(self, stack_class):
        """Helper method to run tests for a given stack implementation."""
        # Test Case 1: Empty stack
        stack = stack_class()
        self.assertIsNone(stack.top(), f"{stack_class.__name__}: Top of empty stack should be None")
        self.assertIsNone(stack.getMin(), f"{stack_class.__name__}: Min of empty stack should be None")
        stack.pop()
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
        stack.pop()
        self.assertEqual(stack.top(), 2, f"{stack_class.__name__}: Top should be 2 after popping 7")
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should be 2 after popping 7")

        stack.pop()
        self.assertEqual(stack.top(), 5, f"{stack_class.__name__}: Top should be 5 after popping 2")
        self.assertEqual(stack.getMin(), 3, f"{stack_class.__name__}: Min should be 3 after popping 2")

        stack.pop()
        self.assertEqual(stack.top(), 3, f"{stack_class.__name__}: Top should be 3 after popping 5")
        self.assertEqual(stack.getMin(), 3, f"{stack_class.__name__}: Min should be 3 after popping 5")

        stack.pop()
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

        stack.pop()
        self.assertEqual(stack.top(), 0, f"{stack_class.__name__}: Top should be 0")
        self.assertEqual(stack.getMin(), -2, f"{stack_class.__name__}: Min should revert to -2")

        stack.push(-4)
        self.assertEqual(stack.top(), -4, f"{stack_class.__name__}: Top should be -4")
        self.assertEqual(stack.getMin(), -4, f"{stack_class.__name__}: Min should be -4")

        # Test Case 5: Positive numbers, ensuring min updates correctly after pops
        stack = stack_class()
        stack.push(5)
        stack.push(10)
        stack.push(2)
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should be 2")
        stack.pop()
        self.assertEqual(stack.getMin(), 5, f"{stack_class.__name__}: Min should be 5 after popping 2")
        stack.pop()
        self.assertEqual(stack.getMin(), 5, f"{stack_class.__name__}: Min should still be 5 after popping 10")
        stack.push(1)
        self.assertEqual(stack.getMin(), 1, f"{stack_class.__name__}: Min should be 1")
        stack.pop()
        self.assertEqual(stack.getMin(), 5, f"{stack_class.__name__}: Min should revert to 5")

        # Test Case 6: Popping all elements
        stack = stack_class()
        stack.push(10)
        stack.push(20)
        stack.pop()
        stack.pop()
        self.assertIsNone(stack.top(), f"{stack_class.__name__}: Top should be None after all elements popped")
        self.assertIsNone(stack.getMin(), f"{stack_class.__name__}: Min should be None after all elements popped")
        stack.pop()
        self.assertIsNone(stack.top(), f"{stack_class.__name__}: Top should remain None")
        self.assertIsNone(stack.getMin(), f"{stack_class.__name__}: Min should remain None")

        # Test Case 7: Duplicate minimum values
        stack = stack_class()
        stack.push(5)
        stack.push(2)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should be 2 with duplicates")
        stack.pop()
        self.assertEqual(stack.getMin(), 2, f"{stack_class.__name__}: Min should still be 2")
        stack.pop()
        self.assertEqual(
            stack.getMin(), 2, f"{stack_class.__name__}: Min should still be 2 after popping one duplicate min"
        )
        stack.pop()
        self.assertEqual(stack.getMin(), 5, f"{stack_class.__name__}: Min should be 5 after all 2s are popped")

    def test_min_stack_two_lists(self):
        self.run_tests_for_stack_type(MinStackTwoLists)

    def test_min_stack_tuple(self):
        self.run_tests_for_stack_type(MinStackTuple)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
    # Using exit=False and argv to make it runnable in environments like Jupyter notebooks or IDEs
    # If running from command line, `unittest.main()` is sufficient.
