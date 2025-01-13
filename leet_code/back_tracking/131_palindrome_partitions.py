class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        Finds all possible palindrome partitioning of a given string.

        Args:
            s: The input string.

        Returns:
            A list of lists of strings, where each inner list represents a valid partitioning of 's' into palindromes.
        """
        ans = []
        self.solution(s, [], ans)  # Call the recursive helper function
        return ans

    def solution(self, s, curr_arr, ans):
        """
        Recursive helper function to generate palindrome partitions.

        Args:
            s: The remaining substring to be partitioned.
            curr_arr: The current partition being built.
            ans: The list to store all valid partitions.
        """
        if (
            len(s) == 0
        ):  # Base case: If the input string is empty, a valid partition is found
            ans.append(
                curr_arr[:]
            )  # Append a copy of the current partition to the result
            return

        for i in range(1, len(s) + 1):  # Iterate through all possible prefixes of 's'
            curr_str = s[0:i]  # Extract the prefix
            if self.is_palindrome(curr_str):  # Check if the prefix is a palindrome
                curr_arr.append(
                    curr_str
                )  # If it's a palindrome, add it to the current partition
                self.solution(
                    s[i:], curr_arr, ans
                )  # Recursively call the function with the remaining substring
                curr_arr.pop()  # Backtrack: Remove the last added prefix to explore other possibilities

    def is_palindrome(self, s):
        """
        Checks if a string is a palindrome.

        Args:
            s: The string to check.

        Returns:
            True if the string is a palindrome, False otherwise.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
        return True


# Test cases
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("nitin", [["n", "i", "t", "i", "n"], ["n", "iti", "n"], ["nitin"]]),
        ("ab", [["a", "b"]]),
        ("", [[]]),
    ]

    for input_str, expected_output in test_cases:
        actual_output = sol.partition(input_str)
        # For easier comparison, sort the inner lists of both actual and expected output
        sorted_actual_output = sorted(
            [sorted(partition) for partition in actual_output]
        )
        sorted_expected_output = sorted(
            [sorted(partition) for partition in expected_output]
        )

        assert (
            sorted_actual_output == sorted_expected_output
        ), f"For input '{input_str}', expected {expected_output} but got {actual_output}"
        print(f"Test case for '{input_str}' passed.")
