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
print(ans)