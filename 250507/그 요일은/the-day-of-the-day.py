m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
m1_day = num_of_days[:m1]
m2_day = num_of_days[:m2]
day1 = sum(m1_day) + d1
day2 = sum(m2_day) + d2
tmp = day2 - day1
cnt = 0
for i in range(tmp) :
    if day[i%7] == A : cnt += 1
    
print(cnt+1)