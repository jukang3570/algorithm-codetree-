arr = list(input())

def check_str(arr) :
    for i in range(len(arr)) :
        cnt = 0
        for j in range(len(arr)) :
            if i != j and arr[i] != arr[j] :
                cnt += 1
        if cnt <1 :
            return False
    return True
check = check_str(arr)

if check == True :
    print('Yes')
else : print('No')