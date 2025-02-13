# 입력 처리
a = list(map(int,input()))
ans = 0
cnt = 0
check = True
for i in range(len(a)) :
    if a[i] == 0:
        a[i] = 1
        check = False
        break
if check == True :
    for i in range(len(a)-1, -1, -1) :
        if a[i] == 1:
            a[i] = 0
            break

for i in range(len(a)-1, -1, -1) :
    ans += a[i] * (pow(2,cnt))
    cnt += 1

print(ans)