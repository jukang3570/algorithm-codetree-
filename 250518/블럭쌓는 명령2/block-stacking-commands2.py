n, k = map(int,input().split())
arr = [ 0 for _ in range(n+1)]
for _ in range(k) :
    a,b = map(int,input().split())
    for k in range(a,b+1) :
        arr[k] += 1

print(max(arr))