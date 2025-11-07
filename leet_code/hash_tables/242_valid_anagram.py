"""
Problem: Check if two strings are anagrams of each other

Approach:
- Compare character frequency using hash table (Counter)
- Alternative: sort both strings and compare
- Time complexity: O(n) for hash table, O(n log n) for sorting
- Space complexity: O(n)
"""

import unittest
from collections import Counter


class AnagramChecker:
    def isAnagram_sorting(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram_hash_manual(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_char_counts: dict[str, int] = {}
        t_char_counts: dict[str, int] = {}

        for char_s in s:
            s_char_counts[char_s] = s_char_counts.get(char_s, 0) + 1

        for char_t in t:
            t_char_counts[char_t] = t_char_counts.get(char_t, 0) + 1

        return s_char_counts == t_char_counts

    def isAnagram_hash_counter(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


class TestAnagramChecker(unittest.TestCase):
    def setUp(self):
        self.checker = AnagramChecker()
        self.methods_to_test = [
            ("Sorting", self.checker.isAnagram_sorting),
            ("Hash Table (Manual)", self.checker.isAnagram_hash_manual),
            ("Hash Table (Counter)", self.checker.isAnagram_hash_counter),
        ]

    def test_empty_strings(self):
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertTrue(method("", ""), f"[{name}] Failed for empty strings")

    def test_simple_anagrams(self):
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertTrue(method("listen", "silent"), f"[{name}] Failed for 'listen', 'silent'")
                self.assertTrue(
                    method("rail safety", "fairy tales"),
                    f"[{name}] Failed for 'rail safety', 'fairy tales'",
                )
                self.assertTrue(method("anagram", "nagaram"), f"[{name}] Failed for 'anagram', 'nagaram'")

    def test_not_anagrams_different_lengths(self):
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertFalse(method("hello", "hellos"), f"[{name}] Failed for 'hello', 'hellos'")
                self.assertFalse(method("rat", ""), f"[{name}] Failed for 'rat', ''")

    def test_not_anagrams_same_length(self):
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertFalse(method("apple", "apply"), f"[{name}] Failed for 'apple', 'apply'")
                self.assertFalse(method("rat", "car"), f"[{name}] Failed for 'rat', 'car'")

    def test_anagrams_with_duplicates(self):
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertTrue(method("aabb", "bbaa"), f"[{name}] Failed for 'aabb', 'bbaa'")
                self.assertTrue(method("racecar", "carrace"), f"[{name}] Failed for 'racecar', 'carrace'")

    def test_not_anagrams_with_duplicates(self):
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertFalse(method("aaab", "bbba"), f"[{name}] Failed for 'aaab', 'bbba'")
                self.assertFalse(method("helloo", "helooo"), f"[{name}] Failed for 'helloo', 'helooo'")

    def test_case_sensitivity(self):
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertFalse(
                    method("Listen", "silent"),
                    f"[{name}] Failed for 'Listen', 'silent' (case sensitive)",
                )
                self.assertTrue(
                    method("Listen", "Listen"),
                    f"[{name}] Failed for 'Listen', 'Listen' (identical case)",
                )

    def test_special_characters_and_numbers(self):
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertTrue(method("123!@", "@!321"), f"[{name}] Failed for '123!@', '@!321'")
                self.assertFalse(method("12345", "12344"), f"[{name}] Failed for '12345', '12344'")

    def test_long_strings(self):
        long_s1 = "a" * 5000 + "b" * 5000
        long_s2 = "b" * 5000 + "a" * 5000
        long_s3 = "a" * 5000 + "b" * 5000 + "c"
        long_s4 = "b" * 5000 + "a" * 5000 + "d"
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertTrue(method(long_s1, long_s2), f"[{name}] Failed for long string anagram")
                self.assertFalse(method(long_s3, long_s4), f"[{name}] Failed for long string non-anagram")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
