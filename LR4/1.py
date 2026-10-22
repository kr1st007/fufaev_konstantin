a = int(input())
b = int(input())
c = int(input())
max = 0
min = 0
if a >= b  and a >= c:
    max += a
elif b >= a and b >=c:
    max += b
else:
    max += c

if a <= b  and a <= c:
    min += a
elif b <= a and b <= c:
    min += b
else:
    min += c
print(max,min)