"""
Problem: Implement Queue using Stacks (LeetCode 232)

Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue
(push, peek, pop, and empty).

Approach: Two Stacks
- Use two stacks: enqueue_stack for incoming elements and dequeue_stack
  for outgoing elements.
- When popping or peeking, if dequeue_stack is empty, transfer all
  elements from enqueue_stack to dequeue_stack. This reverses the order,
  making it FIFO.
- Time complexity: Amortized O(1) for all operations.
- Space complexity: O(n) to store the elements.
"""

import unittest
from typing import (
    List,
    Optional,
)


class MyQueue:
    """Implement a FIFO queue using two stacks."""

    def __init__(self) -> None:
        """Initialize the two stacks for queue operations."""
        self.dequeue_stack: List[int] = []
        self.enqueue_stack: List[int] = []

    def push(self, x: int) -> None:
        """Push element x to the back of the queue."""
        self.enqueue_stack.append(x)

    def _transfer_enqueue_to_dequeue(self) -> None:
        """Internal helper to move elements from enqueue to dequeue stack."""
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

    def pop(self) -> Optional[int]:
        """Removes the element from the front of the queue and returns it."""
        self._transfer_enqueue_to_dequeue()
        return self.dequeue_stack.pop() if self.dequeue_stack else None

    def peek(self) -> Optional[int]:
        """Get the front element without removing it."""
        self._transfer_enqueue_to_dequeue()
        return self.dequeue_stack[-1] if self.dequeue_stack else None

    def empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise."""
        return not (self.dequeue_stack or self.enqueue_stack)


class TestMyQueue(unittest.TestCase):
    """Unit tests for the MyQueue class implementation."""

    def setUp(self):
        """Set up a fresh MyQueue instance for each test."""
        self.queue = MyQueue()

    def test_leetcode_example(self):
        """Test with the example provided in the LeetCode description."""
        self.queue.push(1)
        self.queue.push(2)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.pop(), 1)
        self.assertFalse(self.queue.empty())

    def test_multiple_push_pop(self):
        """Test a sequence of multiple push and pop operations."""
        for i in range(1, 6):
            self.queue.push(i)

        # Pop half
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 2)

        # Push more
        self.queue.push(6)

        # Pop remaining in correct order
        self.assertEqual(self.queue.pop(), 3)
        self.assertEqual(self.queue.pop(), 4)
        self.assertEqual(self.queue.pop(), 5)
        self.assertEqual(self.queue.pop(), 6)
        self.assertTrue(self.queue.empty())

    def test_empty_operations(self):
        """Test operations on an empty queue."""
        self.assertTrue(self.queue.empty())
        self.assertIsNone(self.queue.peek())
        self.assertIsNone(self.queue.pop())

    def test_single_element(self):
        """Test operations with a single element."""
        self.queue.push(10)
        self.assertFalse(self.queue.empty())
        self.assertEqual(self.queue.peek(), 10)
        self.assertEqual(self.queue.pop(), 10)
        self.assertTrue(self.queue.empty())

    def test_interleaved_operations(self):
        """Test interleaved push/pop operations using subtests."""
        operations = [
            ("push", 1),
            ("push", 2),
            ("pop", 1),
            ("push", 3),
            ("peek", 2),
            ("pop", 2),
            ("pop", 3),
            ("empty", True),
        ]

        for i, (op, val) in enumerate(operations):
            with self.subTest(operation_index=i, op=op):
                if op == "push":
                    self.queue.push(val)
                elif op == "pop":
                    self.assertEqual(self.queue.pop(), val)
                elif op == "peek":
                    self.assertEqual(self.queue.peek(), val)
                elif op == "empty":
                    self.assertEqual(self.queue.empty(), val)


if __name__ == "__main__":
    unittest.main()
