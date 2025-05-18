m1, d1, m2, d2 = map(int, input().split())
A = input()

# 2024년은 윤년이므로 2월 29일까지
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 날짜를 일수로 변환 (1월 1일 기준 총일수)
start = sum(num_of_days[:m1]) + d1
end = sum(num_of_days[:m2]) + d2

# 기준 요일 인덱스: m1월 d1일이 월요일 == 0번 인덱스
base_idx = days.index("Mon")

cnt = 0
for i in range(end - start + 1):  # (start일부터 end일까지)
    current_day = days[(base_idx + i) % 7]
    if current_day == A:
        cnt += 1

print(cnt)