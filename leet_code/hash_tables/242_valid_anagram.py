import unittest
from collections import Counter  # Used for the Pythonic hash table solution


# --- Combined Solution Class ---
class AnagramChecker:
    """
    A class containing different methods to check if two strings are anagrams.
    """

    def isAnagram_sorting(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams by sorting them.
        Time Complexity: O(N log N) due to sorting.
        Space Complexity: O(N) for sorted copies (or O(log N) to O(N) depending on sort).
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram_hash_manual(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams using manually implemented hash tables (dictionaries).
        Time Complexity: O(N) for iterating through strings.
        Space Complexity: O(K) for hash tables, where K is the number of unique characters (max O(N)).
        """
        if len(s) != len(t):
            return False

        s_char_counts = {}
        t_char_counts = {}

        for char_s in s:
            s_char_counts[char_s] = s_char_counts.get(char_s, 0) + 1

        for char_t in t:
            t_char_counts[char_t] = t_char_counts.get(char_t, 0) + 1

        return s_char_counts == t_char_counts

    def isAnagram_hash_counter(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams using collections.Counter.
        Time Complexity: O(N) for creating Counter objects.
        Space Complexity: O(K) for Counter objects (max O(N)).
        """
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


# --- Unit Tests for Combined Solution Class ---
class TestAnagramChecker(unittest.TestCase):
    def setUp(self):
        """Set up the AnagramChecker instance before each test."""
        self.checker = AnagramChecker()
        self.methods_to_test = [
            ("Sorting", self.checker.isAnagram_sorting),
            ("Hash Table (Manual)", self.checker.isAnagram_hash_manual),
            ("Hash Table (Counter)", self.checker.isAnagram_hash_counter),
        ]

    def test_empty_strings(self):
        """Test if two empty strings are anagrams using all methods."""
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertTrue(method("", ""), f"[{name}] Failed for empty strings")

    def test_simple_anagrams(self):
        """Test with simple valid anagrams using all methods."""
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertTrue(
                    method("listen", "silent"), f"[{name}] Failed for 'listen', 'silent'"
                )
                self.assertTrue(
                    method("rail safety", "fairy tales"),
                    f"[{name}] Failed for 'rail safety', 'fairy tales'",
                )
                self.assertTrue(
                    method("anagram", "nagaram"), f"[{name}] Failed for 'anagram', 'nagaram'"
                )

    def test_not_anagrams_different_lengths(self):
        """Test strings that are not anagrams due to different lengths using all methods."""
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertFalse(
                    method("hello", "hellos"), f"[{name}] Failed for 'hello', 'hellos'"
                )
                self.assertFalse(method("rat", ""), f"[{name}] Failed for 'rat', ''")

    def test_not_anagrams_same_length(self):
        """Test strings of the same length that are not anagrams using all methods."""
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertFalse(method("apple", "apply"), f"[{name}] Failed for 'apple', 'apply'")
                self.assertFalse(method("rat", "car"), f"[{name}] Failed for 'rat', 'car'")

    def test_anagrams_with_duplicates(self):
        """Test anagrams with duplicate characters using all methods."""
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertTrue(method("aabb", "bbaa"), f"[{name}] Failed for 'aabb', 'bbaa'")
                self.assertTrue(
                    method("racecar", "carrace"), f"[{name}] Failed for 'racecar', 'carrace'"
                )

    def test_not_anagrams_with_duplicates(self):
        """Test non-anagrams with duplicate characters but different counts using all methods."""
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertFalse(method("aaab", "bbba"), f"[{name}] Failed for 'aaab', 'bbba'")
                self.assertFalse(
                    method("helloo", "helooo"), f"[{name}] Failed for 'helloo', 'helooo'"
                )

    def test_case_sensitivity(self):
        """Test if the functions are case-sensitive using all methods."""
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
        """Test with special characters and numbers using all methods."""
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertTrue(method("123!@", "@!321"), f"[{name}] Failed for '123!@', '@!321'")
                self.assertFalse(method("12345", "12344"), f"[{name}] Failed for '12345', '12344'")

    def test_long_strings(self):
        """Test with longer strings for performance consideration using all methods."""
        long_s1 = "a" * 5000 + "b" * 5000
        long_s2 = "b" * 5000 + "a" * 5000
        long_s3 = "a" * 5000 + "b" * 5000 + "c"
        long_s4 = "b" * 5000 + "a" * 5000 + "d"
        for name, method in self.methods_to_test:
            with self.subTest(method_name=name):
                self.assertTrue(
                    method(long_s1, long_s2), f"[{name}] Failed for long string anagram"
                )
                self.assertFalse(
                    method(long_s3, long_s4), f"[{name}] Failed for long string non-anagram"
                )


if __name__ == "__main__":
    print("--- Running Anagram Unit Tests for Combined AnagramChecker Class ---")

    # unittest.main() is a simple way to run all tests in the current file.
    # verbosity=2 gives more detailed output.
    unittest.main(verbosity=2)

    # Example usage of the AnagramChecker class:
    checker = AnagramChecker()
    s1, t1 = "decimal", "medical"
    s2, t2 = "state", "taste"
    s3, t3 = "hello", "world"

    print(f"\nExample usage of AnagramChecker:")
    print(f"\nTesting '{s1}' and '{t1}':")
    print(f"  Sorting method: {checker.isAnagram_sorting(s1, t1)}")
    print(f"  Manual Hash method: {checker.isAnagram_hash_manual(s1, t1)}")
    print(f"  Counter Hash method: {checker.isAnagram_hash_counter(s1, t1)}")

    print(f"\nTesting '{s2}' and '{t2}':")
    print(f"  Sorting method: {checker.isAnagram_sorting(s2, t2)}")
    print(f"  Manual Hash method: {checker.isAnagram_hash_manual(s2, t2)}")
    print(f"  Counter Hash method: {checker.isAnagram_hash_counter(s2, t2)}")

    print(f"\nTesting '{s3}' and '{t3}':")
    print(f"  Sorting method: {checker.isAnagram_sorting(s3, t3)}")
    print(f"  Manual Hash method: {checker.isAnagram_hash_manual(s3, t3)}")
    print(f"  Counter Hash method: {checker.isAnagram_hash_counter(s3, t3)}")
