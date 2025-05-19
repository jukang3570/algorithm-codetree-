N = int(input())

# Please write your code here.
def fun(N) :
    if N == 1 : return 1
    elif N == 2 : return 2
    else : return fun(N//3) + fun(N-1)
ans = fun(N)
print(ans)