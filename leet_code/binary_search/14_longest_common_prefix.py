from typing import List
import unittest

# Define the Solution class containing the method to find the longest common prefix
class Solution:
    """
    Finds the longest common prefix string amongst an array of strings.
    This implementation uses a binary search approach on the length of the prefix.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Handle the edge case where the list of strings is empty
        if not strs:
            return ''

        # Determine the minimum length among all strings. The LCP cannot be longer than this.
        min_len = min(len(x) for x in strs)
        # Initialize binary search boundaries: start (minimum possible LCP length, 1) and end (maximum possible, min_len)
        start, end = 1, min_len

        # Perform binary search for the length of the LCP
        while start <= end:
            # Calculate the middle length to check
            mid = (start + end) // 2
            # Check if a prefix of length 'mid' is common to all strings
            if self.is_common_prefix(strs, mid):
                # If common, try a longer prefix (shift 'start' to mid + 1)
                start = mid + 1
            else:
                # If not common, the LCP must be shorter (shift 'end' to mid - 1)
                end = mid - 1
        
        # Return the prefix of the first string up to the determined LCP length
        return strs[0][:end]

    def is_common_prefix(self, strs, l):
        """
        Helper function to check if a prefix of length 'l' of the first string 
        is a prefix of all other strings in the list.
        """
        # Get the prefix of length 'l' from the first string
        str1 = strs[0][:l]
        # Iterate through the rest of the strings (starting from the second string)
        for i in range(1,len(strs)):
            # Check if the current string starts with the determined prefix (str1)
            if not strs[i].startswith(str1):
                # If any string does not start with str1, it's not a common prefix
                return False
        # If all strings start with str1, it is a common prefix of length 'l'
        return True

# --- Unit Tests ---

class TestLongestCommonPrefix(unittest.TestCase):
    """
    Unit tests for the longestCommonPrefix method in the Solution class.
    """
    
    def test_example_one(self):
        # Standard case with a common prefix
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["flower","flow","flight"]), "fl", 
                         "Should return 'fl' for ['flower', 'flow', 'flight']")

    def test_example_two(self):
        # Case with no common prefix
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["dog","racecar","car"]), "", 
                         "Should return '' for ['dog', 'racecar', 'car']")

    def test_empty_list(self):
        # Edge case: empty list of strings
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix([]), "", 
                         "Should return '' for an empty list")

    def test_single_string(self):
        # Edge case: list with a single string
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["a"]), "a", 
                         "Should return the string itself for a single-element list")

    def test_all_same_string(self):
        # Case where all strings are identical
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["abc", "abc", "abc"]), "abc", 
                         "Should return the string itself when all are identical")

    def test_empty_strings_present(self):
        # Case where one or more strings are empty. LCP must be empty.
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["a", ""]), "", 
                         "Should return '' if an empty string is present")
        self.assertEqual(solution.longestCommonPrefix(["", "b", "c"]), "",
                         "Should return '' if an empty string is present")

    def test_no_common_prefix_one_char(self):
        # Case where common prefix is only the first character (or none)
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["apple", "apricot", "apex"]), "ap", 
                         "Should return 'ap'")

# Standard boilerplate to run the tests when the script is executed
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)