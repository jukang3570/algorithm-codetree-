n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def fun(num,step) :
    point = num * step
    flag = True
    for k in arr :
        if point % k != 0 : flag = False
    if flag == True : return point
    else : return fun(num, step+1)

ans = fun(max(arr),1)
print(ans)