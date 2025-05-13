n, m = map(int, input().split())

# Please write your code here.
a = min(n,m)
b = max(n,m)
for i in range(1,100) :
    tmp = b * i
    if tmp % a == 0 :
        print(tmp)
        break 