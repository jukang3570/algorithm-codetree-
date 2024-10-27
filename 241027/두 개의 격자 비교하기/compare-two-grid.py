n, m = tuple(map(int, input().split()))

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr_1 = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr_ans = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n) :
    for j in range(m) :
        if arr[i][j] != arr_1[i][j] :
            arr_ans[i][j] = 1

for i in range(n) :
    for j in range(m) :
        print(arr_ans[i][j], end =" ")
    print()