n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
count_list = set()
for i in range(n) :
    for j in range(n-2) :
        cnt = 0
        for k in range(j,j+3) :
            if arr[i][k] == 1 :
                cnt += 1
        count_list.add(cnt)

count_list = list(count_list)
count_list.sort(reverse=True)
print(count_list[0] + count_list[1])