n = int(input())
arr = []
ans = 10000000001
for i in range(n) :
    a = int(input())
    arr.append(a)

for i in range(n) :
    value = 0
    cnt = i
    for j in range(i,n+i) :
        value += arr[cnt] * abs(i-j)
        cnt += 1
        if cnt >= n :
            cnt = 0
    cnt += 1
    ans = min(value,ans)
    
print(ans)