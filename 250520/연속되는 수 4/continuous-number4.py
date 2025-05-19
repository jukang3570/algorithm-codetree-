n = int(input())
arr = []
cnt = 0
ans = 0
for _ in range(n) :
    a = int(input())
    arr.append(a)
for i in range(n) :
    if i == 0 or arr[i] > arr[i-1] :
        cnt += 1
    else : cnt = 1
    ans = max(ans,cnt)

print(ans)