"""
Problem: Given a list of products with quantities and weights, find the minimum
number of items per box (capacity) needed to ship all products using at most
maxBoxes boxes, where each box holds at most maxWeightPerBox total weight.

Approach:
- Binary search on capacity range (1 to max(quantities))
- For each candidate capacity, count boxes needed across all products
- Items per box are limited by capacity, weight constraint, and remaining quantity
- Time complexity: O(n log(max_qty)) where n is number of products
- Space complexity: O(1)
"""

import unittest
from typing import List


class Solution:
    """Provides a method to find the minimum shipping capacity across all products."""

    def minimumShippingCapacity(
        self,
        quantities: List[int],
        weights: List[int],
        maxBoxes: int,
        maxWeightPerBox: int,
    ) -> int:
        """
        Finds the minimum per-box item capacity such that all products can be
        shipped using at most maxBoxes boxes.

        Each product's items must stay together by type within a box; a box holds
        at most maxWeightPerBox total weight and at most `capacity` items.
        """

        def count_boxes(capacity: int) -> int:
            """Counts how many boxes are needed to ship all products at the given capacity."""
            boxes = 0
            for i, qty in enumerate(quantities):
                remaining = qty
                while remaining > 0:
                    items_per_box = min(remaining, capacity, maxWeightPerBox // weights[i])
                    boxes += 1
                    remaining -= items_per_box
            return boxes

        left, right = 1, max(quantities)

        while left < right:
            mid = (left + right) // 2
            if count_boxes(mid) <= maxBoxes:
                right = mid
            else:
                left = mid + 1

        return right


# --- Unit Tests ---


class TestMinimumShippingCapacity(unittest.TestCase):
    """
    Unit tests for the minimumShippingCapacity method in the Solution class.
    """

    def setUp(self):
        self.sol = Solution()

    def test_basic_case(self):
        """Tests a basic case with two products where weight limits box fill."""
        quantities = [3, 2]
        weights = [1, 2]
        maxBoxes = 3
        maxWeightPerBox = 4
        self.assertEqual(self.sol.minimumShippingCapacity(quantities, weights, maxBoxes, maxWeightPerBox), 2)

    def test_single_product_no_weight_constraint(self):
        """Tests a single product where only capacity limits packing."""
        quantities = [10]
        weights = [1]
        maxBoxes = 2
        maxWeightPerBox = 10
        self.assertEqual(self.sol.minimumShippingCapacity(quantities, weights, maxBoxes, maxWeightPerBox), 5)

    def test_weight_constraint_drives_result(self):
        """Tests that a tight weight limit forces more boxes regardless of capacity."""
        quantities = [4]
        weights = [3]
        maxBoxes = 2
        maxWeightPerBox = 6
        # weight allows 2 items/box; capacity must be >= 2 to fit in 2 boxes
        self.assertEqual(self.sol.minimumShippingCapacity(quantities, weights, maxBoxes, maxWeightPerBox), 2)

    def test_many_products_exact_fit(self):
        """Tests multiple single-item products that each need exactly one box."""
        quantities = [1, 1, 1]
        weights = [1, 1, 1]
        maxBoxes = 3
        maxWeightPerBox = 1
        self.assertEqual(self.sol.minimumShippingCapacity(quantities, weights, maxBoxes, maxWeightPerBox), 1)

    def test_minimum_capacity_is_one(self):
        """Tests a case where capacity of 1 is sufficient to meet the box budget."""
        quantities = [3]
        weights = [1]
        maxBoxes = 3
        maxWeightPerBox = 5
        self.assertEqual(self.sol.minimumShippingCapacity(quantities, weights, maxBoxes, maxWeightPerBox), 1)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
