n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

end_point = (arr[n-1][0], arr[n-1][1])
cnt = 0
ans = []
value = 0
state = [arr[0][0], arr[0][1]]

def distance(arr, cnt, value, state_value, state) :
    if cnt == n - 1:
        value += abs(state[0] - end_point[0]) + abs(state[1] - end_point[1])
        ans.append(value)
        return ans
    value += abs(state[0] - arr[state_value][0]) + abs(state[1] - arr[state_value][1])
    cnt += 1
    state = [arr[state_value][0], arr[state_value][1]]
    state_value += 1
    distance(arr, cnt, value, state_value, state)

for i in range(0,n-2) :
    state_value = i+1
    cnt = 2
    value = 0
    distance(arr, cnt, value, state_value, state)
    
print(min(ans))