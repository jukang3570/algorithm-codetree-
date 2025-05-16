n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class info :
    def __init__(self,name,phone,region) :
        self.name = name
        self.phone = phone
        self.region = region

pos = name.index(max(name))
ans = info(name[pos],street_address[pos], region[pos])
print(f"name {ans.name}")
print(f"addr {ans.phone}")
print(f"city {ans.region}")