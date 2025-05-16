n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
t = list(t)
arr = []
for i in range(n) :
    tmp = list(str[i])
    flag = True
    for j in range(len(t)) :
        if t[j] != tmp[j] :
            flag = False
    if flag == True : arr.append(tmp)
arr.sort()
ans = ''.join(arr[k-1])
print(ans)