import unittest
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        Calculates the number of unique email addresses after applying normalization rules.

        Normalization rules:
        1. Ignore periods ('.') before the plus sign ('+') in the local name.
        2. Ignore everything after the plus sign ('+') in the local name.
        3. The domain name is unchanged.

        Args:
            emails: A list of email addresses.

        Returns:
            The number of unique email addresses after normalization.
        """

        def clean_email(email: str) -> str:
            """
            Normalizes a single email address.

            Args:
                email: The email address to normalize.

            Returns:
                The normalized email address.
            """
            local_name, domain_name = email.split(
                "@"
            )  # Split into local and domain parts
            local_name = local_name.split("+")[0]  # Ignore everything after '+'
            local_name = local_name.replace(".", "")  # Remove periods

            return local_name + "@" + domain_name  # Combine and return

        unique_emails = set()  # Use a set for efficient uniqueness check
        for email in emails:
            unique_emails.add(clean_email(email))

        return len(unique_emails)


class TestNumUniqueEmails(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        emails = [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
        expected = 2
        self.assertEqual(self.solution.numUniqueEmails(emails), expected)

    def test_example_2(self):
        emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
        expected = 3
        self.assertEqual(self.solution.numUniqueEmails(emails), expected)

    def test_empty_list(self):
        emails = []
        expected = 0
        self.assertEqual(self.solution.numUniqueEmails(emails), expected)

    def test_all_same(self):
        emails = ["test.email+alex@leetcode.com"] * 5
        expected = 1
        self.assertEqual(self.solution.numUniqueEmails(emails), expected)

    def test_no_plus_sign(self):
        emails = ["testemail@leetcode.com", "testemail@lee.tcode.com"]
        expected = 2
        self.assertEqual(self.solution.numUniqueEmails(emails), expected)

    def test_no_periods(self):
        emails = ["test+alex@leetcode.com", "test+bob@leetcode.com"]
        expected = 1  # after cleaning 'test@leetcode.com'
        self.assertEqual(self.solution.numUniqueEmails(emails), expected)


if __name__ == "__main__":
    unittest.main()
