n = int(input())
A = list(map(int, input().split()))

# Write your code here!
max_value = 0
ans = []
for i in range(n) :
    distance = 0
    for j in range(n) :
        distance += A[j] * abs(i-j)
    ans.append(distance)
print(min(ans))