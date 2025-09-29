li = [10, 25, 20, 50, 25, 15, 40]

print(f"Before sorting: {li}")


n = len(li)
for i in range(n):
    swap_index = i
    for j in range(i, n):
        if li[j] < li[swap_index]:
            swap_index = j
    print(f"Putting {li[swap_index]} at index {i}")
    li[i], li[swap_index] = li[swap_index], li[i]

print(f"After sorting: {li}")
