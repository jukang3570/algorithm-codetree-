n = int(input())
arr = list(map(int, input().split()))
tmp = 0

# Write your code here!
for i in range(len(arr)) :
    for j in range(i+1, len(arr)) :
        if arr[i] > arr[j] :
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

for _ in range(n) :
    print(arr[_], end = ' ')