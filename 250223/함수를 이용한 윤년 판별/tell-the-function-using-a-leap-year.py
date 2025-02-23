n = int(input())

def yun_year(n) :
    if n % 100 == 0 :
        if n % 400 != 0 :
            return 'false'
        else : 'true'

    if n % 4 == 0 :
        return 'true'
    else :
        return 'false'

print(yun_year(n))