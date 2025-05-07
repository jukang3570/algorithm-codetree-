
arr = list(map(int,input()))

num = 0
for i in range (len(arr)) :
    num += arr[len(arr)-1-i] * (2 ** i)

print(num)