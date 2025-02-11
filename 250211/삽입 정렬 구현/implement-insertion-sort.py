n = int(input())
arr = list(map(int, input().split()))



for i in range(1,n):
    key = arr[i]
    while i > 0 and arr[i] < arr[i-1]:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1

print(*arr)