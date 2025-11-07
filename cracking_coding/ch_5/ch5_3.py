# you have an integer and you can flip exactly on bit
# find the length  of the longest merge


# Python program to find Index
# of 0 to be replaced with 1 to get
# longest continuous sequence
# of 1s in a binary array


# Returns index of 0 to be
# replaced with 1 to get longest
# continuous sequence of 1s.
#  If there is no 0 in array, then
# it returns -1.
def maxOnesIndex(arr, n):
    # for maximum number of 1 around a zero
    max_count = 0
    # for storing result
    max_index = 0
    # index of previous zero
    prev_zero = -1
    # index of previous to previous zero
    prev_prev_zero = -1
    # Traverse the input array
    for curr in range(n):
        print(
            f"Current: {curr}, Max_index: {max_index}, Max_count: {max_count}, prev_zero: {prev_zero}, prev_prev_zero: {prev_prev_zero}"
        )
        # If current element is 0,
        # then calculate the difference
        # between curr and prev_prev_zero
        if arr[curr] == 0:
            # Update result if count of
            # 1s around prev_zero is more
            if curr - prev_prev_zero > max_count:
                max_count = curr - prev_prev_zero
                max_index = prev_zero
                # Update for next iteration
            prev_prev_zero = prev_zero
            prev_zero = curr
    # Check for the last encountered zero

    if n - prev_prev_zero > max_count:
        max_index = prev_zero
    print(
        f"Current: {curr}, Max_index: {max_index}, Max_count: {max_count}, prev_zero: {prev_zero}, prev_prev_zero: {prev_prev_zero}"
    )
    return max_index


# Driver program

arr = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
n = len(arr)

print("Index of 0 to be replaced is ", maxOnesIndex(arr, n))
