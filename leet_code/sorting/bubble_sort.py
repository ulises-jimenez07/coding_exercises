li = [10, 25, 20, 50, 25, 15, 40]

print(f"Before sorting: {li}")
n = len(li)
for i in range(n):
    for j in range( n - i - 1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1] , li[j]

print(f"After sorting: {li}")
