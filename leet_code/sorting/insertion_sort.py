li = [10, 25, 20, 50, 25, 15, 40]

print(f"Before sorting: {li}")
n = len(li)

for i in range(1, n):
    j = i -1
    key = li[i]
    while j >= 0 and li[j] > key:
        li[j+1]= li[j]
        j-= 1
    li[j+1]= key
    print(li[: i+1])


print(f"After sorting: {li}")