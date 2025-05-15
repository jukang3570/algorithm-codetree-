n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
avg = sum(blocks) // n
ans = 0
for num in blocks :
    if num < avg :
        ans += abs(num-avg)

print(ans)