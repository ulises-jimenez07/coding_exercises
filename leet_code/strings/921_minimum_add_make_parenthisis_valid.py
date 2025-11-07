import unittest


class Solution:
    """
    This class contains a method to solve the 'Minimum Add to Make Parentheses Valid' problem.
    It calculates the minimum number of parentheses (either '(' or ')') that must be added
    to an input string `s` to make it a valid parentheses string.
    A valid string has:
    1. An equal number of '(' and ')'.
    2. Every prefix has at least as many '(' as ')'.
    """

    def minAddToMakeValid(self, s: str) -> int:
        """
        Calculates the minimum number of parentheses to add to make the string valid.
        Uses a single pass and two counters: one for the current balance and one for the needed additions.

        :param s: The input string consisting only of '(' and ')'.
        :return: The minimum number of insertions required.
        """
        count = 0  # Tracks the balance of open parentheses
        ans = 0  # Stores the total number of parentheses to add

        for ch in s:
            if ch == "(":
                count += 1
            else:
                count -= 1

            # If count becomes negative, it means we have a closing parenthesis without a matching open one.
            # We need to add an opening parenthesis to make it valid.
            if count < 0:
                ans += 1
                count = 0  # Reset count as this ')' is now balanced by the added '('

        # After iterating, any remaining open parentheses need a closing parenthesis.
        ans += count

        return ans


# -----------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    """
    Unit tests for the minAddToMakeValid method.
    """

    def setUp(self):
        self.solution = Solution()

    def test_example_1_need_closing(self):
        """Test case: Open brackets need closing: "(((" -> 3"""
        s = "((("
        self.assertEqual(self.solution.minAddToMakeValid(s), 3)

    def test_example_2_need_opening(self):
        """Test case: Closing brackets need opening: ")))" -> 3"""
        s = ")))"
        self.assertEqual(self.solution.minAddToMakeValid(s), 3)

    def test_example_3_mixed_needs(self):
        """Test case: Mixed, should be 1 (add '(' at start or ')' at end)"""
        s = "(()"
        self.assertEqual(self.solution.minAddToMakeValid(s), 1)

    def test_example_4_valid_string(self):
        """Test case: Already valid string: "()" -> 0"""
        s = "()"
        self.assertEqual(self.solution.minAddToMakeValid(s), 0)

    def test_example_5_complex_case(self):
        """Test case: Complex string: "())(((" -> 4"""
        s = "())((("
        self.assertEqual(self.solution.minAddToMakeValid(s), 4)

    def test_empty_string(self):
        """Test case: Empty string: "" -> 0"""
        s = ""
        self.assertEqual(self.solution.minAddToMakeValid(s), 0)


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
