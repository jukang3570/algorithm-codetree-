m1, d1, m2, d2 = map(int, input().split())
A = input()

# 2024년은 윤년이므로 2월은 29일까지
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 날짜를 일수로 변환
day1 = sum(num_of_days[:m1]) + d1
day2 = sum(num_of_days[:m2]) + d2

cnt = 0
for i in range(day1, day2 + 1):
    if day[i % 7] == A:
        cnt += 1

print(cnt)