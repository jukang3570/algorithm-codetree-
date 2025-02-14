arr = list(input())
ans = 0
for i in range(len((arr))) :
    if arr[i] == '(' and arr[i+1] == '(':
        for j in range(len(arr)-1, i, -1) :
            if arr[j] == ')' and arr[j-1] == ')' :
                ans += 1
print(ans)