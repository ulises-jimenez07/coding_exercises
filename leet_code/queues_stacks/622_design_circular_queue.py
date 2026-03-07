"""
Problem: Design Circular Queue - implement a FIFO data structure with fixed size.

Approach:
- Version 1: Linked List based circular queue.
- Version 2: Array (List) based circular queue using head index and size.
- Time complexity: All operations are O(1).
- Space complexity: O(k) where k is the requested capacity.
"""

import unittest
from typing import (
    List,
    Optional,
    Type,
    Union,
)


class Node:
    """Simple node for linked list implementation."""

    def __init__(self, value: int, next_node: Optional["Node"] = None):
        """Initializes a node with a value and optional next pointer."""
        self.value: int = value
        self.next: Optional[Node] = next_node


class MyCircularQueueV1:
    """
    Circular queue implementation using a linked list.
    Tracks head and tail nodes to allow O(1) operations.
    """

    def __init__(self, k: int) -> None:
        """Initializes the queue with capacity k."""
        self.capacity: int = k
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.count: int = 0

    def enQueue(self, value: int) -> bool:
        """Inserts an element into the queue. Returns true if successful."""
        if self.isFull():
            return False

        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            # Connect current tail to new node and update tail
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node

        self.count += 1
        return True

    def deQueue(self) -> bool:
        """Deletes an element from the queue. Returns true if successful."""
        if self.isEmpty() or self.head is None:
            return False

        # Move head to the next node
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        """Gets the front item from the queue. Returns -1 if empty."""
        if self.head is None:
            return -1
        return self.head.value

    def Rear(self) -> int:
        """Gets the last item from the queue. Returns -1 if empty."""
        if self.tail is None:
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        """Checks whether the circular queue is empty."""
        return self.count == 0

    def isFull(self) -> bool:
        """Checks whether the circular queue is full."""
        return self.count == self.capacity


class MyCircularQueueV2:
    """
    Circular queue implementation using a fixed-size array.
    Uses head index and current size to manage capacity.
    """

    def __init__(self, k: int) -> None:
        """Initializes the queue with capacity k."""
        self.queue: List[int] = [0] * k
        self.head_index: int = 0
        self.count: int = 0
        self.capacity: int = k

    def enQueue(self, value: int) -> bool:
        """Inserts an element into the circular queue."""
        if self.isFull():
            return False

        # Calculate insertion index using modulo arithmetic
        insert_idx = (self.head_index + self.count) % self.capacity
        self.queue[insert_idx] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """Deletes an element from the circular queue."""
        if self.isEmpty():
            return False

        # Advance head index and decrement count
        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """Gets the front item from the queue."""
        if self.isEmpty():
            return -1
        return self.queue[self.head_index]

    def Rear(self) -> int:
        """Gets the last item from the queue."""
        if self.isEmpty():
            return -1
        # Tail is at (head + count - 1) index
        rear_idx = (self.head_index + self.count - 1) % self.capacity
        return self.queue[rear_idx]

    def isEmpty(self) -> bool:
        """Checks whether the circular queue is empty."""
        return self.count == 0

    def isFull(self) -> bool:
        """Checks whether the circular queue is full."""
        return self.count == self.capacity


class TestCircularQueues(unittest.TestCase):
    """Unit tests for both circular queue implementations."""

    def test_leetcode_sequence(self) -> None:
        """Tests the sequence from LeetCode example."""
        q_classes: List[Type[Union[MyCircularQueueV1, MyCircularQueueV2]]] = [
            MyCircularQueueV1,
            MyCircularQueueV2,
        ]
        for q_class in q_classes:
            q = q_class(3)
            self.assertTrue(q.enQueue(1))
            self.assertTrue(q.enQueue(2))
            self.assertTrue(q.enQueue(3))
            self.assertFalse(q.enQueue(4))  # Full
            self.assertEqual(q.Rear(), 3)
            self.assertTrue(q.isFull())
            self.assertTrue(q.deQueue())
            self.assertTrue(q.enQueue(4))
            self.assertEqual(q.Rear(), 4)

    def test_empty_and_single(self) -> None:
        """Tests behavior with empty and single element queues."""
        q_classes: List[Type[Union[MyCircularQueueV1, MyCircularQueueV2]]] = [
            MyCircularQueueV1,
            MyCircularQueueV2,
        ]
        for q_class in q_classes:
            q = q_class(1)
            self.assertTrue(q.isEmpty())
            self.assertEqual(q.Front(), -1)
            self.assertTrue(q.enQueue(10))
            self.assertTrue(q.isFull())
            self.assertEqual(q.Front(), 10)
            self.assertEqual(q.Rear(), 10)
            self.assertTrue(q.deQueue())
            self.assertTrue(q.isEmpty())

    def test_overwrite_behavior(self) -> None:
        """Ensures logic handles wrap-around correctly."""
        q_classes: List[Type[Union[MyCircularQueueV1, MyCircularQueueV2]]] = [
            MyCircularQueueV1,
            MyCircularQueueV2,
        ]
        for q_class in q_classes:
            q = q_class(2)
            q.enQueue(1)
            q.enQueue(2)
            q.deQueue()  # Removes 1
            q.enQueue(3)  # Wraps or adds new node
            self.assertEqual(q.Front(), 2)
            self.assertEqual(q.Rear(), 3)

    def test_ordered_ops(self) -> None:
        """Tests multiple operations in order using enumerate."""
        q_classes: List[Type[Union[MyCircularQueueV1, MyCircularQueueV2]]] = [
            MyCircularQueueV1,
            MyCircularQueueV2,
        ]
        for q_class in q_classes:
            capacity = 5
            q = q_class(capacity)
            elements = [10, 20, 30, 40, 50]

            for i, val in enumerate(elements):
                self.assertTrue(q.enQueue(val), f"Failed to enqueue {val} at index {i}")

            self.assertTrue(q.isFull())

            for i, val in enumerate(elements):
                self.assertEqual(q.Front(), val, f"Front mismatch at index {i}")
                self.assertTrue(q.deQueue(), f"Failed to dequeue at index {i}")

            self.assertTrue(q.isEmpty())


if __name__ == "__main__":
    unittest.main()
