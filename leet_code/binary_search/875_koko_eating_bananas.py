import math
import unittest
from typing import List

class Solution:
    """
    Finds the minimum integer eating speed 'k' for a monkey to eat all bananas
    in a given list of piles within 'h' hours.
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Calculates the minimum integer eating speed 'k'.

        Args:
            piles: A list of integers representing the number of bananas in each pile.
            h: The maximum number of hours the monkey has to eat all bananas.

        Returns:
            The minimum integer eating speed 'k'.
        """
        # The minimum possible speed is 1, and the maximum is the size of the largest pile.
        # We perform a binary search on the possible speeds.
        start = 1
        end = max(piles)
        ans = end  # Initialize ans to a large value

        while start <= end:
            mid = (start + end) // 2
            # If the time taken with 'mid' speed is too long, we need to eat faster.
            if self.count_hours(piles, mid) > h:
                start = mid + 1
            # If the time is within the limit, 'mid' is a potential answer.
            # We try for a smaller speed by searching in the lower half.
            else:
                ans = mid
                end = mid - 1

        return ans

    def count_hours(self, piles: List[int], speed: int) -> int:
        """
        Calculates the total hours required to eat all piles at a given speed.

        Args:
            piles: A list of integers representing the number of bananas in each pile.
            speed: The eating speed 'k'.

        Returns:
            The total hours required.
        """
        # For each pile, we calculate the hours needed (ceil(pile/speed)) and sum them up.
        return sum(math.ceil(pile / speed) for pile in piles)

class TestMinEatingSpeed(unittest.TestCase):
    """
    Unit tests for the minEatingSpeed method.
    """

    def test_example_1(self):
        """Test with a standard example from LeetCode."""
        sol = Solution()
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(sol.minEatingSpeed(piles, h), 4)

    def test_example_2(self):
        """Test with a different example."""
        sol = Solution()
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(sol.minEatingSpeed(piles, h), 30)

    def test_example_3(self):
        """Test with an example where the speed is 1."""
        sol = Solution()
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(sol.minEatingSpeed(piles, h), 23)

    def test_single_pile(self):
        """Test with a single pile."""
        sol = Solution()
        piles = [10]
        h = 3
        self.assertEqual(sol.minEatingSpeed(piles, h), 4)

    def test_large_numbers(self):
        """Test with large numbers in piles and hours."""
        sol = Solution()
        piles = [1000000000]
        h = 2
        self.assertEqual(sol.minEatingSpeed(piles, h), 500000000)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)