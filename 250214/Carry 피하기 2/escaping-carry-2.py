n = int(input())
arr = []
ans = -1
for _ in range(n) :
    a = int(input())
    arr.append(a)
    
def carry_check(tmp1, tmp2) :
    while tmp1 > 0 or tmp2 > 0 :
        if (tmp1 % 10) + (tmp2 % 10) >= 10 :
            return True
        tmp1 //= 10
        tmp2 //= 10
    return False

for i in range(n-2) :
    for j in range(i+1, n-1) :
        check = carry_check(arr[i], arr[j])
        if check == False :
            for k in range(j+1, n) :
                check = carry_check(arr[i]+arr[j], arr[k])
                if check == False :
                    ans = max(ans, arr[i]+arr[j]+arr[k])

print(ans)