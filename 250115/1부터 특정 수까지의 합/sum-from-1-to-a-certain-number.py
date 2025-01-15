def ans (n) :
    sum = 0
    for i in range(n) :
        sum += i+1
    return sum/10

n = int(input())
print(f'{int(ans(n))}')