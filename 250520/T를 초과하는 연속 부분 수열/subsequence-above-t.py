ans = 0
cnt = 0
n, t = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(n) :
    if arr[i] > t :
        cnt += 1
    else : cnt = 0
    ans = max(ans,cnt)

print(ans)