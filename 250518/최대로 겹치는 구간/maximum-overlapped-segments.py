n = int(input())
arr = [ 0 for _ in range(200)]

for _ in range(n) :
    a,b = map(int,input().split())
    if a < 0 or b < 0 :
        a += 100
        b += 100
    for k in range(a,b) :
        arr[k] += 1

print(max(arr))