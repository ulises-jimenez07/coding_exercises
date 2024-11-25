from collections import deque
import unittest  # Import unittest for testing


class LRUCache(object):
    """
    Implements an LRU (Least Recently Used) cache using a deque and a dictionary.
    """

    def __init__(self, capacity):
        """
        Initializes the LRU cache with a given capacity.

        :type capacity: int
        """
        self.cache = (
            deque()
        )  # Deque to maintain the order of elements (most recent at the end)
        self.map = dict()  # Dictionary to store key-value pairs
        self.capacity = capacity  # Maximum capacity of the cache

    def get(self, key):
        """
        Retrieves the value associated with a given key.

        If the key is in the cache, move it to the end of the deque (making it most recent) and return its value.
        If not, return -1.

        :type key: int
        :rtype: int
        """
        if key in self.map:
            self.cache.remove(key)  # Remove the key from its current position
            self.cache.append(key)  # Append the key to the end (most recent)
            return self.map[key]  # Return the value associated with the key
        return -1  # Key not found

    def put(self, key, value):
        """
        Inserts or updates a key-value pair in the cache.

        If the key is already present, update its value and move it to the end of the deque.
        If the key is not present and the cache is full, remove the least recently used element (from the front of the deque)
        before inserting the new key-value pair.

        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.map:  # Check if the key is already in the cache
            if len(self.cache) == self.capacity:  # Check if the cache is full
                oldest = self.cache.popleft()  # Remove the least recently used key
                del self.map[oldest]  # Delete the key-value pair from the map
        else:  # If the key is already present
            self.cache.remove(key)  # Remove the key from its current position
        self.map[key] = value  # Update or insert the key-value pair
        self.cache.append(key)  # Append the key to the end (most recent)


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

    # def test_zero_capacity(self):  # Added for better coverage
    #     cache = LRUCache(0)  # Initialize with zero capacity
    #     cache.put(1, 1)
    #     self.assertEqual(cache.get(1), -1)


if __name__ == "__main__":
    unittest.main()
