
a, b = map(int,input().split())
n = int(input())
num = 0
ans = []

n = list(map(int,str(n)))
for i in range(len(n)) :
    num += (a**i) * n[len(n)-1-i]

while num > 0 :
    ans.append(num%b)
    num //= b
    
for n in ans[::-1] :
    print(n, end='')