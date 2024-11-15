#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# Divide and Conquer - sortedFrequency
import math


def sortedFrequency(arr, num):
    left_index = search_left(arr, num)
    right_index = search_right(arr, num)
    if left_index == -1 or right_index == -1:
        return -1
    return right_index - left_index + 1


def search_left(arr, num):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == num:
            if mid == 0 or arr[mid - 1] != num:
                result = mid
            right = mid - 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return result


def search_right(arr, num):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == num:
            if mid == len(arr) - 1 or arr[mid + 1] != num:
                result = mid
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return result
