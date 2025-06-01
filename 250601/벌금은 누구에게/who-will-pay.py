n,m,k = map(int,input().split())
arr = [ 0 for _ in range(n+1)]
ans = 0
for t in range(m) :
    a = int(input())
    arr[a] += 1
    if arr[a] >= k : 
        ans = a
        break

if ans != 0 : print(ans)
else : print(-1)