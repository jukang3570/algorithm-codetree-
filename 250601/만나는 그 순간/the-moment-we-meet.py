n,m = map(int,input().split())

pos_a = []
pos_b = []
a_pos = 0
b_pos = 0
ans = 0


for s in range(1,n+1) :
    d,t = input().split()
    t = int(t)
    if d == 'R' :
        for j in range(t) :
            a_pos += 1
            pos_a.append(a_pos)
    elif d == 'L':
        for j in range(t) :
            a_pos -= 1
            pos_a.append(a_pos)

for s in range(1,m+1) :
    d, t = input().split()
    t = int(t)
    if d == 'R' :
        for j in range(t) :
            b_pos += 1
            pos_b.append(b_pos)
    elif d == 'L':
        for j in range(t) :
            b_pos -= 1
            pos_b.append(b_pos)

for i in range(len(pos_a)) :
    if pos_a[i] == pos_b[i] : 
        ans = i+1
        break
    
    
if ans != 0 : print(ans)
else : print(-1)