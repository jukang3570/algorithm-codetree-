m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0
m1_day = num_of_days[m1-1] - d1

for i in range(m1,m2-2) : days += num_of_days[i]
print(m1_day + days + d2)