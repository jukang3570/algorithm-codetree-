n = int(input())
arr = []

if n == 0:
    arr.append(0)
else:
    while n > 0:
        arr.append(n % 2)
        n //= 2

arr.reverse()
print(''.join(map(str, arr)))