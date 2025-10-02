arr = [2,5,1,2,3,4,6,5,2]

print(f"Before sorting {arr}")
max_element = max(arr)
freq = [0] *(max_element +1)

for num in arr:
    freq[num] += 1


for i in range(1, len(freq)):
    freq[i] = freq[i-1] +freq[i]

temp = [0] *len(arr)

for i in range(len(arr) -1, -1,-1):
    cnt = freq[arr[i]]
    temp[cnt -1] = arr[i]
    freq[arr[i]] -= 1

for i in range(len(temp)):
    arr[i] = temp[i]

print(f"After sorting {arr}")