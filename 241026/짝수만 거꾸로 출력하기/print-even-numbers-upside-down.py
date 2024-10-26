a = int(input())
reverse_arr = []

arr = list(map(int, input().split()))

for i in range(a - 1, -1, -1):
    if arr[i] % 2 == 0:  # 짝수 조건만 확인
        reverse_arr.append(arr[i])

print(" ".join(map(str, reverse_arr)))