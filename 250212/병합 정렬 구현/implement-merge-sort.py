n = int(input())
arr = list(map(int, input().split()))


# Write your code here!
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    lower_arr = merge_sort(arr[mid:])
    upper_arr = merge_sort(arr[:mid])
    h = l = 0
    merge_arr = []

    while l < len(lower_arr) and h < len(upper_arr):
        if lower_arr[l] < upper_arr[h]:
            merge_arr.append(lower_arr[l])
            l += 1
        else:
            merge_arr.append(upper_arr[h])
            h += 1

    merge_arr += lower_arr[l:]
    merge_arr += upper_arr[h:]

    return merge_arr


arr = merge_sort(arr)
print(*arr)