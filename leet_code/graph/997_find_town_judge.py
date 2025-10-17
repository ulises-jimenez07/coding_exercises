from typing import List
import unittest

class Solution:
    """
    Finds the town judge in a town of N people.
    The town judge is defined as the person who is trusted by everybody else 
    (N-1 people) and trusts nobody.
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Calculates the in-degree and out-degree for each person to find the judge.

        :param n: The number of people in the town (labeled 1 to n).
        :param trust: A list of trust relationships, where trust[i] = [a, b] 
                      represents that person 'a' trusts person 'b'.
        :return: The label of the town judge if they exist, otherwise -1.
        """
        
        # Initialize arrays to store the number of people a person trusts (out-degree)
        # and the number of people who trust a person (in-degree).
        # We use size n + 1 because people are labeled from 1 to n. Index 0 is unused.
        out_degree = [0] * (n + 1)
        in_degree = [0] * (n + 1)

        # Iterate through all trust relationships to populate the degrees.
        for rel in trust:
            # 'from_val' trusts 'to_val'
            from_val, to_val = rel
            
            # Increment the out-degree of the person who trusts (from_val)
            out_degree[from_val] += 1
            
            # Increment the in-degree of the person who is trusted (to_val)
            in_degree[to_val] += 1

        # Check each person (from 1 to n) to see if they meet the judge criteria.
        for i in range(1, n+1):
            # Judge criteria:
            # 1. Trusted by N-1 people (in_degree == n - 1)
            # 2. Trusts nobody (out_degree == 0)
            if in_degree[i] == (n - 1) and out_degree[i] == 0:
                # If both conditions are met, person 'i' is the judge.
                return i
        
        # If no person meets the judge criteria after checking everyone, return -1.
        return -1


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class's findJudge method.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example_1_judge_exists(self):
        """Test case where the judge is person 2."""
        n = 2
        trust = [[1, 2]]
        # Person 2 is trusted by 1 person (1), trusts 0 people. n-1 = 1.
        self.assertEqual(self.solution.findJudge(n, trust), 2)

    def test_example_2_no_judge(self):
        """Test case where there is no judge."""
        n = 3
        trust = [[1, 3], [2, 3], [3, 1]]
        # Person 3 is trusted by 2 people, but also trusts person 1 (out-degree is 1).
        self.assertEqual(self.solution.findJudge(n, trust), -1)

    def test_example_3_judge_exists(self):
        """Test case where the judge is person 3."""
        n = 3
        trust = [[1, 3], [2, 3]]
        # Person 3 is trusted by 2 people (1 and 2), trusts 0 people. n-1 = 2.
        self.assertEqual(self.solution.findJudge(n, trust), 3)

    def test_example_4_no_judge_incomplete_trust(self):
        """Test case with 4 people but not everyone trusts a potential judge."""
        n = 4
        trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
        # Potential judge: Person 3. Trusted by 3 people (1, 2, 4), trusts 0. n-1 = 3.
        self.assertEqual(self.solution.findJudge(n, trust), 3)

    def test_single_person_is_judge(self):
        """Test case with only one person (N=1). They must be the judge."""
        n = 1
        trust = [] # An empty list of trust relationships
        # Person 1: trusted by 1-1=0 people, trusts 0 people.
        self.assertEqual(self.solution.findJudge(n, trust), 1)

    def test_no_trust_judge_not_possible_n_greater_than_1(self):
        """Test case with multiple people but no trust relationships."""
        n = 3
        trust = []
        # No person is trusted by n-1 = 2 people.
        self.assertEqual(self.solution.findJudge(n, trust), -1)

    def test_everyone_trusts_everyone_no_judge(self):
        """Test case where everyone trusts everyone else."""
        n = 3
        trust = [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
        # Everyone trusts at least one person (out-degree >= 1). No judge possible.
        self.assertEqual(self.solution.findJudge(n, trust), -1)
    
    def test_complex_case_no_judge(self):
        """Test a more complex scenario where no one fully meets the criteria."""
        n = 5
        trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]
        # No one has in-degree of 4 and out-degree of 0.
        self.assertEqual(self.solution.findJudge(n, trust), -1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)