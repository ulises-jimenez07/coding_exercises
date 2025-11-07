"""
Problem: Implement LRU (Least Recently Used) cache with get and put operations

Approach:
- Use dictionary for O(1) key-value lookups
- Use deque to track access order (most recent at end)
- On get: move key to end of deque
- On put: add new key or evict oldest if at capacity
- Time complexity: O(n) per operation due to deque.remove()
- Space complexity: O(capacity)
"""

import unittest
from collections import deque


class LRUCache:
    def __init__(self, capacity):
        self.cache = deque()
        self.map = dict()
        self.capacity = capacity

    def get(self, key):
        if key in self.map:
            self.cache.remove(key)  # Mark as recently used
            self.cache.append(key)
            return self.map[key]
        return -1

    def put(self, key, value):
        if key not in self.map:
            if len(self.cache) == self.capacity:
                oldest = self.cache.popleft()  # Evict LRU
                del self.map[oldest]
        else:
            self.cache.remove(key)
        self.map[key] = value
        self.cache.append(key)  # Mark as recently used


# Test cases using unittest
class TestLRUCache(unittest.TestCase):
    def test_basic_operations(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)  # Returns 1
        cache.put(3, 3)  # Evicts key 2
        self.assertEqual(cache.get(2), -1)  # Returns -1 (not found)
        cache.put(4, 4)  # Evicts key 1
        self.assertEqual(cache.get(1), -1)  # Returns -1 (not found)
        self.assertEqual(cache.get(3), 3)  # Returns 3
        self.assertEqual(cache.get(4), 4)  # Returns 4

    def test_empty_cache(self):
        cache = LRUCache(1)
        self.assertEqual(cache.get(1), -1)  # Empty cache

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)  # Update key 1
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 2)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
