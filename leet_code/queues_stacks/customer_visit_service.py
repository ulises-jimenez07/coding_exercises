"""
Problem: Customer Visit Service
Track customer visits and return the first customer who has visited exactly once.

Approach:
- Store visit counts in a dictionary
- Keep first-time visitors in a queue in arrival order
- Lazily remove repeated visitors from the front when reading the answer
- Time complexity: O(1) amortized per operation
- Space complexity: O(n)
"""

import unittest
from collections import deque


class CustomerService:
    """Tracks customer visits and exposes the first one-time visitor."""

    def __init__(self):
        self.counts = {}
        self.queue = deque()

    def post_customer_visit(self, customer_id):
        """Record a customer visit."""
        self.counts[customer_id] = self.counts.get(customer_id, 0) + 1
        if self.counts[customer_id] == 1:
            self.queue.append(customer_id)

    def get_first_one_time_visitor(self):
        """Return the earliest visitor with exactly one visit, or None."""
        while self.queue and self.counts[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else None


class TestCustomerService(unittest.TestCase):
    """Unit tests for CustomerService."""

    def setUp(self):
        self.service = CustomerService()

    def test_empty_service(self):
        self.assertIsNone(self.service.get_first_one_time_visitor())

    def test_first_unique_visitor(self):
        self.service.post_customer_visit("alice")
        self.service.post_customer_visit("bob")

        self.assertEqual(self.service.get_first_one_time_visitor(), "alice")

    def test_lazy_removal_after_repeated_visit(self):
        self.service.post_customer_visit("alice")
        self.service.post_customer_visit("bob")
        self.service.post_customer_visit("alice")

        self.assertEqual(self.service.get_first_one_time_visitor(), "bob")

    def test_all_visitors_repeat(self):
        visits = ["alice", "bob", "alice", "bob"]
        for customer_id in visits:
            self.service.post_customer_visit(customer_id)

        self.assertIsNone(self.service.get_first_one_time_visitor())

    def test_integer_customer_ids(self):
        visits = [10, 20, 10, 30]
        for customer_id in visits:
            self.service.post_customer_visit(customer_id)

        self.assertEqual(self.service.get_first_one_time_visitor(), 20)


if __name__ == "__main__":
    unittest.main()
