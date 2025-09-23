# The Solution class contains the logic to solve the integer replacement problem.
class Solution:
    # The main method that initiates the integer replacement process.
    def integerReplacement(self, n: int) -> int:
        # Initialize a dictionary 'dp' to store the minimum operations for each integer.
        # This is used for memoization to avoid redundant calculations.
        self.dp = {}
        # Call the helper function to find the minimum operations to reduce 'n' to 1.
        return self.min_no_op_i_to_1(n)

    # A recursive helper function to calculate the minimum number of operations to
    # transform an integer 'i' to 1.
    def min_no_op_i_to_1(self, i):
        # Base case: If the integer is 1 or less, no more operations are needed.
        if i <= 1:
            return 0
        
        # Check if the result for 'i' has already been computed and stored in the 'dp' dictionary.
        if i not in self.dp:
            # Initialize the answer for the current integer.
            ans = 0
            
            # If 'i' is even, the only valid operation is to divide by 2.
            if i % 2 == 0:
                # Add 1 for the current operation and recursively call for the result of 'i // 2'.
                ans = 1 + self.min_no_op_i_to_1(i // 2)
            # If 'i' is odd, there are two possible operations: decrement by 1 or increment by 1.
            else:
                # Add 1 for the current operation and take the minimum of the two recursive calls:
                # one for 'i - 1' and one for 'i + 1'.
                ans = 1 + min(self.min_no_op_i_to_1(i - 1), self.min_no_op_i_to_1(i + 1))
            
            # Store the computed result in the 'dp' dictionary to use for future lookups (memoization).
            self.dp[i] = ans
        
        # Return the minimum number of operations for 'i' from the 'dp' dictionary.
        return self.dp[i]

import unittest

# Define a class for the unit tests, inheriting from unittest.TestCase.
class TestSolution(unittest.TestCase):
    # This method runs before each test to set up the necessary objects.
    def setUp(self):
        # Create an instance of the Solution class.
        self.sol = Solution()

    # Test case 1: Test with an even number.
    def test_even_number(self):
        # Expected minimum operations for 8 is 3 (8 -> 4 -> 2 -> 1).
        self.assertEqual(self.sol.integerReplacement(8), 3)

    # Test case 2: Test with an odd number.
    def test_odd_number(self):
        # Expected minimum operations for 7 is 4 (7 -> 8 -> 4 -> 2 -> 1).
        self.assertEqual(self.sol.integerReplacement(7), 4)
    
    # Test case 3: Test with a small number, 1.
    def test_one(self):
        # Expected minimum operations for 1 is 0.
        self.assertEqual(self.sol.integerReplacement(1), 0)

    # Test case 4: Test with a number that results in a path through incrementation.
    def test_path_through_increment(self):
        # Expected minimum operations for 3 is 2 (3 -> 2 -> 1).
        self.assertEqual(self.sol.integerReplacement(3), 2)
    
    # Test case 5: Test with a number that results in a path through decrementation.
    def test_path_through_decrement(self):
        # Expected minimum operations for 65535 is 17.
        # (65535 -> 65536 -> 32768 -> ... -> 1)
        self.assertEqual(self.sol.integerReplacement(65535), 17)

# The entry point for running the unit tests.
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)