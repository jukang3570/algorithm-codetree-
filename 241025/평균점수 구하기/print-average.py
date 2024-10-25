a = list(map(float,input().split()))
sum = 0

for i in a :
    sum += i

print(f"{sum/len(a):.1f}")