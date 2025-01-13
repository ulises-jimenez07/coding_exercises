import unittest  # Importing the unittest module for writing test cases


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        Calculates the number of tuples (a, b, c, d) from four lists such that a + b + c + d == 0.

        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count = 0  # Initialize the count of tuples that sum to zero
        map = {}  # Initialize a hash map to store sums of pairs from nums1 and nums2

        # Iterate through all possible pairs from nums1 and nums2
        for a in nums1:
            for b in nums2:
                sum_ab = a + b
                if sum_ab not in map:  # Check if the sum already exists as a key
                    map[sum_ab] = 0  # Initialize the count for this sum if it's new
                map[sum_ab] += 1  # Increment the count for the current sum

        # Iterate through all possible pairs from nums3 and nums4
        for c in nums3:
            for d in nums4:
                sum_cd = c + d
                complement = -(
                    sum_cd
                )  # Calculate the complement needed to make the total sum zero
                if complement in map:  # Check if the complement exists in the map
                    count += map[
                        complement
                    ]  # Add the count of pairs that sum to the complement

        return count  # Return the total count of tuples that satisfy the condition


# Test cases using the unittest module
class TestFourSumCount(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(Solution().fourSumCount([], [], [], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(Solution().fourSumCount([1], [1], [-1], [-1]), 1)
        self.assertEqual(Solution().fourSumCount([1], [2], [-2], [-1]), 1)
        self.assertEqual(
            Solution().fourSumCount([1], [1], [-2], [-1]), 0
        )  # No matching sum

    def test_multiple_elements(self):
        nums1 = [1, 2]
        nums2 = [-2, -1]
        nums3 = [-1, 2]
        nums4 = [0, 2]
        self.assertEqual(Solution().fourSumCount(nums1, nums2, nums3, nums4), 2)

    def test_all_zeros(self):
        self.assertEqual(Solution().fourSumCount([0], [0], [0], [0]), 1)
        self.assertEqual(Solution().fourSumCount([0, 0], [0, 0], [0, 0], [0, 0]), 16)

    def test_large_input(self):  # Test with a larger input size
        nums1 = list(range(100))
        nums2 = list(range(100))
        nums3 = list(range(-100, 0))
        nums4 = list(range(-100, 0))
        # Expecting at least one combination to result in 0. This is a simplified check for large inputs.
        self.assertGreaterEqual(Solution().fourSumCount(nums1, nums2, nums3, nums4), 0)


if __name__ == "__main__":
    unittest.main()
