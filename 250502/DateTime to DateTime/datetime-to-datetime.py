a, b, c = map(int, input().split())

# Please write your code here.
day = (a - 11) * 24 * 60
hour = (b - 11) * 60
minute = c - 11
if a < 11 : print(-1)
elif a == 11 and b < 11 : print(-1)
elif a == 11 and b == 11 and c < 11 : print(-1)
else : print(day+hour+minute)