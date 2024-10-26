a = int(input())
arr = []

for i in range(a) :
    b = int(input())
    if b % 2 == 0 and b != 0:
        arr.append(a)

if len(arr) == 0 :
    print(0)
else :
    for elm in arr :
        print(elm,end = " ")