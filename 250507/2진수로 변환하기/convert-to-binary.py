n = int(input())
arr = []
while n > 1 :
    arr.append(n%2)
    n //= 2
arr.append(1)
arr.reverse()
for num in arr :
    print(num,end = '')