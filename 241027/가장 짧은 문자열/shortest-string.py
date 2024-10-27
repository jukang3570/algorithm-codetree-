a = input()
b = input()
c = input()

max = 0
min = 21

if len(a) > max :
    max = len(a)
if len(b) > max :
    max = len(b)
if len(c) > max :
    max = len(c)

if len(a) < min :
    min = len(a)
if len(b) < min :
    min = len(b)
if len(c) < min :
    min = len(c)

print(max - min)