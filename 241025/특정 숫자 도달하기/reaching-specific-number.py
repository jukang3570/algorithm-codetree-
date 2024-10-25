arr = list(map(int, input().split()))
sum = 0
cnt = 0

for i in arr :
    if i < 250 :
        sum += i
        cnt+=1
    elif i >= 250 :
        break;

if sum == 0 :
    for i in arr :
        sum+= i
        cnt+=1

print(f"{sum} {(sum/cnt):.1f}")