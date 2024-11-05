def ans(n, m) :
    max = 0
    for i in range(1, n+1) :
        if n % i == 0 and m % i == 0 and i > max :
            max = i
    print(max)
n, m = map(int,input().split())
if n > m :
    ans(m, n)
else :
    ans(n, m)