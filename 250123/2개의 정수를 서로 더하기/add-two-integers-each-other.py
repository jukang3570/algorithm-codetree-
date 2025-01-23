# 표준 입력처럼 처리
a, b = map(int,input().split())
a += b
b += a

print(f'{a} {b}')