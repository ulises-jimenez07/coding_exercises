"""
Problem: Calculate number of unique email addresses after normalization rules

Approach:
- Normalize each email: remove dots in local, ignore after plus sign
- Use set to track unique normalized emails
- Time complexity: O(n*m) where m is average email length
- Space complexity: O(n)
"""

import unittest
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """Calculates number of unique email addresses after normalization."""

        def clean_email(email: str) -> str:
            """Normalizes a single email address."""
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")
            return local_name + "@" + domain_name

        unique_emails = set()
        for email in emails:
            unique_emails.add(clean_email(email))

        return len(unique_emails)


class TestNumUniqueEmails(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Example 1."""
        emails = [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
        self.assertEqual(self.solution.numUniqueEmails(emails), 2)

    def test_example_2(self):
        """Example 2."""
        emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 3)

    def test_empty_list(self):
        """Empty list."""
        self.assertEqual(self.solution.numUniqueEmails([]), 0)

    def test_all_same(self):
        """All same."""
        emails = ["test.email+alex@leetcode.com"] * 5
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)

    def test_no_plus_sign(self):
        """No plus sign."""
        emails = ["testemail@leetcode.com", "testemail@lee.tcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 2)

    def test_no_periods(self):
        """No periods."""
        emails = ["test+alex@leetcode.com", "test+bob@leetcode.com"]
        self.assertEqual(self.solution.numUniqueEmails(emails), 1)


if __name__ == "__main__":
    unittest.main()
