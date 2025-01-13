class Solution(object):
    def letterCombinations(self, digits):
        """
        Generates all possible letter combinations that the given digits on a phone keypad could represent.

        Args:
            digits: A string representing the digits pressed on the phone keypad.

        Returns:
            A list of strings, where each string is a possible letter combination.
            Returns an empty list if the input is empty.
        """

        if len(digits) == 0:
            return []

        # Mapping of digits to letters on a phone keypad.
        digits_to_string = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []  # Initialize the list to store the combinations.

        # Start the backtracking process.
        self.back_tracking(digits, digits_to_string, "", ans, 0)
        return ans

    def back_tracking(self, digits, digits_to_string, curr, ans, digit_index):
        """
        Recursive backtracking helper function to generate letter combinations.

        Args:
            digits: The input digits string.
            digits_to_string: The mapping of digits to letters.
            curr: The current combination being built.
            ans: The list to store the complete combinations.
            digit_index: The index of the current digit being processed.
        """

        # Base case: If the length of the current combination equals the length of the input digits,
        # it means a valid combination is formed. Add it to the answer list and return.
        if len(curr) == len(digits):
            ans.append(curr)
            return

        # Get the current digit and its corresponding letters.
        current_digit = digits[digit_index]
        current_string = digits_to_string[current_digit]

        # Iterate through the letters corresponding to the current digit.
        for char in current_string:  # Simplified loop
            # Recursively call back_tracking to explore combinations with the current character.
            self.back_tracking(
                digits, digits_to_string, curr + char, ans, digit_index + 1
            )


# Test cases
solution = Solution()
print(
    solution.letterCombinations("23")
)  # Expected Output: ['ad','ae','af','bd','be','bf','cd','ce','cf']
print(solution.letterCombinations(""))  # Expected Output: []
print(solution.letterCombinations("2"))  # Expected Output: ['a','b','c']
print(
    solution.letterCombinations("79")
)  # Expected Output: ['wp', 'wq', 'wr', 'ws', 'xp', 'xq', 'xr', 'xs', 'yp', 'yq', 'yr', 'ys', 'zp', 'zq', 'zr', 'zs']
