"""
Problem: Group strings that are anagrams of each other

Approach:
- Sort each string and use as hash key
- Group strings with same sorted form together
- Return grouped anagram lists
- Time complexity: O(n * k log k) where k is max string length
- Space complexity: O(n * k)
"""

import unittest


class Solution:
    def groupAnagrams(self, strs):
        map = {}
        for s in strs:
            # Use sorted string as key
            array = list(s)
            array.sort()
            sorted_s = "".join(array)
            if sorted_s not in map:
                map[sorted_s] = []
            map[sorted_s].append(s)
        return list(map.values())


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.groupAnagrams([]), [])

    def test_single_word(self):
        self.assertEqual(self.solution.groupAnagrams(["bat"]), [["bat"]])

    def test_example_case(self):
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        result = self.solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        # Sort inner lists for consistent comparison
        for sublist in result:
            sublist.sort()
        for sublist in expected:
            sublist.sort()
        self.assertCountEqual(result, expected)

    def test_empty_string(self):
        self.assertEqual(self.solution.groupAnagrams([""]), [[""]])

    def test_case_sensitive(self):
        self.assertEqual(self.solution.groupAnagrams(["Tea", "tea"]), [["Tea"], ["tea"]])

    def test_different_length_words(self):
        expected = [["a"], ["ab", "ba"]]
        result = self.solution.groupAnagrams(["a", "ab", "ba"])
        for sublist in result:
            sublist.sort()
        for sublist in expected:
            sublist.sort()
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
