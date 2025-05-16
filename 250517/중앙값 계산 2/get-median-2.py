n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

ans = []
for i in range(0,n,2) :
    if i == 0 :
        ans.append(arr[i])
    else :
        tmp = arr[:i+1:]
        tmp.sort()
        ans.append(tmp[i//2])
for num in ans :
    print(num, end = ' ')