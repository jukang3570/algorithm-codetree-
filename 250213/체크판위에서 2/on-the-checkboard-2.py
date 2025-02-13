# Read input as a string
r,c = map(int,input().split())
arr = [list(input().split()) for _ in range(c)]
ans =0

for i in range(1,r-1) :
    for j in range(1,c-1) :
        if arr[i][j] == 'B' :
            for k in range(i+1,r-1) :
                for p in range(j+1, c-1) :
                    if arr[k][p] == 'W':
                        ans += 1

print(ans)
