def moveZeroes(nums):
    """
    Moves all zeros in a list to the end while maintaining the relative order of non-zero elements.

    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    j = 0  # Index for placing the next non-zero element

    # Iterate through the list
    for num in nums:
        # If the current element is non-zero
        if num != 0:
            # Place it at the current index j and increment j
            nums[j] = num
            j += 1

    # Fill the remaining elements from index j to the end with zeros
    for x in range(j, len(nums)):
        nums[x] = 0


# Test cases
def test_moveZeroes():
    # Test case 1: Basic example
    nums1 = [0, 1, 0, 3, 12]
    expected1 = [1, 3, 12, 0, 0]
    moveZeroes(nums1)
    assert nums1 == expected1

    # Test case 2: All zeros
    nums2 = [0, 0, 0, 0, 0]
    expected2 = [0, 0, 0, 0, 0]
    moveZeroes(nums2)
    assert nums2 == expected2

    # Test case 3: No zeros
    nums3 = [1, 2, 3, 4, 5]
    expected3 = [1, 2, 3, 4, 5]
    moveZeroes(nums3)
    assert nums3 == expected3

    # Test case 4: Single zero
    nums4 = [0]
    expected4 = [0]
    moveZeroes(nums4)
    assert nums4 == expected4

    # Test case 5: Empty list
    nums5 = []
    expected5 = []
    moveZeroes(nums5)
    assert nums5 == expected5

    # Test case 6: Zeros at the beginning
    nums6 = [0, 0, 1]
    expected6 = [1, 0, 0]
    moveZeroes(nums6)
    assert nums6 == expected6

    # Test case 7: Zeros at the end
    nums7 = [1, 2, 0, 0]
    expected7 = [1, 2, 0, 0]
    moveZeroes(nums7)
    assert nums7 == expected7

    print("All test cases passed!")


test_moveZeroes()
