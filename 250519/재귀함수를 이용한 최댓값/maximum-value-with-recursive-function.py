n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def max_value(tmp, pos) :
    if pos == n : return tmp
    if tmp < arr[pos] : tmp = arr[pos]
    
    return max_value(tmp,pos+1)


ans = max_value(arr[0],1)
print(ans)