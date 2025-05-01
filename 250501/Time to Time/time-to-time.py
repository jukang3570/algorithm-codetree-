a, b, c, d = map(int, input().split())

# Please write your code here.
a_time = a * 60 + b
b_time = c * 60 + d
print(abs(b_time - a_time))