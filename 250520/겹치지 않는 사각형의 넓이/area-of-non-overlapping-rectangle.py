a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = list(map(int,input().split()))

grid = [ ['0' for _ in range(2001)] for _ in range(2001)]

def square(x1, y1, x2, y2, c) :
    for i in range(x1, x2) :
        for j in range(y1,y2) :
            grid[i][j] = c

square(a[0],a[1],a[2],a[3], '1')
square(b[0],b[1],b[2],b[3], '1')
square(m[0],m[1],m[2],m[3], '0')

ans = 0
for row in grid :
    ans += row.count('1')
print(ans)

