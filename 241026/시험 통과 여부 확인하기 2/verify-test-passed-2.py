a = int(input())
cnt = 0
ans = []

for i in range(a) :
    arr = list(map(int,input().split()))
    avg = 0
    sum = 0
    for i in arr :
        sum += i
    avg = sum / 4
    if avg >= 60 :
        ans.append("pass")
        cnt += 1 
    elif avg < 60 :
        ans.append("fail")

for i in range(a) :
    print(ans[i])
print(cnt)