grid = [ [0 for _ in range(2001)] for _ in range(2001)]
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def square(x1, y1, x2, y2, c) :
    for i in range(x1, x2+1) :
        for j in range(y1,y2+1) :
            grid[i][j] = c

square(a[0]+1000,a[1]+1000,a[2]+1000,a[3]+1000, '1')
square(b[0]+1000,b[1]+1000,b[2]+1000,b[3]+1000, '0')
ans = 0
for row in grid :
    ans += row.count('1')
print(ans)