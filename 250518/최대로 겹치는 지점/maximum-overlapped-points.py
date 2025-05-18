n = int(input())
arr = [ 0 for _ in range(101)]
for _ in range(n) :
    a,b = map(int,input().split())
    for k in range(a,b+1) :
        arr[k] += 1

print(max(arr))