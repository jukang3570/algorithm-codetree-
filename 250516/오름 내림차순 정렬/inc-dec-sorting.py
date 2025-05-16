n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for num in nums :
    print(num, end = ' ')
print()
for num in nums[::-1] :
    print(num, end = ' ')