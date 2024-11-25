import unittest  # Importing the unittest module for writing test cases


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of 's' that contains all the characters in 't'.

        Args:
            s: The source string.
            t: The target string containing characters to be included in the window.

        Returns:
            The minimum window substring. If no such window exists, returns an empty string.
        """
        len1 = len(s)  # Length of the source string
        len2 = len(t)  # Length of the target string

        if len1 < len2:  # If 's' is shorter than 't', no window can contain all of 't'
            return ""

        hash_pat = {}  # Hash map to store character counts in 't'
        hash_str = {}  # Hash map to store character counts in the current window of 's'

        # Populate hash_pat with character counts from 't'
        for i in range(len2):
            char = t[i]
            hash_pat[char] = hash_pat.get(char, 0) + 1

        count = 0  # Counter for matching characters found in the current window
        left = 0  # Left pointer of the sliding window
        start_index = -1  # Starting index of the minimum window (initialized to -1)
        min_len = float("inf")  # Minimum window length (initialized to infinity)

        # Iterate through 's' with the right pointer of the sliding window
        for right in range(len1):
            char = s[right]
            hash_str[char] = (
                hash_str.get(char, 0) + 1
            )  # Update character count in the window

            # If the current character is in 't' and its count in the window is less than or equal to its count in 't',
            # increment the matching character counter.
            if char in hash_pat and hash_str[char] <= hash_pat[char]:
                count += 1

            # If all characters of 't' are present in the current window
            if count == len2:
                # Shrink the window from the left until a required character is removed
                while s[left] not in hash_pat or hash_str[s[left]] > hash_pat[s[left]]:
                    left_char = s[left]
                    if left_char in hash_pat and hash_str[left_char] > hash_pat.get(
                        left_char, 0
                    ):
                        hash_str[left_char] -= 1
                    left += 1

                # Calculate the current window length
                window_len = right - left + 1

                # Update the minimum window length and starting index if a smaller window is found
                if min_len > window_len:
                    min_len = window_len
                    start_index = left

        # If no valid window is found, return an empty string
        if start_index == -1:
            return ""

        # Return the minimum window substring
        return s[start_index : start_index + min_len]


class TestMinWindow(unittest.TestCase):
    def test_empty_s(self):
        self.assertEqual(Solution().minWindow("", "A"), "")

    def test_t_longer_than_s(self):
        self.assertEqual(Solution().minWindow("AB", "ABC"), "")

    def test_substring_at_beginning(self):
        self.assertEqual(Solution().minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_substring_at_end(self):
        self.assertEqual(Solution().minWindow("BBBBBBCCCCA", "ABC"), "BCCCCA")

    def test_no_substring_found(self):
        self.assertEqual(Solution().minWindow("ADOBECODEBAN", "ABCC"), "")

    def test_single_character_t(self):  # Added this test case for better coverage
        self.assertEqual(Solution().minWindow("ABCDE", "B"), "B")

    def test_all_characters_same(self):  # Another test case for comprehensive coverage
        self.assertEqual(Solution().minWindow("AAAAA", "A"), "A")


if __name__ == "__main__":
    unittest.main()
