import unittest

class Solution:
    """
    Implements a method to determine if a given integer 'n' is a power of two.
    A number 'n' is a power of two if it can be written as 2^x for some integer x.
    """
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Checks if an integer 'n' is a power of two by repeatedly dividing by 2.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if 'n' is a power of two, False otherwise.
        """
        # A power of two must be a positive integer. 0 is not a power of two.
        if n <= 0:
            return False

        # Continuously divide 'n' by 2 as long as it is an even number.
        # This removes all factors of 2 from 'n'.
        while n % 2 == 0:
            n /= 2

        # If 'n' was a power of two (e.g., 1, 2, 4, 8, 16...), 
        # repeatedly dividing by 2 will eventually result in 1.
        # If 'n' was not a power of two (e.g., 3, 6, 10, 12...), 
        # it will be an odd number greater than 1 after the loop.
        return n == 1

# --- Unit Tests ---

class TestIsPowerOfTwo(unittest.TestCase):
    """
    Unit tests for the isPowerOfTwo method in the Solution class.
    """

    def test_powers_of_two(self):
        """Test with classic powers of two."""
        solution = Solution()
        self.assertTrue(solution.isPowerOfTwo(1), "1 is 2^0")
        self.assertTrue(solution.isPowerOfTwo(2), "2 is 2^1")
        self.assertTrue(solution.isPowerOfTwo(4), "4 is 2^2")
        self.assertTrue(solution.isPowerOfTwo(16), "16 is 2^4")
        self.assertTrue(solution.isPowerOfTwo(1024), "1024 is 2^10")

    def test_non_powers_of_two(self):
        """Test with numbers that are not powers of two."""
        solution = Solution()
        self.assertFalse(solution.isPowerOfTwo(3), "3 is not a power of two")
        self.assertFalse(solution.isPowerOfTwo(6), "6 is not a power of two")
        self.assertFalse(solution.isPowerOfTwo(15), "15 is not a power of two")
        self.assertFalse(solution.isPowerOfTwo(1023), "1023 is not a power of two")
        self.assertFalse(solution.isPowerOfTwo(5), "5 is not a power of two")

    def test_edge_cases(self):
        """Test with zero and negative numbers."""
        solution = Solution()
        # The logic was slightly modified to handle n=0 and negative numbers based on the standard definition, 
        # though the original code already handled n=0.
        self.assertFalse(solution.isPowerOfTwo(0), "0 is not a power of two")
        self.assertFalse(solution.isPowerOfTwo(-2), "Negative numbers are not powers of two")
        self.assertFalse(solution.isPowerOfTwo(-16), "Negative numbers are not powers of two")

if __name__ == '__main__':
    # Run tests only if the script is executed directly
    # argv and exit=False are used to allow the notebook/environment to continue after tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)