n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)
state = [ '0' for _ in range(10001)]
# Please write your code here.
pos = 5000
for i in range(n) :
    d = dir[i]
    y = x[i]
    if d == 'R' :
        for j in range(y) :
            state[pos] = 'B'
            pos += 1
        pos -= 1
    elif d == 'L' :
        for j in range(y) :
            state[pos] = 'W'
            pos -= 1
        pos += 1

print(state.count('W'), state.count('B'))
