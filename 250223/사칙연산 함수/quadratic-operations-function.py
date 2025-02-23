
arr = list(map(str,input().split()))

def plus(a,b) :
    return a+ b
def minus(a,b) :
    return a - b
def mul(a,b) :
    return a * b
def div(a,b) :
    return a // b

for i in range(1,2) :
    if arr[i] == '+' :
        print(arr[i-1], '+' , arr[i+1], '=', plus(int(arr[i-1]), int(arr[i+1])))
    elif arr[i] == '-' :
        print(arr[i-1], '-', arr[i+1], '=',  minus(int(arr[i-1]), int(arr[i+1])))
    elif arr[i] == '*' :
        print(arr[i-1], '*', arr[i+1], '=', mul(int(arr[i-1]), int(arr[i+1])))
    elif arr[i] == '/' :
        print(arr[i-1], '/', arr[i+1], '=', div(int(arr[i-1]), int(arr[i+1])))
    else : print('False')