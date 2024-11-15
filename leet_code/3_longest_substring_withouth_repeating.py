class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Finds the length of the longest substring without repeating characters.

        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)  # Handle empty or single-character strings

        seen = {}  # Dictionary to store the last seen index of each character
        max_length = 0  # Initialize the maximum length
        left = right = 0  # Initialize left and right pointers of the sliding window

        for i in range(len(s)):  # Iterate through the string
            if s[i] in seen:  # Check if the character is already in 'seen'
                # Move the left pointer to the right of the previous occurrence of the character
                left = max(left, seen[s[i]] + 1)

            right += 1  # Expand the window by moving the right pointer
            seen[s[i]] = i  # Update the last seen index of the current character
            max_length = max(
                right - left, max_length
            )  # Update max_length if the current window is longer

        return max_length


# Test cases
solution = Solution()

# Test case 1: Basic example
s1 = "abcabcbb"
expected1 = 3
result1 = solution.lengthOfLongestSubstring(s1)
print(f"Test case 1: Expected {expected1}, got {result1}")
assert result1 == expected1

# Test case 2: Repeating characters
s2 = "bbbbb"
expected2 = 1
result2 = solution.lengthOfLongestSubstring(s2)
print(f"Test case 2: Expected {expected2}, got {result2}")
assert result2 == expected2

# Test case 3: No repeating characters
s3 = "pwwkew"
expected3 = 3
result3 = solution.lengthOfLongestSubstring(s3)
print(f"Test case 3: Expected {expected3}, got {result3}")
assert result3 == expected3

# Test case 4: Empty string
s4 = ""
expected4 = 0
result4 = solution.lengthOfLongestSubstring(s4)
print(f"Test case 4: Expected {expected4}, got {result4}")
assert result4 == expected4

# Test case 5: Single character string
s5 = "a"
expected5 = 1
result5 = solution.lengthOfLongestSubstring(s5)
print(f"Test case 5: Expected {expected5}, got {result5}")
assert result5 == expected5

# Test case 6: All unique characters
s6 = "abcdefg"
expected6 = 7
result6 = solution.lengthOfLongestSubstring(s6)
print(f"Test case 6: Expected {expected6}, got {result6}")
assert result6 == expected6
