n = int(input())

def factorial(n,cnt) :
    if n == 1 :
        print(cnt)
        return
    if n % 2 == 0 :
        factorial(n//2, cnt+1)
        return
    else :
        factorial(n // 3, cnt + 1)
        return
cnt = 0
ans = factorial(n, cnt)