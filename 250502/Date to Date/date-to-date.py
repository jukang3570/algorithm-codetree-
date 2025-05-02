m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1_day = num_of_days[:m1]
m2_day = num_of_days[:m2]
day1 = sum(m1_day) + d1
day2 = sum(m2_day) + d2

print(abs(day1-day2)+1)