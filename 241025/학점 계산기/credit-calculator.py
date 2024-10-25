a = int(input())
arr = list(map(float,input().split()))
sum = 0

for i in arr :
    sum += i

avg = sum / a

print(f"{avg:.1f}")
if avg >= 4 :
    print("Good")
elif avg < 4 and avg >= 3 :
    print("Good")
else :
    print("Poor")