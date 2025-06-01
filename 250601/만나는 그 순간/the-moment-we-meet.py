n,m = map(int,input().split())

pos_a = []
pos_b = []
a_pos = 1000
b_pos = 1000
ans = 0


for s in range(1,n+1) :
    d,t = input().split()
    t = int(t)
    if d == 'R' :
        a_pos += t
    elif d == 'L':
        a_pos -= t
    pos_a.append(a_pos)

for s in range(1,m+1) :
    d, t = input().split()
    t = int(t)
    if d == 'R' :
        b_pos += t
    elif d == 'L':
        b_pos -= t
    pos_b.append(b_pos)

for a in pos_a :
    for b in pos_b :
        if a == b :
            ans = a
        

if ans != 0 : print(ans- 999)
else : print(-1)