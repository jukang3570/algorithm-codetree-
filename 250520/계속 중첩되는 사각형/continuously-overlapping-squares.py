grid = [ [ '0' for _ in range(201)] for _ in range(201)]
n = int(input())

def square(x1,y1,x2,y2, c) :
    for i in range(x1,x2) :
        for j in range(y1,y2) :
            grid[i][j] = c

for i in range(1, n+1) :
    x1, y1, x2, y2 = map(int,input().split())
    #red
    if i % 2 == 1 :
        square(x1+100, y1+100, x2+100, y2+100, 'r')
    #blue
    elif i % 2 == 0 :
        square(x1+100, y1+100, x2+100, y2+100, 'b')

ans = 0
for row in grid :
    ans += row.count('b')
print(ans)