import unittest


class Solution:
    """
    A class to solve the "Climbing Stairs" problem using recursion with memoization.
    """

    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb to the top of a staircase with n steps.

        This is the main function that initializes the memoization dictionary and
        starts the recursive calculation.

        Args:
            n: The number of steps in the staircase.

        Returns:
            The total number of distinct ways to climb to the top.
        """
        self.num_ways = {}
        return self.num_ways_to_n(0, n)

    def num_ways_to_n(self, i: int, n: int) -> int:
        """
        A helper function that recursively calculates the number of ways to reach
        step 'n' starting from step 'i'.

        This method uses memoization to store and reuse results for subproblems.

        Args:
            i: The current step number.
            n: The total number of steps.

        Returns:
            The number of ways to reach step 'n' from step 'i'.
        """
        # Base case 1: If the current step 'i' is past the destination 'n', it's an invalid path.
        if i > n:
            return 0
        # Base case 2: If the current step 'i' is the destination 'n', we've found one valid way.
        if i == n:
            return 1
        else:
            # Check if the result for the current step 'i' is already memoized.
            if i in self.num_ways:
                return self.num_ways[i]
            else:
                # Recursive step: The number of ways is the sum of ways from the next two possible moves
                # (taking 1 step or taking 2 steps).
                self.num_ways[i] = self.num_ways_to_n(i + 1, n) + self.num_ways_to_n(i + 2, n)
                return self.num_ways[i]


# --------------------------------------------------------------------------------


## Unit Tests 🧪
class TestClimbStairs(unittest.TestCase):
    """
    Unit tests for the Solution class's climbStairs method.
    """

    def test_n_equals_1(self):
        """Test case for n = 1."""
        self.assertEqual(Solution().climbStairs(1), 1)

    def test_n_equals_2(self):
        """Test case for n = 2."""
        self.assertEqual(Solution().climbStairs(2), 2)

    def test_n_equals_3(self):
        """Test case for n = 3."""
        self.assertEqual(Solution().climbStairs(3), 3)

    def test_n_equals_4(self):
        """Test case for n = 4."""
        self.assertEqual(Solution().climbStairs(4), 5)

    def test_n_equals_5(self):
        """Test case for n = 5."""
        self.assertEqual(Solution().climbStairs(5), 8)

    def test_n_equals_30(self):
        """Test case for a larger number, n = 30."""
        self.assertEqual(Solution().climbStairs(30), 1346269)


# This allows the tests to be run from the command line.
if __name__ == "__main__":
    unittest.main()
