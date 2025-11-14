"""
Problem: Happy Number (LeetCode 202)

A happy number is defined by the following process:
- Replace the number by the sum of the squares of its digits
- Repeat until the number equals 1, or loops in a cycle
- Numbers that end in 1 are happy

Approach 1: HashSet Detection
- Track seen numbers in a set to detect cycles
- Time complexity: O(log n)
- Space complexity: O(log n)

Approach 2: Floyd's Cycle Detection
- Use fast & slow pointers like in linked list cycle detection
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest


class SolutionHashSet:
    """Solution using HashSet to detect cycles in the happy number sequence."""

    def isHappy(self, n: int) -> bool:
        """
        Determines if a number is happy using a HashSet to detect cycles.
        """

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


class SolutionFloydCycle:
    """Solution using Floyd's Cycle Detection algorithm with fast and slow pointers."""

    def isHappy(self, n: int) -> bool:
        """
        Determines if a number is happy using Floyd's Cycle Detection.
        """

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        slow = n
        fast = get_next(n)

        while fast not in (1, slow):
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1


class TestHappyNumber(unittest.TestCase):
    """Unit tests for both happy number solution implementations."""

    def setUp(self):
        self.solution_set = SolutionHashSet()
        self.solution_floyd = SolutionFloydCycle()

    def test_happy_number_19(self):
        # 19 -> 82 -> 68 -> 100 -> 1
        self.assertTrue(self.solution_set.isHappy(19))
        self.assertTrue(self.solution_floyd.isHappy(19))

    def test_unhappy_number_2(self):
        # 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (cycle)
        self.assertFalse(self.solution_set.isHappy(2))
        self.assertFalse(self.solution_floyd.isHappy(2))

    def test_happy_number_1(self):
        self.assertTrue(self.solution_set.isHappy(1))
        self.assertTrue(self.solution_floyd.isHappy(1))

    def test_happy_number_7(self):
        # 7 -> 49 -> 97 -> 130 -> 10 -> 1
        self.assertTrue(self.solution_set.isHappy(7))
        self.assertTrue(self.solution_floyd.isHappy(7))

    def test_happy_number_10(self):
        self.assertTrue(self.solution_set.isHappy(10))
        self.assertTrue(self.solution_floyd.isHappy(10))

    def test_unhappy_number_4(self):
        # 4 -> 16 -> 37 -> ... -> 4 (cycle)
        self.assertFalse(self.solution_set.isHappy(4))
        self.assertFalse(self.solution_floyd.isHappy(4))

    def test_happy_number_100(self):
        self.assertTrue(self.solution_set.isHappy(100))
        self.assertTrue(self.solution_floyd.isHappy(100))

    def test_unhappy_number_20(self):
        self.assertFalse(self.solution_set.isHappy(20))
        self.assertFalse(self.solution_floyd.isHappy(20))

    def test_happy_number_23(self):
        # 23 -> 13 -> 10 -> 1
        self.assertTrue(self.solution_set.isHappy(23))
        self.assertTrue(self.solution_floyd.isHappy(23))

    def test_large_happy_number(self):
        self.assertTrue(self.solution_set.isHappy(68))
        self.assertTrue(self.solution_floyd.isHappy(68))


if __name__ == "__main__":
    unittest.main()
