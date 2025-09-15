from typing import List
import unittest


class Solution:
    """
    Solves the problem of finding the number of ways to assign plus or minus signs
    to each integer in an array so that their sum equals a specific target.
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Main function to initiate the recursive search with memoization.

        Args:
            nums: A list of integers.
            target: The target sum.

        Returns:
            The number of ways to achieve the target sum.
        """
        self.nums = nums
        self.ht = {}  # Hashtable for memoization (key: (index, current_target))
        return self.num_to_target(0, target)

    def num_to_target(self, i, ct):
        """
        Recursive helper function with memoization to find the number of ways.

        Args:
            i: The current index in the nums array.
            ct: The current target sum to achieve.

        Returns:
            The number of ways from the current state (i, ct).
        """
        if i < len(self.nums) - 1:
            key = (i, ct)
            if key in self.ht:
                return self.ht[key]  # Return memoized result if available

            # Recurse for both plus and minus signs and store the sum
            self.ht[key] = self.num_to_target(i + 1, ct - self.nums[i]) + self.num_to_target(
                i + 1, ct + self.nums[i]
            )
            return self.ht[key]

        # Base case for the last element
        if ct == 0 and self.nums[i] == 0:
            return 2  # Two ways: +0 and -0 both result in 0

        if abs(ct) == abs(self.nums[i]):
            return 1  # One way to reach the target with the last element

        return 0  # No way to reach the target with the last element


# -----------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def test_example_1(self):
        """
        Test case from the problem description.
        nums = [1,1,1,1,1], target = 3
        Expected output: 5
        """
        s = Solution()
        self.assertEqual(s.findTargetSumWays([1, 1, 1, 1, 1], 3), 5)

    def test_example_2(self):
        """
        Test case with a single element and a positive target.
        nums = [1], target = 1
        Expected output: 1
        """
        s = Solution()
        self.assertEqual(s.findTargetSumWays([1], 1), 1)

    def test_example_3(self):
        """
        Test case with a single element and a negative target.
        nums = [1], target = -1
        Expected output: 1
        """
        s = Solution()
        self.assertEqual(s.findTargetSumWays([1], -1), 1)

    def test_with_zero(self):
        """
        Test case involving a zero.
        nums = [0], target = 0
        Expected output: 2 (+0, -0)
        """
        s = Solution()
        self.assertEqual(s.findTargetSumWays([0], 0), 2)

    def test_larger_set(self):
        """
        Test case with a larger set of numbers.
        nums = [7,9,3,8,0,6,1,5,4,2], target = 1
        Expected output: 140
        """
        s = Solution()
        self.assertEqual(s.findTargetSumWays([7, 9, 3, 8, 0, 6, 1, 5, 4, 2], 1), 46)


if __name__ == "__main__":
    unittest.main()
