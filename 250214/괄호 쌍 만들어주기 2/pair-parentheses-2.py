arr = list(input())
ans = 0
for i in range(len((arr))) :
    if arr[i] == '(' :
        for j in range(len(arr)-1, i, -1) :
            if arr[j] == ')' :
                ans += 1
                arr[i] = 'x'
                arr[j] = 'x'
                break
print(ans)