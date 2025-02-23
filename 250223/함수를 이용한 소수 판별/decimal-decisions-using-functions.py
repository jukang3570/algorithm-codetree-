
a,b = map(int,input().split())
cnt = 0
def check(j) :
    if j %2 != 0 and j%3 != 0 and j != 1:
        return j
    else :
        return 0


for i in range(a,b+1) :
    cnt += check(i)
print(cnt)