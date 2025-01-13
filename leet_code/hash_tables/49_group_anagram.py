import unittest  # Importing the unittest module for creating test cases


class Solution(object):
    def groupAnagrams(self, strs):
        """
        Groups anagrams together from a list of strings.

        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = (
            {}
        )  # Initialize a dictionary to store sorted strings as keys and their anagrams as values
        for s in strs:  # Iterate through each string in the input list
            array = list(s)  # Convert the string to a list of characters
            array.sort()  # Sort the list of characters alphabetically
            sorted_s = "".join(array)  # Join the sorted characters back into a string
            if (
                sorted_s not in map
            ):  # Check if the sorted string is already a key in the dictionary
                map[sorted_s] = (
                    []
                )  # Create a new list for this sorted string if it's not already a key
            map[sorted_s].append(
                s
            )  # Add the original string to the list associated with its sorted version
        return list(
            map.values()
        )  # Return a list of lists, where each inner list contains anagrams


# Test cases using the unittest module
class TestGroupAnagrams(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(
            Solution().groupAnagrams([]), []
        )  # Empty input should return an empty list

    def test_single_word(self):
        self.assertEqual(
            Solution().groupAnagrams(["bat"]), [["bat"]]
        )  # Single word should be in its own group

    def test_example_case(self):
        self.assertEqual(
            Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        )  # Example case from the problem description

    def test_empty_string(self):
        self.assertEqual(
            Solution().groupAnagrams([""]), [[""]]
        )  # Handles empty strings

    def test_case_sensitive(self):
        # The function sorts lowercase and uppercase separately
        self.assertEqual(
            Solution().groupAnagrams(["Tea", "tea"]), [["Tea"], ["tea"]]
        )  # Case sensitive

    def test_different_length_words(self):  # Test with words of varying lengths
        self.assertEqual(
            Solution().groupAnagrams(["a", "ab", "ba"]), [["a"], ["ab", "ba"]]
        )


if __name__ == "__main__":
    unittest.main()
