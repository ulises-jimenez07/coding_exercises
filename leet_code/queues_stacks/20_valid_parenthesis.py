class Solution(object):
    def isValid(self, s):
        """
        Determines if a string containing parentheses is valid.

        A valid string has properly nested and matching parentheses.

        Args:
            s: The string containing parentheses.

        Returns:
            True if the string is valid, False otherwise.
        """
        brackets = {"(": ")", "[": "]", "{": "}"}  # Define matching bracket pairs
        stack = []  # Use a stack to track opening brackets

        for char in s:  # Iterate through each character in the string
            if char in brackets:  # If it's an opening bracket
                stack.append(char)  # Push it onto the stack
            elif len(stack) == 0:  # If it's a closing bracket but the stack is empty
                return False  # It's unmatched, so the string is invalid
            else:  # If it's a closing bracket and the stack isn't empty
                top = stack.pop()  # Pop the last opening bracket from the stack
                if (
                    brackets[top] != char
                ):  # If it doesn't match the current closing bracket
                    return False  # The string is invalid

        return len(stack) == 0  # If the stack is empty at the end, the string is valid


# Test cases
test_cases = [
    ("()", True),  # Simple valid case
    ("()[]{}", True),  # Multiple valid bracket types
    ("(]", False),  # Mismatched brackets
    ("([)]", False),  # Incorrect nesting
    ("{[]}", True),  # Correct nesting
    ("", True),  # Empty string is valid
    ("(", False),  # Unclosed opening bracket
    ("}", False),  # Unmatched closing bracket
    ("{{{{", False),  # Multiple unclosed opening brackets
    ("}}", False),  # Multiple unmatched closing brackets
]

# Run the test cases
for input_string, expected_result in test_cases:
    result = Solution().isValid(input_string)
    print(f"Input: {input_string}, Expected: {expected_result}, Result: {result}")
    assert result == expected_result, f"Test failed for input: {input_string}"

print("All test cases passed!")
