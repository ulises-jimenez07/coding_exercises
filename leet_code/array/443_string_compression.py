"""
Problem: Compress an array of characters in-place.
The compressed string should be stored in the input character array chars.

Approach:
- Use two pointers: `read` to iterate through the array and `write` to track where to store results.
- Staged Traversal:
    1. Find the end of the current group of identical characters to determine the count.
    2. Write the character at the `write` position.
    3. If count > 1, convert the count to string and write each digit.
- Time complexity: O(n) where n is the length of the array.
- Space complexity: O(1) as we modify the array in-place.
"""

import unittest
from typing import List


class Solution:
    """Provides methods to compress character arrays in-place."""

    def compress(self, chars: List[str]) -> int:
        """Compresses the characters in the array and returns the new length."""
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            char = chars[read]
            count = 0

            # Stage 1: Find the group boundary and calculate count
            while read < n and chars[read] == char:
                read += 1
                count += 1

            # Stage 2: Write the character
            chars[write] = char
            write += 1

            # Stage 3: Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


class TestStringCompression(unittest.TestCase):
    """Unit tests for the String Compression solution."""

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Standard compression case."""
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        new_length = self.solution.compress(chars)
        self.assertEqual(chars[:new_length], ["a", "2", "b", "2", "c", "3"])
        self.assertEqual(new_length, 6)

    def test_example_2(self):
        """Single character case."""
        chars = ["a"]
        new_length = self.solution.compress(chars)
        self.assertEqual(chars[:new_length], ["a"])
        self.assertEqual(new_length, 1)

    def test_example_3(self):
        """Multi-digit count case."""
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        new_length = self.solution.compress(chars)
        self.assertEqual(chars[:new_length], ["a", "b", "1", "2"])
        self.assertEqual(new_length, 4)

    def test_no_groups(self):
        """No characters repeat."""
        chars = ["a", "b", "c"]
        new_length = self.solution.compress(chars)
        self.assertEqual(chars[:new_length], ["a", "b", "c"])
        self.assertEqual(new_length, 3)

    def test_all_same(self):
        """All characters are the same."""
        chars = ["a", "a", "a"]
        new_length = self.solution.compress(chars)
        self.assertEqual(chars[:new_length], ["a", "3"])
        self.assertEqual(new_length, 2)


if __name__ == "__main__":
    unittest.main()
