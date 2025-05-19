n = int(input())
arr = []
for _ in range(n) :
    a = int(input())
    arr.append(a)
ans = 0

for i in range(n) :
    if i == 0 or arr[i] != arr[i-1] :
        ans += 1

print(ans)