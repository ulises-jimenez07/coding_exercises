def sparse_search(arr, item):
    def inner_search(arr, item, low, high):
        middle = low + (high - low) // 2

        if arr[middle] == "":
            left = middle - 1
            right = middle + 1
            while True:
                if left < low and right > high:
                    return None
                elif right <= high and arr[right] != "":
                    middle = right
                    break
                elif left >= low and arr[left] != "":
                    middle = left
                    break
                left -= 1
                right += 1

        if arr[middle] == item:
            return middle
        if arr[middle] < item:
            return inner_search(arr, item, middle + 1, high)
        if arr[middle] > item:
            return inner_search(arr, item, low, middle - 1)

    return inner_search(arr, item, 0, len(arr) - 1)


test_cases = [
    (["a", "", "", "b", "", "c", "", "", "d", "", "", "", "", "e", ""], "d"),
    (["a", "", "", "b", "", "c", "", "", "d", "", "", "", "", "e", ""], "f"),
    (["a", "", "", "b", "", "c", "", "", "d", "", "", "", "", "e", ""], "a"),
]

for test in test_cases:
    print(sparse_search(test[0], test[1]))
