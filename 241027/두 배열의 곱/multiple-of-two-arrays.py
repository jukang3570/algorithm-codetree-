arr = [
    list(map(int, input().split()))
    for _ in range(3)
]
input()

arr_1 = [
    list(map(int, input().split()))
    for _ in range(3)
]

arr_ans = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3) :
    for j in range(3) :
        arr_ans[i][j] = arr[i][j] * arr_1[i][j]

for i in range(3) :
    for j in range(3) :
        print(arr_ans[i][j], end = " ")
    print()