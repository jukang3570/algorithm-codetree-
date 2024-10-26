a = int(input())
reverse_arr = []
cnt = 0

arr = list(map(int , input().split()))

for i in range (len(arr)-1 , -1, -1 ) :
    if arr[i] % 2 == 0 and arr[i] != 0 :
        reverse_arr.append(arr[i])


if len(reverse_arr) == 0 :
    print(0)
else :
    for elm in reverse_arr :
        print(elm,end = " ")