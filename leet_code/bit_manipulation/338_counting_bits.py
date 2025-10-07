from typing import List
import unittest

class Solution:
    """
    This class provides a solution to the "Counting Bits" problem.
    The goal is to calculate the number of set bits (1s in binary representation) for each integer from 0 to n.
    """
    def countBits(self, n: int) -> List[int]:
        """
        Calculates the number of set bits for each integer from 0 to n.

        Args:
            n: The upper limit of the range (inclusive).

        Returns:
            A list where the i-th element is the number of set bits in the integer i.
        """
        # Uses a list comprehension to iterate from 0 to n and calculate the number of set bits for each number.
        return [self.get_no_of_set_bits(num) for num in range(n + 1)]

    def get_no_of_set_bits(self, num: int) -> int:
        """
        Counts the number of set bits (1s) in the binary representation of a given integer.

        Args:
            num: The integer to analyze.

        Returns:
            The number of set bits in the integer.
        """
        count = 0
        # Iterates through each bit position from 0 to 31 (for a 32-bit integer).
        for i in range(32):
            # Performs a bitwise AND operation between the number and a bitmask (1 shifted left by i).
            # If the result is greater than 0, it means the i-th bit is set.
            if (num & (1 << i)) > 0:
                count += 1
        return count

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """
    def setUp(self):
        """
        Set up the test case by creating an instance of the Solution class.
        This method is called before each test function.
        """
        self.solution = Solution()

    def test_count_bits_zero(self):
        """
        Tests the countBits method with n=0.
        """
        self.assertEqual(self.solution.countBits(0), [0])

    def test_count_bits_one(self):
        """
        Tests the countBits method with n=1.
        """
        self.assertEqual(self.solution.countBits(1), [0, 1])

    def test_count_bits_two(self):
        """
        Tests the countBits method with n=2.
        """
        self.assertEqual(self.solution.countBits(2), [0, 1, 1])

    def test_count_bits_five(self):
        """
        Tests the countBits method with n=5.
        """
        self.assertEqual(self.solution.countBits(5), [0, 1, 1, 2, 1, 2])

    def test_get_no_of_set_bits_zero(self):
        """
        Tests the get_no_of_set_bits method with num=0.
        """
        self.assertEqual(self.solution.get_no_of_set_bits(0), 0)

    def test_get_no_of_set_bits_one(self):
        """
        Tests the get_no_of_set_bits method with num=1.
        """
        self.assertEqual(self.solution.get_no_of_set_bits(1), 1)

    def test_get_no_of_set_bits_seven(self):
        """
        Tests the get_no_of_set_bits method with num=7 (binary 111).
        """
        self.assertEqual(self.solution.get_no_of_set_bits(7), 3)

    def test_get_no_of_set_bits_sixteen(self):
        """
        Tests the get_no_of_set_bits method with num=16 (binary 10000).
        """
        self.assertEqual(self.solution.get_no_of_set_bits(16), 1)

if __name__ == '__main__':
    unittest.main()