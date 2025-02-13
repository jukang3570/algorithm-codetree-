# 입력 처리
a = list(map(int,input()))
ans = 0
cnt = 0
for i in range(len(a)) :
    if a[i] == 0:
        a[i] = 1
        break

for i in range(len(a)-1, -1, -1) :
    ans += a[i] * (pow(2,cnt))
    cnt += 1
if len(a) < 2 and a[i] == 1:
    print(0)
else:
    print(ans)