n = int(input())
arr = []
for _ in range(n) :
    a = int(input())
    arr.append(a)
ans = 1
cnt = 1
for i in range(n) :
    if i == 0 or arr[i] == arr[i-1] :
        cnt += 1
    else : 
        ans = max(ans,cnt)
        cnt = 1


print(ans)