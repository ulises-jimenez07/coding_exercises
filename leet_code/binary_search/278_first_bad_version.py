"""
Problem: Find the first bad version in a sequence of versions

Approach:
- Binary search to minimize API calls
- Narrow search range based on isBadVersion result
- Time complexity: O(log n)
- Space complexity: O(1)
"""

import unittest

# Mock isBadVersion for local testing
_bad_version_global = 0


def isBadVersion(version: int) -> bool:
    return version >= _bad_version_global


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = (right + left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


class TestFirstBadVersion(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_version_is_bad(self):
        global _bad_version_global
        _bad_version_global = 1
        self.assertEqual(self.solution.firstBadVersion(5), 1)

    def test_last_version_is_bad(self):
        global _bad_version_global
        _bad_version_global = 5
        self.assertEqual(self.solution.firstBadVersion(5), 5)

    def test_middle_version_is_bad(self):
        global _bad_version_global
        _bad_version_global = 3
        self.assertEqual(self.solution.firstBadVersion(5), 3)

    def test_single_version_is_bad(self):
        global _bad_version_global
        _bad_version_global = 1
        self.assertEqual(self.solution.firstBadVersion(1), 1)

    def test_no_bad_versions_in_range(self):
        global _bad_version_global
        _bad_version_global = 6  # Bad version is outside the tested range
        self.assertEqual(self.solution.firstBadVersion(5), 5)  # Should return n if no bad version found up to n


if __name__ == "__main__":
    unittest.main()
