n = int(input())
arr = []
for _ in range(n) :
    a = int(input())
    arr.append(a)
minus = 0
plus = 0
ans = 0
for i in range(n) :
    if arr[i] < 0 :
        plus = 0
        minus += 1
    elif arr[i] > 0 :
        plus += 1
        minus = 0
    ans = max(plus,minus, ans)

print(ans)