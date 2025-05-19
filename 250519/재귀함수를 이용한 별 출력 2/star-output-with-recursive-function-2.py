n = int(input())

# Please write your code here.
def start_print(n) :
    if n == 0 : return
    print('* ' * n)
    start_print(n-1)

def start_print_reverse(s, n) :
    if s > n : return
    print('* ' * s)
    start_print_reverse(s+1,n)

start_print(n)
start_print_reverse(1, n)