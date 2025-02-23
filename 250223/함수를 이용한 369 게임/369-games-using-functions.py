a,b = map(int,input().split())
cnt = 0
def check(j) :
    tmp = list(map(int,str(j)))
    for i in range(len(tmp)) :
        if tmp[i] == 3 or tmp[i] == 6 or tmp[i] == 9 or j % 3 == 0 :
            return 1
    return 0


for i in range(a,b+1) :
    cnt += check(i)
print(cnt)