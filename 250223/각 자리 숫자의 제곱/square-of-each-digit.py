n = int(input())

def factorial(n) :
    if n < 10 :
        return n ** 2
    return factorial(n// 10) + ((n%10) ** 2)

n = factorial(n)
print(n)