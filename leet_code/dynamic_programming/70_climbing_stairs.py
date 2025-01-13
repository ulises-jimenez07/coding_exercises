import unittest


class Solution(object):
    def climbStairs(self, n):
        """
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

        :type n: int
        :rtype: int
        """
        # Base cases:
        # If n is 1, there's only 1 way (1 step)
        if n == 1:
            return 1
        # If n is 2, there are 2 ways (1+1 or 2)
        if n == 2:
            return 2

        # Initialize variables to store number of ways for previous two steps
        one_step_before = 2  # Ways to reach (n-1)th step
        two_steps_before = 1  # Ways to reach (n-2)th step

        # Iterate from 3 to n, calculating ways to reach current step
        for _ in range(3, n + 1):
            # Number of ways to reach current step is sum of ways to reach previous two steps.
            current = one_step_before + two_steps_before
            # Update previous step counts for next iteration
            two_steps_before = one_step_before
            one_step_before = current

        # Return the number of ways to reach the nth step.
        return one_step_before


class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_one_step(self):
        self.assertEqual(self.solution.climbStairs(1), 1)

    def test_two_steps(self):
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_three_steps(self):
        self.assertEqual(self.solution.climbStairs(3), 3)

    def test_four_steps(self):
        self.assertEqual(self.solution.climbStairs(4), 5)

    def test_five_steps(self):
        self.assertEqual(self.solution.climbStairs(5), 8)

    def test_large_number_of_steps(self):  # Test a larger input
        self.assertEqual(self.solution.climbStairs(10), 89)


if __name__ == "__main__":
    unittest.main()
