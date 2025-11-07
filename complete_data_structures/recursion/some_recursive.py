def isOdd(num):
    return num % 2 != 0


def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    return cb(arr[0]) or someRecursive(arr[1:], cb)
