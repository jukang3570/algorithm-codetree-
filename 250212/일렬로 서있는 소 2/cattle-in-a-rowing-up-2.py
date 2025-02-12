N = int(input())
A = list(map(int, input().split()))

# Write your code here!
cnt = 0
for i in range(N) :
    state = A[i]
    for j in range(i+1, N) :
        if A[j] >= state :
            for k in range(j+1, N) :
                if A[k] >= A[j] :
                    cnt += 1

print(cnt)