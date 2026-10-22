x = float(input())
y = float(input())
if (x**2 + y**2 <= 1) or (x <= 0 and y <=0 and y >= -x - 2 ):
    print("Да")
else:
    print("Нет")
