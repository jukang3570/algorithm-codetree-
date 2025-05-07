
n = list(map(int,input()))
num = 0
for i in range(len(n)) :
    num += n[len(n)-1-i] * (2**i)
num *= 17
arr = []
while num > 1 :
    arr.append(num % 2)
    num //= 2
if num != 0 : arr.append(1)
for cnt in arr[::-1] :
    print(cnt, end ='')