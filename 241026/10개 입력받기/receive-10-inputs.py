array = list(map(int, input().split()))
sum = 0
cnt = 0

for i in array :
    if i == 0 :
        break
    sum += i
    cnt += 1

print(f"{sum} {sum/cnt:.1f}")