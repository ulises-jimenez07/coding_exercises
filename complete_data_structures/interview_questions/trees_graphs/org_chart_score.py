# def dfs_recursive(self, vertex, visited):
#     visited.add(vertex)
#     print(vertex, end=" ")

#     for adjacent_vertex in self.adjacency_list[vertex]:
#         if adjacent_vertex not in visited:
#             self.dfs_recursive(adjacent_vertex, visited)
import unittest


def calculate_score(org_chart, node):
    """
    Calculates the score of a node in an organizational chart.
    Args:
        org_chart: A dictionary representing the organizational chart.
        node: The node whose score to calculate.
    Returns:
        The score of the node.
    """

    if node not in org_chart:
        return 0
    score = len(org_chart[node])  # Direct reports
    for report in org_chart[node]:
        score += calculate_score(
            org_chart, report
        )  # Recursive call for indirect reports

    return score


def calculate_score_optimized(org_chart, node, memo={}):
    """
    Calculates the score of a node in an organizational chart using dynamic programming.

    Args:
        org_chart: A dictionary representing the organizational chart.
        node: The node whose score to calculate.
        memo: A dictionary to store calculated scores for nodes.

    Returns:
        The score of the node.
    """

    if node in memo:
        return memo[node]
    if node not in org_chart:
        return 0

    score = len(org_chart[node])  # Direct reports
    for report in org_chart[node]:
        score += calculate_score_optimized(org_chart, report, memo)

    memo[node] = score
    return score


class TestOrgChartScore(unittest.TestCase):
    def setUp(self):
        self.org_chart = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F"],
            "D": [],
            "E": [],
            "F": [],
        }
        self.org_chart_2 = {
            "CEO": ["VP1", "VP2"],
            "VP1": ["Director1", "Director2"],
            "VP2": ["Director3"],
            "Director1": ["Manager1", "Manager2"],
            "Director2": ["Manager3"],
            "Director3": ["Manager4"],
        }

    def test_calculate_score_root(self):
        self.assertEqual(calculate_score(self.org_chart, "A"), 5)

    def test_calculate_score_middle(self):
        self.assertEqual(calculate_score(self.org_chart, "B"), 2)

    def test_calculate_score_leaf(self):
        self.assertEqual(calculate_score(self.org_chart, "D"), 0)

    def test_calculate_score_nonexistent(self):
        self.assertEqual(calculate_score(self.org_chart, "G"), 0)

    def test_calculate_score_empty_chart(self):
        self.assertEqual(calculate_score({}, "A"), 0)

    def test_calculate_score_optimized_root(self):
        self.assertEqual(calculate_score_optimized(self.org_chart, "A"), 5)

    def test_calculate_score_optimized_middle(self):
        self.assertEqual(calculate_score_optimized(self.org_chart, "B"), 2)

    def test_calculate_score_optimized_leaf(self):
        self.assertEqual(calculate_score_optimized(self.org_chart, "D"), 0)

    def test_calculate_score_optimized_nonexistent(self):
        self.assertEqual(calculate_score_optimized(self.org_chart, "G"), 0)

    def test_calculate_score_optimized_empty_chart(self):
        self.assertEqual(calculate_score_optimized({}, "A"), 0)

    def test_calculate_score_optimized_memoization(self):
        memo = {}
        self.assertEqual(calculate_score_optimized(self.org_chart, "A", memo), 5)
        self.assertEqual(memo["A"], 5)
        self.assertEqual(memo["B"], 2)
        self.assertEqual(memo["C"], 1)


if __name__ == "__main__":
    unittest.main()
