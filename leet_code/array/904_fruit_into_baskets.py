import unittest
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

        You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

        You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
        Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
        Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
        Given the integer array fruits, return the maximum number of fruits you can pick.
        """
        basket = {}  # Dictionary to store fruit types and their counts
        left = 0  # Left pointer of the sliding window
        max_fruits = 0  # Initialize max_fruits

        # Iterate through the fruits using the right pointer of the sliding window
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1  # Add fruit to the basket

            # If more than two types of fruits in the basket
            while len(basket) > 2:
                basket[fruits[left]] -= 1  # Remove fruit from the left side
                if basket[fruits[left]] == 0:  # if count becomes zero
                    del basket[fruits[left]]  # remove fruit type from basket
                left += 1  # Shrink the window from the left

            max_fruits = max(max_fruits, right - left + 1)  # Calculate max fruits

        return max_fruits


class TestTotalFruit(unittest.TestCase):
    def test_example_1(self):
        fruits = [1, 2, 1]
        expected = 3
        self.assertEqual(Solution().totalFruit(fruits), expected)

    def test_example_2(self):
        fruits = [0, 1, 2, 2]
        expected = 3
        self.assertEqual(Solution().totalFruit(fruits), expected)

    def test_example_3(self):
        fruits = [1, 2, 3, 2, 2]
        expected = 4
        self.assertEqual(Solution().totalFruit(fruits), expected)

    def test_example_4(self):  # Test case with all same fruits
        fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
        expected = 5
        self.assertEqual(Solution().totalFruit(fruits), expected)

    def test_empty_list(self):
        fruits = []
        expected = 0
        self.assertEqual(Solution().totalFruit(fruits), expected)

    def test_one_fruit_type(self):
        fruits = [1, 1, 1, 1, 1]
        expected = 5
        self.assertEqual(Solution().totalFruit(fruits), expected)

    def test_two_fruit_types(self):
        fruits = [1, 0, 1, 4, 1, 4, 1, 2, 3]
        expected = 5
        self.assertEqual(Solution().totalFruit(fruits), expected)


if __name__ == "__main__":
    unittest.main()
