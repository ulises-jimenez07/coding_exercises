a = [10,50,40,20,15,16,2,3,8,9,99,34,43,100,121,104,132]

def quick_sort(left, right):
    if left < right:
        partition_point = partition(left, right)
        quick_sort(left, partition_point -1)
        quick_sort(partition_point + 1, right)

def partition(start, end):
    left = start -1
    pivot = a[end]
    for i in range(start, end):
        if a[i] <= pivot:
            left += 1
            a[left], a [i] =a[i], a[left]

    left += 1
    a[end], a[left] = a[left], a[end]
    return left

print(f"Before Sorting {a}")
quick_sort(0, len(a)-1)
print(f"After Sorting {a}")

# a = [1, 5, 2,6, 0,4,3]
# print(f"Before partioning {a}")
# n = len(a)

# key = a[-1]
# left = -1
# for i in range(n-1):
#     if a[i] <= key:
#         left += 1
#         a[i], a[left] = a[left], a[i]

# left += 1
# a[-1], a[left] = a[left], a[n-1]

# print(f"After partioning {a}")
