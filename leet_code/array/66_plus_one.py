from typing import List
import unittest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments the large integer represented as a list of digits by one.

        Args:
            digits: A list of integers representing a non-negative integer.
                   Each element in the list is a digit in the range [0, 9].

        Returns:
            A list of integers representing the incremented integer.
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i], carry = (digits[i] + carry) % 10, (digits[i] + carry) // 10
            if carry == 0:
                break
        if carry:
            digits.insert(0, carry)
        return digits

    def plusOne_2(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = (digits[n - 1] + 1) // 10
        digits[n - 1] = (digits[n - 1] + 1) % 10
        j = 2
        while carry > 0 and j <= n:
            new_value = (digits[n - j] + carry) % 10
            carry = (digits[n - j] + carry) // 10
            digits[n - j] = new_value
            j += 1
            print(digits)
        if carry > 0:
            return [carry] + digits
        return digits


class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_digit(self):
        self.assertEqual(self.solution.plusOne([0]), [1])
        self.assertEqual(self.solution.plusOne([5]), [6])
        self.assertEqual(self.solution.plusOne([9]), [1, 0])

    def test_multiple_digits_no_carry(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_multiple_digits_with_carry(self):
        self.assertEqual(self.solution.plusOne([1, 9, 9]), [2, 0, 0])
        self.assertEqual(self.solution.plusOne([9, 9, 9]), [1, 0, 0, 0])
        self.assertEqual(self.solution.plusOne([9, 8, 9]), [9, 9, 0])

    def test_leading_zeros(
        self,
    ):  # Though the problem states non-negative integers, it's good practice to handle edge cases.
        self.assertEqual(self.solution.plusOne([0, 0, 1]), [0, 0, 2])


if __name__ == "__main__":
    unittest.main()
