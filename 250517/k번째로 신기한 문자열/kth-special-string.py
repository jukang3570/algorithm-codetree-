n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
filtered = [ s for s in str if s.startswith(t)]

filtered.sort()

print(filtered[k-1])