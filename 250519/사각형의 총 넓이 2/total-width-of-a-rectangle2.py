n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
grid = [ ['0' for _ in range(300)] for _ in range(300)]

for i in range(2) :
    for j in range(x1[i],x2[i]) :
        for k in range(y1[i],y2[i]) :
            grid[j][k] = '1'

# 마지막에
ans = sum(row.count('1') for row in grid)
print(ans)