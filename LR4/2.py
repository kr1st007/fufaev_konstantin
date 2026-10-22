import math
a = int(input())
b = int(input())
c = int(input())
d = b**2 - 4 * a * c
if a == 0:
    if a == 0 and b == 0:
        print("Деление на ноль")
    else:
        print((-c/b))
elif d < 0:
    print("Корней нет")
elif d == 0 :
   print((-b/(2*a)))
elif d > 0:
    print(((-b + math.sqrt(d))/(2*a)))
    print(((-b - math.sqrt(d))/(2*a)))