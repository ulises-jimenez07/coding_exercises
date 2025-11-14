"""
Problem: Count Total Reports in an Organization Hierarchy

Given the structure of an organization as a list of employee-manager relationships,
compute the total number of direct and indirect subordinates for every manager.

Approach:
- Build an adjacency list where manager -> list of direct reports
- Use DFS with memoization to count total reports recursively
- For each manager, total reports = direct reports + all their subordinates
- Time complexity: O(n) where n is the number of employees
- Space complexity: O(n) for adjacency list and memoization
"""

import collections
import unittest


class OrganizationAnalyzer:
    """
    A class to analyze an organization hierarchy and count total reports for each manager.
    """

    def __init__(self, reports_to_list, employees):
        # Build an adjacency list mapping each manager to their direct reports
        self.adjacency_list = collections.defaultdict(list)
        for employee, manager in reports_to_list:
            self.adjacency_list[manager].append(employee)

        # Initialize memoization cache and track all employees
        self.memo = {}
        self.all_employees = set(employees)
        self.managers = set(self.adjacency_list.keys())

    def count_reports(self, manager_id: str) -> int:
        """
        Recursively calculates the total number of reports for a given manager.

        Args:
            manager_id: The ID of the manager to count reports for.

        Returns:
            The total count of direct and indirect reports.
        """
        # Return cached result if we've already computed this
        if manager_id in self.memo:
            return self.memo[manager_id]

        # Base case: if this person isn't a manager, they have no reports
        if manager_id not in self.adjacency_list:
            return 0

        total_count = 0

        # Count each direct report plus all of their subordinates
        for direct_report in self.adjacency_list[manager_id]:
            # Each direct report counts as 1, plus all the people under them
            total_count += 1 + self.count_reports(direct_report)

        # Cache the result before returning
        self.memo[manager_id] = total_count
        return total_count

    def analyze_hierarchy(self) -> dict:
        """
        Computes the total report count for every manager in the organization.

        Returns:
            A dictionary mapping manager IDs to their total report counts.
        """
        results = {}

        # Calculate total reports for each manager in the organization
        for manager_id in self.managers:
            results[manager_id] = self.count_reports(manager_id)

        return results


# -----------------------------------------------------------------------------


class TestOrganizationAnalyzer(unittest.TestCase):
    """
    Unit tests for the OrganizationAnalyzer class.
    """

    def test_example_hierarchy(self):
        """
        Test the example hierarchy where A manages B and C, B manages D and E, and C manages F.
        """
        employees = ["A", "B", "C", "D", "E", "F"]
        reports_to = [["B", "A"], ["C", "A"], ["D", "B"], ["E", "B"], ["F", "C"]]

        analyzer = OrganizationAnalyzer(reports_to, employees)
        expected = {"A": 5, "B": 2, "C": 1}
        self.assertEqual(analyzer.analyze_hierarchy(), expected)

    def test_linear_hierarchy(self):
        """
        Test a linear chain of command: A -> B -> C -> D.
        """
        employees = ["A", "B", "C", "D"]
        reports_to = [["B", "A"], ["C", "B"], ["D", "C"]]

        analyzer = OrganizationAnalyzer(reports_to, employees)
        expected = {"A": 3, "B": 2, "C": 1}
        self.assertEqual(analyzer.analyze_hierarchy(), expected)

    def test_single_manager(self):
        """
        Test a flat hierarchy where one manager has multiple direct reports with no subordinates.
        """
        employees = ["A", "B", "C", "D"]
        reports_to = [["B", "A"], ["C", "A"], ["D", "A"]]

        analyzer = OrganizationAnalyzer(reports_to, employees)
        expected = {"A": 3}
        self.assertEqual(analyzer.analyze_hierarchy(), expected)

    def test_complex_hierarchy(self):
        """
        Test a more complex organizational structure with multiple levels and branches.
        """
        employees = ["Z", "Y", "X", "W", "V", "U"]
        reports_to = [["Y", "Z"], ["X", "Z"], ["W", "Y"], ["V", "X"], ["U", "X"]]

        analyzer = OrganizationAnalyzer(reports_to, employees)
        expected = {"Z": 5, "Y": 1, "X": 2}
        self.assertEqual(analyzer.analyze_hierarchy(), expected)


if __name__ == "__main__":
    unittest.main()
