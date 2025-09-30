a = [7,9,3,4, 1,5,10,15,12,9,18,23,14]

def merge_sort(left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        merge(left, mid, right)

def merge(start, mid , end):
    # c = a[start:mid + 1] + a[mid: end + 1]
    i = start
    j = mid + 1
    k = 0
    c = [0] * (end - start + 1)

    while i <= mid or j <= end:
        if i <= mid and j <= end:
            if a[i] <= a[j]:
                c[k] = a[i]
                i += 1
            else:
                c[k] = a[j]
                j += 1
        elif i <= mid:
            c[k] = a[i]
            i += 1
        else:
            c[k] = a[j]
            j += 1
        k += 1
    
    for i in range(len(c)):
        a[start + i] = c[i]

print(f"Before sorting {a}")
merge_sort(0, len(a) -1)
print(f"After sorting {a}")


# n = len(a)
# m = len(b)
# c = [0] * (n + m)
# i = j =k =0
# while i<n or j<m:
#     if i < n and j <m:
#         if a[i] < b[j]:
#             c[k] = a[i]
#             i += 1
#         else:
#             c[k] = b[j]
#             j += 1
#         k += 1
#     elif i < n:
#         c[k] = a[i]
#         i += 1
#         k += 1
#     else:
#         c[k] = b[j]
#         j += 1
#         k += 1