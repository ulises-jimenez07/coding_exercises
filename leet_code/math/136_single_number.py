class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Finds the single number that appears only once in a list where every other number appears twice.

        This method utilizes the bitwise XOR operator to efficiently find the single number.
        XOR has the following properties:
        - x ^ x = 0  (A number XORed with itself is 0)
        - x ^ 0 = x  (A number XORed with 0 is itself)
        - XOR is commutative and associative, meaning the order of operations doesn't matter.

        By XORing all numbers in the list, the numbers appearing twice will cancel each other out (become 0),
        leaving only the single number XORed with 0, which results in the single number itself.

        Args:
            nums: A list of integers where every element appears twice except for one.

        Returns:
            The single number that appears only once.
        """
        ans = 0
        for num in nums:
            ans ^= num  # XOR each number with the current result

        return ans


# Test cases
solution = Solution()

# Test case 1: Basic example
nums1 = [2, 2, 1]
expected1 = 1
assert (
    solution.singleNumber(nums1) == expected1
), f"Test case 1 failed. Expected: {expected1}, Got: {solution.singleNumber(nums1)}"

# Test case 2: Single number at the beginning
nums2 = [1, 2, 2]
expected2 = 1
assert (
    solution.singleNumber(nums2) == expected2
), f"Test case 2 failed. Expected: {expected2}, Got: {solution.singleNumber(nums2)}"

# Test case 3: Single number at the end
nums3 = [2, 1, 2]
expected3 = 1
assert (
    solution.singleNumber(nums3) == expected3
), f"Test case 3 failed. Expected: {expected3}, Got: {solution.singleNumber(nums3)}"

# Test case 4: Longer list
nums4 = [4, 1, 2, 1, 2]
expected4 = 4
assert (
    solution.singleNumber(nums4) == expected4
), f"Test case 4 failed. Expected: {expected4}, Got: {solution.singleNumber(nums4)}"

# Test case 5: List with a single element
nums5 = [5]
expected5 = 5
assert (
    solution.singleNumber(nums5) == expected5
), f"Test case 5 failed. Expected: {expected5}, Got: {solution.singleNumber(nums5)}"


print("All test cases passed!")  # This will print only if all assertions pass
