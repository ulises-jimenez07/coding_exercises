"""
Problem: Design Circular Deque - implement a double-ended queue with fixed size.

Approach:
- Version 1: Doubly Linked List based circular deque.
- Version 2: Array (List) based circular deque using head index and size.
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


class DoubleNode:
    """Node for a doubly linked list implementation."""

    def __init__(
        self,
        value: int,
        next_node: Optional["DoubleNode"] = None,
        prev_node: Optional["DoubleNode"] = None,
    ):
        """Initializes a node with a value and optional next/prev pointers."""
        self.value: int = value
        self.next: Optional[DoubleNode] = next_node
        self.prev: Optional[DoubleNode] = prev_node


class MyCircularDequeV1:
    """
    Circular deque implementation using a doubly linked list.
    Maintains head and tail pointers for O(1) front and rear operations.
    """

    def __init__(self, k: int):
        """Initializes the deque with capacity k."""
        self.capacity: int = k
        self.head: Optional[DoubleNode] = None
        self.tail: Optional[DoubleNode] = None
        self.count: int = 0

    def insertFront(self, value: int) -> bool:
        """Adds an item at the front of Deque. Returns true if successful."""
        if self.isFull():
            return False

        if self.head is None:
            # First element: head and tail point to it
            self.head = self.tail = DoubleNode(value)
        else:
            # Update current head's prev and set new head
            new_head = DoubleNode(value, self.head)
            self.head.prev = new_head
            self.head = new_head

        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        """Adds an item at the rear of Deque. Returns true if successful."""
        if self.isFull():
            return False

        if self.head is None:
            # First element: head and tail point to it
            self.head = self.tail = DoubleNode(value)
        else:
            # Update current tail's next and set new tail
            new_node = DoubleNode(value, None, self.tail)
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node

        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """Deletes an item from the front of Deque. Returns true if successful."""
        if self.isEmpty() or self.head is None:
            return False

        if self.count == 1:
            self.head = self.tail = None
        else:
            # Advance head and clear its prev pointer
            self.head = self.head.next
            if self.head:
                self.head.prev = None

        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """Deletes an item from the rear of Deque. Returns true if successful."""
        if self.isEmpty() or self.tail is None:
            return False

        if self.count == 1:
            self.head = self.tail = None
        else:
            # Move tail back and clear its next pointer
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

        self.count -= 1
        return True

    def getFront(self) -> int:
        """Gets the front item from the deque. Returns -1 if empty."""
        return -1 if self.isEmpty() or self.head is None else self.head.value

    def getRear(self) -> int:
        """Gets the last item from the deque. Returns -1 if empty."""
        return -1 if self.isEmpty() or self.tail is None else self.tail.value

    def isEmpty(self) -> bool:
        """Checks whether the circular deque is empty."""
        return self.count == 0

    def isFull(self) -> bool:
        """Checks whether the circular deque is full."""
        return self.count == self.capacity


class MyCircularDequeV2:
    """
    Circular deque implementation using a fixed-size array.
    Uses head index and current size for efficient wrap-around.
    """

    def __init__(self, k: int):
        """Initializes the deque with capacity k."""
        self.queue: List[int] = [0] * k
        self.head_index: int = 0
        self.count: int = 0
        self.capacity: int = k

    def insertFront(self, value: int) -> bool:
        """Adds an item at the front of Deque."""
        if self.isFull():
            return False

        # Move head index backward with wrap-around
        self.head_index = (self.head_index - 1) % self.capacity
        self.queue[self.head_index] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        """Adds an item at the rear of Deque."""
        if self.isFull():
            return False

        # Tail is at (head + count) index with wrap-around
        insert_idx = (self.head_index + self.count) % self.capacity
        self.queue[insert_idx] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """Deletes an item from the front of Deque."""
        if self.isEmpty():
            return False

        # Advance head index with wrap-around
        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """Deletes an item from the rear of Deque."""
        if self.isEmpty():
            return False

        # Simply decrement count; future insertions will overwrite
        self.count -= 1
        return True

    def getFront(self) -> int:
        """Gets the front item from the deque."""
        if self.isEmpty():
            return -1
        return self.queue[self.head_index]

    def getRear(self) -> int:
        """Gets the last item from the deque."""
        if self.isEmpty():
            return -1
        # Rear index calculation based on head and count
        rear_idx = (self.head_index + self.count - 1) % self.capacity
        return self.queue[rear_idx]

    def isEmpty(self) -> bool:
        """Checks whether the circular deque is empty."""
        return self.count == 0

    def isFull(self) -> bool:
        """Checks whether the circular deque is full."""
        return self.count == self.capacity


class TestCircularDeques(unittest.TestCase):
    """Unit tests for both circular deque implementations."""

    def test_leetcode_example(self) -> None:
        """Tests the sequence from LeetCode example 1."""
        deque_classes: List[Type[Union[MyCircularDequeV1, MyCircularDequeV2]]] = [
            MyCircularDequeV1,
            MyCircularDequeV2,
        ]
        for deque_class in deque_classes:
            obj = deque_class(3)
            self.assertTrue(obj.insertLast(1))
            self.assertTrue(obj.insertLast(2))
            self.assertTrue(obj.insertFront(3))
            self.assertFalse(obj.insertFront(4))  # Full
            self.assertEqual(obj.getRear(), 2)
            self.assertTrue(obj.isFull())
            self.assertTrue(obj.deleteLast())
            self.assertTrue(obj.insertFront(4))
            self.assertEqual(obj.getFront(), 4)

    def test_empty_and_single_element(self) -> None:
        """Tests behavior with empty and single element deques."""
        deque_classes: List[Type[Union[MyCircularDequeV1, MyCircularDequeV2]]] = [
            MyCircularDequeV1,
            MyCircularDequeV2,
        ]
        for deque_class in deque_classes:
            obj = deque_class(1)
            self.assertTrue(obj.isEmpty())
            self.assertEqual(obj.getFront(), -1)
            self.assertTrue(obj.insertFront(10))
            self.assertTrue(obj.isFull())
            self.assertEqual(obj.getRear(), 10)
            self.assertTrue(obj.deleteFront())
            self.assertTrue(obj.isEmpty())
            self.assertFalse(obj.deleteLast())

    def test_ordered_ops(self) -> None:
        """Tests multiple operations in order using enumerate."""
        deque_classes: List[Type[Union[MyCircularDequeV1, MyCircularDequeV2]]] = [
            MyCircularDequeV1,
            MyCircularDequeV2,
        ]
        for deque_class in deque_classes:
            capacity = 5
            obj = deque_class(capacity)
            elements = [10, 20, 30, 40, 50]

            # Insert at last and verify order
            for i, val in enumerate(elements):
                self.assertTrue(obj.insertLast(val), f"Failed to insertLast {val} at index {i}")

            for i, val in enumerate(elements):
                self.assertEqual(obj.getFront(), val, f"Front mismatch at index {i}")
                self.assertTrue(obj.deleteFront(), f"Failed to deleteFront at index {i}")

            # Insert at front and verify order
            for i, val in enumerate(elements):
                self.assertTrue(obj.insertFront(val), f"Failed to insertFront {val} at index {i}")

            for i, val in enumerate(elements):
                self.assertEqual(obj.getRear(), val, f"Rear mismatch at index {i}")
                self.assertTrue(obj.deleteLast(), f"Failed to deleteLast at index {i}")


if __name__ == "__main__":
    unittest.main()
