n,m = map(int,input().split())
first = 0
ans = 0
pos_a = 0
pos_b = 0
a = []
b =[]

for _ in range(n) :
    v,t = map(int,input().split())
    for t in range(t) :
        pos_a += v
        a.append(pos_a)

for _ in range(m) :
    v,t = map(int,input().split())
    for t in range(t) :
        pos_b += v
        b.append(pos_b)

if a[0] > b[0] : first = a
else : first = b

for i in range(1,len(a)) :
    if first == a :
        if b[i] > a[i] : 
            ans += 1
            first = b
    elif first == b :
        if a[i] > b[i] : 
            ans += 1
            first = a
print(ans)
        
