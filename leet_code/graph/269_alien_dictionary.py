"""
Problem: Alien Dictionary
Given a lexicographically sorted list of words in an alien language, find the order
of its characters.

Approach: Topological Sort (Kahn's BFS)
- Compare each adjacent pair of words character by character to derive ordering edges.
- The first position where they differ gives: char_a comes before char_b → edge a→b.
- Build a directed graph of these constraints, then topological sort to find the order.
- If a cycle is detected or input is invalid, return an empty list.

Complexity:
- Time:  O(C) where C is total length of all words
- Space: O(1) — at most 26 unique characters
"""

import unittest
from collections import (
    defaultdict,
    deque,
)
from typing import List


class Solution:
    """Topological sort solution for the alien dictionary problem."""

    def alienOrder(self, words: List[str]) -> str:
        """Return character order in the alien language via topological sort."""
        # Collect all unique characters and initialize in-degree to 0
        in_degree = {c: 0 for word in words for c in word}
        graph: defaultdict[str, set[str]] = defaultdict(set)

        # Compare adjacent word pairs to build ordering constraints
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            found_diff = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    # w1[j] must come before w2[j]
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    found_diff = True
                    break

            # Invalid: w1 is longer than w2 and w2 is a prefix of w1
            if not found_diff and len(w1) > len(w2):
                return ""

        # BFS topological sort: start with all characters of in-degree 0
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If result doesn't include all characters, a cycle exists
        if len(result) != len(in_degree):
            return ""

        return "".join(result)


class TestAlienDictionary(unittest.TestCase):
    """Unit tests for Solution.alienOrder."""

    def setUp(self):
        self.solution = Solution()

    def test_example_main(self):
        """xww before wxyz → x<w; wxyz before wxyw → z<w; wxyw before ywx → w<y; ywx before ywz → x<z"""
        words = ["xww", "wxyz", "wxyw", "ywx", "ywz"]
        result = self.solution.alienOrder(words)
        # Validate all derived constraints hold in result
        order = {c: i for i, c in enumerate(result)}
        self.assertLess(order["x"], order["w"])
        self.assertLess(order["z"], order["w"])
        self.assertLess(order["w"], order["y"])
        self.assertLess(order["x"], order["z"])

    def test_example_1(self):
        """baa before abcd → b<a; abcd before abca → d<a; abca before cab → b<c; cab before cad → b<d"""
        words = ["baa", "abcd", "abca", "cab", "cad"]
        result = self.solution.alienOrder(words)
        order = {c: i for i, c in enumerate(result)}
        self.assertLess(order["b"], order["a"])
        self.assertLess(order["d"], order["a"])
        self.assertLess(order["b"], order["c"])
        self.assertLess(order["b"], order["d"])

    def test_example_2(self):
        """caa before aaa → c<a; aaa before aab → a<b"""
        words = ["caa", "aaa", "aab"]
        result = self.solution.alienOrder(words)
        order = {c: i for i, c in enumerate(result)}
        self.assertLess(order["c"], order["a"])
        self.assertLess(order["a"], order["b"])

    def test_single_word(self):
        """Single word — all characters appear but no ordering constraints."""
        words = ["abc"]
        result = self.solution.alienOrder(words)
        self.assertEqual(set(result), {"a", "b", "c"})

    def test_invalid_prefix_order(self):
        """abc before ab is invalid (longer word listed before its prefix)."""
        words = ["abc", "ab"]
        self.assertEqual(self.solution.alienOrder(words), "")

    def test_two_chars(self):
        """z before a → z<a."""
        words = ["z", "a"]
        result = self.solution.alienOrder(words)
        order = {c: i for i, c in enumerate(result)}
        self.assertLess(order["z"], order["a"])


if __name__ == "__main__":
    unittest.main()
