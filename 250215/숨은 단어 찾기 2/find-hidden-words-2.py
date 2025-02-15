dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 0, 1, -1, -1, 0, -1, 1]

n , m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
cnt = 0


for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 'L' :
            x =0
            y= 0
            for d in range(8) :
                x = i + dx[d]
                y = j + dy[d]
                if x >= 0 and x <n and y >= 0 and y < m :
                    if arr[x][y] == 'E' :
                        x += dx[d]
                        y += dy[d]
                        if x >= 0 and x <n and y >= 0 and y < m :
                            if arr[x][y] == 'E':
                                cnt += 1

print(cnt)