n = int(input())
arr = [0 for _ in range(201)]
state = ['0' for _ in range(201)]
pos = 0

for i in range(1,n+1) :
    a,b = input().split()
    a = int(a)
    if b == 'R' :
        for k in range(a) :
            if i % 2 == 1 and arr[pos] < 3 :
                arr[pos] += 1
                state[pos] = 'B'
            elif i % 2 == 0 and arr[pos] < 3 :
                arr[pos]+= 1
                sate[pos] = 'W'
            else :
                state[pos] = 'G'
        
        pos += 1
    elif b == 'L':
        for k in range(a) :
            if i % 2 == 1 and arr[pos] < 3 :
                arr[pos] += 1
                state[pos] = 'B'
            elif i % 2 == 0 and arr[pos] < 3 :
                arr[pos]+= 1
                sate[pos] = 'W'
            else :
                state[pos] = 'G'
        pos -= 1
print(state.count('B', state.count('W')), state.count('G'))