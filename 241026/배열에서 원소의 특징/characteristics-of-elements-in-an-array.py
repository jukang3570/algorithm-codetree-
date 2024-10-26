arr = list(map(int, input().split()))
tmp = 0

for i in range(1,10) :
    if arr[i] % 3 == 0 and arr[i] != 0 :
        tmp = arr[i-1]
        break

print(tmp)