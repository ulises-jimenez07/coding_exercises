"""
Problem: Revenue Hierarchy
Calculate the total revenue for a customer and their full referral tree.

Approach:
- Model each customer as a tree node with direct revenue and referrals
- Use DFS recursion to sum direct revenue plus every descendant referral's revenue
- Time complexity: O(n)
- Space complexity: O(h) for recursion depth, where h is the tree height
"""

import unittest
from dataclasses import (
    dataclass,
    field,
)


@dataclass
class Customer:
    """Customer node in a referral revenue tree."""

    customer_id: int
    direct_revenue: int
    referrals: list["Customer"] = field(default_factory=list)


def get_total_revenue(customer):
    """Return direct and referral revenue for a customer subtree."""
    return customer.direct_revenue + sum(get_total_revenue(referral) for referral in customer.referrals)


class TestRevenueHierarchy(unittest.TestCase):
    """Unit tests for get_total_revenue."""

    def test_single_customer(self):
        customer = Customer(customer_id=1, direct_revenue=100)

        self.assertEqual(get_total_revenue(customer), 100)

    def test_customer_with_direct_referrals(self):
        customer = Customer(
            customer_id=1,
            direct_revenue=100,
            referrals=[
                Customer(customer_id=2, direct_revenue=50),
                Customer(customer_id=3, direct_revenue=25),
            ],
        )

        self.assertEqual(get_total_revenue(customer), 175)

    def test_customer_with_nested_referrals(self):
        customer = Customer(
            customer_id=1,
            direct_revenue=100,
            referrals=[
                Customer(
                    customer_id=2,
                    direct_revenue=50,
                    referrals=[
                        Customer(customer_id=4, direct_revenue=10),
                        Customer(customer_id=5, direct_revenue=15),
                    ],
                ),
                Customer(customer_id=3, direct_revenue=25),
            ],
        )

        self.assertEqual(get_total_revenue(customer), 200)

    def test_zero_revenue_customers(self):
        customer = Customer(
            customer_id=1,
            direct_revenue=0,
            referrals=[Customer(customer_id=2, direct_revenue=0)],
        )

        self.assertEqual(get_total_revenue(customer), 0)


if __name__ == "__main__":
    unittest.main()
