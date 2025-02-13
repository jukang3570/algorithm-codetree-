# Read input as a string
r,c = map(int,input().split())
arr = [list(input().split()) for _ in range(c)]
visited = [[0 for _  in range(r)] for i in range(c)]
ans =0

for _ in range(4) :
    for i in range(1,r) :
        for j in range(1,c) :
            if arr[i][j] == 'B' :
                for k in range(i+1,r) :
                    for p in range(j+1, c) :
                        if arr[k][p] == 'W':
                            for ans_r in range(k+1, r) :
                                for ans_c in range(p+1, c) :
                                    if arr[ans_r][ans_c] == 'B'and visited[k][p] == 0:
                                        ans +=1
                                        visited[k][p] = 1

print(ans)
