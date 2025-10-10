from typing import List
import unittest

class Solution:
    """
    Finds the missing number in an array of distinct numbers from 0 to n.
    """
    def missingNumber(self, nums: List[int]) -> int:
        """
        Calculates the missing number using the XOR bitwise operation.

        The XOR operation is a bitwise operation that returns 1 if the bits are
        different and 0 if they are the same. A key property of XOR is that
        x ^ x = 0 and x ^ 0 = x.

        The algorithm works by XORing all numbers from 0 to n (where n is the
        length of the array) into a variable 'x'. Then, it XORs all the numbers
        in the input array 'nums' into a variable 'y'. The missing number is
        the result of XORing 'x' and 'y'. This is because all numbers that are
        present in both the full range and the input array will cancel each
        other out (x ^ x = 0), leaving only the number that is missing from
        the input array.

        Args:
            nums: A list of distinct integers from 0 to n, with one number missing.

        Returns:
            The single missing number.
        """
        # Calculate the XOR sum of all numbers from 0 to n (inclusive),
        # where n is the length of the input array.
        x = 0
        for i in range(len(nums) + 1):
            x = x ^ i

        # Calculate the XOR sum of all numbers present in the input array.
        y = 0
        for num in nums:
            y = y ^ num

        # The missing number is the XOR of the two sums. This is because
        # all numbers present in both sets cancel each other out.
        return x ^ y

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def test_missingNumber_1(self):
        """
        Test case with a small array where the missing number is in the middle.
        Input: [3, 0, 1]
        Expected Output: 2
        """
        solution = Solution()
        self.assertEqual(solution.missingNumber([3, 0, 1]), 2)

    def test_missingNumber_2(self):
        """
        Test case with the missing number at the end of the range.
        Input: [0, 1]
        Expected Output: 2
        """
        solution = Solution()
        self.assertEqual(solution.missingNumber([0, 1]), 2)

    def test_missingNumber_3(self):
        """
        Test case with a larger array and the missing number at the beginning.
        Input: [9, 6, 4, 2, 3, 5, 7, 0, 1]
        Expected Output: 8
        """
        solution = Solution()
        self.assertEqual(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_missingNumber_empty(self):
        """
        Test case with an empty array.
        Input: []
        Expected Output: 0
        """
        solution = Solution()
        self.assertEqual(solution.missingNumber([]), 0)

# Run the tests
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)