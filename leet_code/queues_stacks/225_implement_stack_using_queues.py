"""
Problem: Implement Stack using Queues - simulate LIFO behavior using FIFO queues.

Approach:
- Version 1: Uses a single deque and rotates elements after each push.
- Version 2: Uses two lists as queues, moving elements to maintain stack order.
- Time complexity: Push is O(n), Pop/Top are O(1).
- Space complexity: O(n) to store elements.
"""

import unittest
from collections import deque
from typing import (
    List,
    Type,
    Union,
)


class MyStackV1:
    """
    Implements a stack using a single queue (deque).
    Rotates the queue on every push to maintain top element at front.
    """

    def __init__(self) -> None:
        """Initializes the stack structure."""
        self.queue: deque[int] = deque()

    def push(self, x: int) -> None:
        """Adds an element to the stack and rotates the queue."""
        self.queue.append(x)
        # Shift existing elements behind the new top
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """Removes and returns the top element."""
        return self.queue.popleft()

    def top(self) -> int:
        """Returns the top element without removing it."""
        return self.queue[0]

    def empty(self) -> bool:
        """Returns whether the stack is empty."""
        return len(self.queue) == 0


class MyStackV2:
    """
    Implements a stack using two lists as queues.
    Maintains stack order by swapping elements between queues on push.
    """

    def __init__(self) -> None:
        """Initializes the two-queue structure."""
        self.q1: List[int] = []
        self.q2: List[int] = []

    def push(self, x: int) -> None:
        """Adds an element by staging it in q2 and moving q1 elements."""
        # 1. Add new element to the empty queue
        self.q2.append(x)

        # 2. Move all elements from q1 to q2 to put x at the front
        while self.q1:
            self.q2.append(self.q1.pop(0))

        # 3. Swap names so q1 is always the primary queue
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """Removes the front of q1 which is the stack top."""
        return self.q1.pop(0)

    def top(self) -> int:
        """Peeks the front of q1."""
        return self.q1[0]

    def empty(self) -> bool:
        """Checks if the primary queue is empty."""
        return not self.q1


class TestMyStacks(unittest.TestCase):
    """Unit tests for both stack implementations."""

    def test_leetcode_example(self) -> None:
        """Verifies the standard LeetCode test case."""
        stack_classes: List[Type[Union[MyStackV1, MyStackV2]]] = [MyStackV1, MyStackV2]
        for stack_class in stack_classes:
            stack = stack_class()
            stack.push(1)
            stack.push(2)
            self.assertEqual(stack.top(), 2)
            self.assertEqual(stack.pop(), 2)
            self.assertFalse(stack.empty())

    def test_single_element(self) -> None:
        """Tests stack behavior with a single element."""
        stack_classes: List[Type[Union[MyStackV1, MyStackV2]]] = [MyStackV1, MyStackV2]
        for stack_class in stack_classes:
            stack = stack_class()
            stack.push(10)
            self.assertEqual(stack.top(), 10)
            self.assertFalse(stack.empty())
            self.assertEqual(stack.pop(), 10)
            self.assertTrue(stack.empty())

    def test_multiple_elements_sequence(self) -> None:
        """Tests a sequence of pushes and pops using enumerate."""
        stack_classes: List[Type[Union[MyStackV1, MyStackV2]]] = [MyStackV1, MyStackV2]
        for stack_class in stack_classes:
            stack = stack_class()
            elements = [10, 20, 30, 40]

            # Push elements and check top at each step
            for i, val in enumerate(elements):
                stack.push(val)
                self.assertEqual(stack.top(), val, f"Failed at index {i}")

            # Pop elements and check LIFO order
            for i, val in enumerate(reversed(elements)):
                self.assertEqual(stack.pop(), val, f"Failed pop at reversed index {i}")

            self.assertTrue(stack.empty())

    def test_empty_stack_behavior(self) -> None:
        """Verifies empty() method behavior."""
        stack_classes: List[Type[Union[MyStackV1, MyStackV2]]] = [MyStackV1, MyStackV2]
        for stack_class in stack_classes:
            stack = stack_class()
            self.assertTrue(stack.empty())
            stack.push(1)
            self.assertFalse(stack.empty())
            stack.pop()
            self.assertTrue(stack.empty())


if __name__ == "__main__":
    unittest.main()
