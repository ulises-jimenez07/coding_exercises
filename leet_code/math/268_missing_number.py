def missingNumber(self, nums):
    """
    Finds the missing number in a list of distinct numbers from 0 to n.

    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.

    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    target_sum = n * (n + 1) / 2  # Calculate the expected sum of numbers from 0 to n
    tot_sum = 0  # Initialize the sum of numbers in the input list
    for num in nums:
        tot_sum += num  # Sum the numbers in the input list
    return int(
        target_sum - tot_sum
    )  # Return the difference, which is the missing number (cast to int for consistency)


# Test cases
def test_missingNumber():
    # Test case 1: Basic example
    nums1 = [3, 0, 1]
    expected1 = 2
    assert (
        missingNumber(None, nums1) == expected1
    ), f"Test case 1 failed. Expected {expected1}, but got {missingNumber(None, nums1)}"

    # Test case 2: Missing number at the beginning
    nums2 = [1, 2, 3]
    expected2 = 0
    assert (
        missingNumber(None, nums2) == expected2
    ), f"Test case 2 failed. Expected {expected2}, but got {missingNumber(None, nums2)}"

    # Test case 3: Missing number at the end
    nums3 = [0, 1, 2]
    expected3 = 3
    assert (
        missingNumber(None, nums3) == expected3
    ), f"Test case 3 failed. Expected {expected3}, but got {missingNumber(None, nums3)}"

    # Test case 4: Single element list
    nums4 = [0]
    expected4 = 1
    assert (
        missingNumber(None, nums4) == expected4
    ), f"Test case 4 failed. Expected {expected4}, but got {missingNumber(None, nums4)}"

    # Test case 5: Empty list (edge case)
    nums5 = []
    expected5 = 0  # When n=0 the range is [0,0]
    assert (
        missingNumber(None, nums5) == expected5
    ), f"Test case 5 failed. Expected {expected5}, but got {missingNumber(None, nums5)}"

    print("All test cases passed!")


test_missingNumber()
