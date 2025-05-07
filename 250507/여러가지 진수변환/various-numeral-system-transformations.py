
n, b = map(int, input().split())

# Please write your code here.
arr = []
while n > 1 :
    arr.append(n % b)
    n //= b
    
if n != 0 : arr.append(1)
for num in arr[::-1] : print(num, end = '')