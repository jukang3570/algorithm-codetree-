product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class info :
    def __init__(self,product_name = "codetree",product_code = 50) :
        self.product_name = product_name
        self.product_code = product_code

ans = info()
print(f"product {ans.product_code} is {ans.product_name}")
ans_1 = info(product_name, product_code)
print(f"product {ans_1.product_code} is {ans_1.product_name}")