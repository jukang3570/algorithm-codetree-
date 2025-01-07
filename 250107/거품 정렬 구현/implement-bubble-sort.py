b = int(input())
a = list(map(int,input().split()))
for _ in range(len(a)) :
    for i in range(b-1) :
        if a[i] > a[i+1] :
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp

for i in range(len(a)) :
    print(f"{a[i]} ", end = '')