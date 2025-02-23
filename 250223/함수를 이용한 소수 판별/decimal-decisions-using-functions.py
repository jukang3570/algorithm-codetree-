a,b = map(int,input().split())
cnt = 0
def check(number) :
    if number == 1:
        return 0
    for i in range(2, number+1) :
        if i != number :
            if number % i == 0 :
                return 0
        else :
            return number


for i in range(a,b+1) :
    cnt += check(i)
print(cnt)