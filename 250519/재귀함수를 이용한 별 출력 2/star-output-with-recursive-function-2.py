n = int(input())

# Please write your code here.
def start_print(n) :
    if n == 0 : return
    print('* ' * n)
    start_print(n-1)



start_print(n)