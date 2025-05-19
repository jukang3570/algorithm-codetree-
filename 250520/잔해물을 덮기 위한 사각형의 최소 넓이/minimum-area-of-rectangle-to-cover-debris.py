grid = [ [0 for _ in range(2001)] for _ in range(2001)]
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def square(x1, y1, x2, y2, c) :
    for i in range(x1, x2) :
        for j in range(y1,y2) :
            grid[i][j] = c

square(a[0]+1000,a[1]+1000,a[2]+1000,a[3]+1000, '1')
square(b[0]+1000,b[1]+1000,b[2]+1000,b[3]+1000, '0')
min_x,min_y,max_x,max_y = 2000, 2000, 0, 0
flag = False
for i in range(2000) :
    for j in range(2000) :
        if grid[i][j] == '1' :
            flag = True
            min_x = min(min_x, i)
            min_y = min(min_y, j)
            max_x = max(max_x, i)
            max_y = max(max_y, j)

if flag == False : print(0)
else : print ( (max_x - min_x + 1) * (max_y - min_y + 1) )