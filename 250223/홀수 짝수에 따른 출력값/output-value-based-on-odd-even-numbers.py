n = int(input())

def twin_num(n):
    if n == 2 :
        return 2
    return twin_num(n-2) + n

def three_num(n) :
    if n == 1 :
        return 1
    return three_num(n-2) + n

if n % 2 == 0 :
    print(twin_num(n))
else :
    print(three_num(n))