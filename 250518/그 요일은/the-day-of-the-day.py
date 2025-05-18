m1, d1, m2, d2 = map(int, input().split())
A = input()

# 윤년 기준
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 기준일(1월 1일)을 0일로 보고 일수 변환
start = sum(num_of_days[:m1]) + d1 - 1
end = sum(num_of_days[:m2]) + d2 - 1

cnt = 0
for i in range(start, end + 1):
    if days[i % 7] == A:
        cnt += 1

print(cnt)