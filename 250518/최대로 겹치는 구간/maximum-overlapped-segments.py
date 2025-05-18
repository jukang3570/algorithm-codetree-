n = int(input())
arr = [0 for _ in range(201)]  # -100 ~ 100 이므로 201칸

for _ in range(n):
    a, b = map(int, input().split())
    a += 100  # 전체 양수로 밀기
    b += 100
    for k in range(a, b):  # b는 포함 X
        arr[k] += 1

print(max(arr))