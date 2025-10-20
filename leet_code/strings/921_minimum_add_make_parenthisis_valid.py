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
        # count: Tracks the current balance of open parentheses.
        # It increases for '(' and decreases for ')'.
        count = 0
        
        # ans: Stores the total number of parentheses that need to be added.
        ans = 0
        
        # Iterate through the string character by character
        for ch in s:
            if ch == '(':
                # Encountered an opening parenthesis, increase the balance.
                count += 1
            else:
                # Encountered a closing parenthesis, decrease the balance.
                count -= 1

            # Check for invalid state: more closing parentheses than open ones encountered so far.
            if count < 0:
                # A closing parenthesis (i.e., ')' ) was found without a matching open one.
                # To fix this, we must add an opening parenthesis '(' before this ')' position.
                ans += 1
                # The balance is then reset to 0, because the newly added '(' fixes the imbalance
                # caused by the current ')', effectively pairing them up.
                count += 1

        # After the loop, 'count' holds the number of unmatched open parentheses.
        # Each of these must be closed by adding a ')' to the end of the string.
        ans += count
        
        # 'ans' now holds the total number of additions (both '(' and ')') needed.
        return ans

# -----------------------------------------------------------------------------

class TestSolution(unittest.TestCase):
    """
    Unit tests for the minAddToMakeValid method.
    """

    def test_example_1_need_closing(self):
        """Test case: Open brackets need closing: "(((" -> 3"""
        s = "((("
        self.assertEqual(Solution().minAddToMakeValid(s), 3)

    def test_example_2_need_opening(self):
        """Test case: Closing brackets need opening: ")))" -> 3"""
        s = ")))"
        self.assertEqual(Solution().minAddToMakeValid(s), 3)

    def test_example_3_mixed_needs(self):
        """Test case: Mixed, should be 1 (add '(' at start or ')' at end)"""
        s = "(()"
        # Balance trace:
        # ( : count=1
        # ( : count=2
        # ) : count=1
        # Final count=1. Result = ans(0) + count(1) = 1.
        self.assertEqual(Solution().minAddToMakeValid(s), 1)

    def test_example_4_valid_string(self):
        """Test case: Already valid string: "()" -> 0"""
        s = "()"
        self.assertEqual(Solution().minAddToMakeValid(s), 0)
        
    def test_example_5_complex_case(self):
        """Test case: Complex string: "())(((" -> 3 (needs '(', then ')' then ')', or similar)"""
        s = "())((("
        # Balance trace:
        # ( : count=1
        # ) : count=0
        # ) : count=-1. ans=1, count=0 (fixed)
        # ( : count=1
        # ( : count=2
        # ( : count=3
        # Final: ans(1) + count(3) = 4.
        # Wait, the example "())(((" needs 3 additions: "(()))((())" (5 total) 
        # or "(()))((())" (5 total)
        # The correct result for "())(((" is 4:  ())(())(() 
        # The function logic is correct. Let's trace it:
        # '(': count=1
        # ')': count=0
        # ')': count=-1. Fix: ans=1, count=0
        # '(': count=1
        # '(': count=2
        # '(': count=3
        # Final: ans=1, count=3. Result = 1 + 3 = 4.
        self.assertEqual(Solution().minAddToMakeValid(s), 4)

    def test_empty_string(self):
        """Test case: Empty string: "" -> 0"""
        s = ""
        self.assertEqual(Solution().minAddToMakeValid(s), 0)

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    # Boilerplate code to run the tests when the script is executed
    unittest.main(argv=['first-arg-is-ignored'], exit=False)