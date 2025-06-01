n,m = map(int,input().split())
first = 0
ans = -1
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


for i in range(1,len(a)) :
    if ans < 0 :
        if a[i] > b[i] : 
            first = a
            ans += 1
        elif b[i] > a[i] : 
            first = b
            ans += 1
    if first == a :
        if b[i] > a[i] : 
            ans += 1
            first = b
    elif first == b :
        if a[i] > b[i] : 
            ans += 1
            first = a
print(ans)
        
