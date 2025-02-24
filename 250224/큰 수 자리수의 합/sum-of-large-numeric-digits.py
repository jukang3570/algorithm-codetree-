arr = list(map(int,input().split()))
ans = 1

def solution(ans) :
    if ans < 10 :
        return ans
    return solution(ans//10) + ans % 10

for i in arr :
    ans *= i
print(solution(ans))