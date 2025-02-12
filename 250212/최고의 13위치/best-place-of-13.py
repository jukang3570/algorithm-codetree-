n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
cnt = 0
max_value = 0
for i in range(n) :
    for j in range(n-2) :
        cnt = 0
        for k in range(j,j+3) :
            if grid[i][k] == 1 :
                cnt += 1
    if cnt > max_value :
        max_value = cnt

print(max_value)