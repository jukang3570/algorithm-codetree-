def ans (a = 0,b = 0,c = 0) :
    min_ans = -101
    if a < b and a < c :
        min_ans = a
    elif b < a and b < c :
        min_ans = b
    elif c < a and c < b:
        min_ans = c
    return min_ans
a, b, c = map(int, input().split())
print(f'{ans(a,b,c)}')