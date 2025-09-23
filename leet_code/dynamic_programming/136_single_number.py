from typing import List
import unittest

class Solution:
    """
    Finds the single element that appears only once in an array 
    where every other element appears exactly twice.
    """
    def singleNumber(self, nums: List[int]) -> int:
        """
        Calculates the single number using the XOR bitwise operation.

        The XOR operation (^) has the following properties:
        - a ^ a = 0 (XORing a number with itself results in 0)
        - a ^ 0 = a (XORing a number with 0 results in the number itself)
        - It is commutative and associative (a ^ b ^ c = a ^ c ^ b)

        By XORing all numbers in the array, all pairs of duplicate numbers will
        cancel each other out (e.g., 2 ^ 2 = 0), leaving only the single unique
        number XORed with 0, which results in the unique number itself.

        Args:
            nums: A list of integers where all elements appear twice except for one.

        Returns:
            The single integer that appears only once.
        """
        ans = 0
        for num in nums:
            # XOR each number in the list with the accumulator 'ans'
            ans ^= num

        return ans

# ---

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def test_single_number_positive(self):
        """
        Tests with a basic case where the single number is positive.
        """
        # Test case: [2, 2, 1] -> The single number should be 1
        nums = [2, 2, 1]
        self.assertEqual(Solution().singleNumber(nums), 1)

    def test_single_number_negative(self):
        """
        Tests with a case where the single number is negative.
        """
        # Test case: [-1, -1, -2] -> The single number should be -2
        nums = [-1, -1, -2]
        self.assertEqual(Solution().singleNumber(nums), -2)

    def test_single_number_zero(self):
        """
        Tests with a case where the single number is zero.
        """
        # Test case: [0, 1, 0] -> The single number should be 1
        nums = [0, 1, 0]
        self.assertEqual(Solution().singleNumber(nums), 1)

    def test_single_number_long_list(self):
        """
        Tests with a longer list of numbers.
        """
        # Test case: [4, 1, 2, 1, 2] -> The single number should be 4
        nums = [4, 1, 2, 1, 2]
        self.assertEqual(Solution().singleNumber(nums), 4)
    
    def test_single_number_one_element(self):
        """
        Tests with a list containing only one element.
        """
        # Test case: [7] -> The single number should be 7
        nums = [7]
        self.assertEqual(Solution().singleNumber(nums), 7)


if __name__ == '__main__':
    unittest.main()