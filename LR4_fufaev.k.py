#Zadanie 1
# a = int(input())
# b = int(input())
# c = int(input())
# max = 0
# min = 0
# if a > b  and a > c:
#     max += a
# elif b > a and b >c:
#     max += b
# else:
#     max += c

# if a < b  and a < c:
#     min += a
# elif b < a and b < c:
#     min += b
# else:
#     min += c
# print(max,min)

#Zadanie 2
# import math
# a = int(input())
# b = int(input())
# c = int(input())
# d = b**2 - 4 * a * c
# if a == 0:
#     print(int(-c/b))
# elif d < 0:
#     print("Корней нет")
# elif d == 0 :
#    print(int(-b/(2*a)))
# elif d > 0:
#     print(int((-b + math.sqrt(d))/(2*a)))
#     print(int((-b - math.sqrt(d))/(2*a)))

#Zadanie 3
# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and b + c > a and c+a > b:
#     print("Да")
#     if a == b == c :
#         print("Равносторонний")
#     elif a == b or b== c or a == c:
#         print("Равнобедренный")
#     else:
#         print("Разностороний")
# else:
#     print("Нет")

#Zadanie 4
# x = float(input())
# y = float(input())
# if (x**2 + y**2 <= 1) or (x <= 0 and y <=0 and y >= -x - 2 ):
#     print("Да")
# else:
#     print("Нет")

#Zadanie 5 test
m = int(input())
d = int(input())
if d > 31 or m > 12 or m < 1 or d < 1:
    print(-1)
inputDays = m * 31


#Zadanie 6
# k = int(input())
# if k < 0:
#     print("Мы не находили грибы, а только теряли")
# elif k > 9 and k < 20:
#     print(f"Мы нашли в лесу {k} грибов ")
# elif k % 10 == 1 :
#     print(f"Мы нашли в лесу {k} гриб")
# elif k% 10 == 2 or k % 10 == 3 or k % 10 == 4 :
#     print(f"Мы нашли в лесу {k} грибa")
# else:
#     print(f"Мы нашли в лесу {k} грибов ")

#Zadanie 7
# t = int(input())
# v =0
# zel = []
# kr = []
# while v < 60:
    
#     for i in range(0,3):
#         zel.append(v)
#         v+=1
#     for i in range(4,6):
#         kr.append(v)
#         v+=1
# if t in zel:
#     print("Зеленый")
# if t in kr:
#     print("Красный")
# print(kr)



    

