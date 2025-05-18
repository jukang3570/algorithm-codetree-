
n,m = map(int,input().split())
grid = [list(map(int,input().split()))for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        # 행 검사
        if j == 0 or grid[i][j] != grid[i][j - 1]:
            tmp = grid[i][j]
            cnt = 0
            for k in range(j, n):
                if tmp == grid[i][k]:
                    cnt += 1
                else:
                    break
            if cnt >= m:
                ans += 1

        # 열 검사
        if j == 0 or grid[j][i] != grid[j - 1][i]:
            tmp = grid[j][i]
            cnt = 0
            for k in range(j, n):
                if tmp == grid[k][i]:
                    cnt += 1
                else:
                    break
            if cnt >= m:
                ans += 1
if m == 1 : print(n*2)
else : print(ans)
        