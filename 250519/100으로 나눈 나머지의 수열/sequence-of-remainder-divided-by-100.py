N = int(input())

# Please write your code here.
def fun(N) :
    if N == 1 : return 2
    elif N == 2 : return 4
    else :
        return fun(N-1) * fun(N-2) % 100

ans = fun(N)
print(ans)