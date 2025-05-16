n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
arr = []
for i in range(n) :
    arr.append(nums[i] + nums[(2*n)-1-i])
print(max(arr))
