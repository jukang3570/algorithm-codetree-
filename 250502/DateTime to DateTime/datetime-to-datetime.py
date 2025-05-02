a, b, c = map(int, input().split())

# Please write your code here.
day = (a - 11) * 24 * 60
hour = (b - 11) * 60
minute = c - 11
print(day+hour+minute)