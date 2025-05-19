n = int(input())

grid = [ ['0' for _ in range(201)]for _ in range(201)]
for _ in range(n) :
    a,b = map(int,input().split())
    a += 100
    b += 100
    for i in range(a, a+8) :
        for j in range(b, b+8) :
            grid[i][j] = '1'

ans = 0
for row in grid :
    ans += row.count('1')
print(ans)
