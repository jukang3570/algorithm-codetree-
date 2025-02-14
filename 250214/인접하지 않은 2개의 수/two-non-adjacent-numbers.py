n = int(input())
arr = list(map(int,input().split()))
ans = -10000000000001
for i in range(n-2) :
    for j in range(i+2, n) :
        value = arr[i] + arr[j]
        ans = max(ans, value)
        
print(ans)