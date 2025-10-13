class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Calculates the number of set bits (1s) in the binary representation of an integer.
        
        This is also known as the Hamming weight or population count.
        
        Args:
            n: A non-negative integer.
            
        Returns:
            The number of set bits in the integer's binary representation.
        """
        count = 0
        # Iterate through each of the 32 bits of the integer.
        for i in range(0, 32):
            # Check if the i-th bit is set (1) using a bitwise AND operation.
            # (1 << i) creates a bitmask with a single 1 at the i-th position.
            if n & (1 << i) != 0:
                # If the bit is set, increment the count.
                count += 1

        return count

import unittest

class TestSolution(unittest.TestCase):
    def test_hammingWeight(self):
        # Test case 1: A positive integer with a known number of set bits.
        self.assertEqual(Solution().hammingWeight(11), 3)  # Binary of 11 is 1011

        # Test case 2: A power of two (should have only one set bit).
        self.assertEqual(Solution().hammingWeight(8), 1)   # Binary of 8 is 1000

        # Test case 3: Zero (should have zero set bits).
        self.assertEqual(Solution().hammingWeight(0), 0)

        # Test case 4: A large number with multiple set bits.
        self.assertEqual(Solution().hammingWeight(128), 1) # Binary of 128 is 10000000

        # Test case 5: A number with all bits set (for a 32-bit integer, this would be -1).
        # We'll use a positive number to stay within the non-negative assumption.
        self.assertEqual(Solution().hammingWeight(4294967295), 32) # Binary of 4294967295 is all 1s (2^32 - 1)

if __name__ == '__main__':
    unittest.main()