
n = int(input())

def factorial(n) :
    if n <2:
        return 1

    return n * factorial(n-1)

print(factorial(n))