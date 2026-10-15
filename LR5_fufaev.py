#Zadanie 1

# n = int(input())
# def u(int):
#     for i in range(1,11):
#         print(f"1 x {n} = ", n*i)
# u(n)

#Zadanie 2

# def f(x):
#     print((x-3)/(x-5))
# for i in range(21):
#     x = i * 0.5
#     if x==5:
#         continue
#     if f(x) == None:
#         continue
#     print(f(x))

#Zadanie 3
# def b():
#     z = int(input())
#     cor = []
#     inpt = []
#     for i in range(1,z+1):
#         cor.append(i)
#     for i in range(z-1):
#         inpt.append(int(input()))
#     for i in range(len(cor)):
#         if inpt[i] != cor[i]:
#             print(cor[i])
#             break
# b()

#Zadanie 4
# def game():
#     a = int(input())
#     b = int(input())
#     cor = []
#     for i in range(a,b+1):
#         cor.append(i)
#     if  a > b:
#         for i in range(a,b-1,-1):
#             cor.append(i)
#     print(cor)
#     attempt = int(input())
#     while attempt not in cor:
#         print("Введите число")
#         attempt = int(input())
#     print("Число корректное")
# game()    

#Zadanie 5
# import random
# def game():
#     a = int(input())
#     b = int(input())
#     ans = random.randint(a,b)
#     attempt = int(input())
#     while attempt != ans:
#         if attempt > ans:
#             print("Перелет")
#             attempt = int(input())
#         if attempt < ans:
#             print("Недолет")
#             attempt = int(input())
#     print("Число угадано")
# game()

#Zadanie 6
# def zd6():
#     n = int(input())
#     minimum = 9999
#     count = 0
#     for i in range(n):
#         t = int(input())
#         if t < minimum:
#             minimum = t
#             count = 1
#         elif t == minimum:
#             count += 1
#     print(count)
# zd6()

#Zadanie 7
# a = int(input())
# b = int(input())
# def sp1(a,b):
#     while a != b:
#         if a > b:
#             a=  a-b
#         if b > a:
#             b = b -a     
#     return a
# print(sp1(a,b))
# def sp2(a,b):
#     if a ==b:
#         return a
#     if a > b:
#         return sp2(a-b,b)
#     else:
#         return sp2(a,b-a)
# print(sp2(a,b))

#Zadanie 8
# n = int(input())
# def sp1(n):
#     res = 1
#     for i in range(2,n+1):
#         res *= i
        
#     return res  
# def sp2(n):
#     res = 1
#     i = 1
#     while i <= n:
#         res *= i
#         i +=1
#     return res
# def sp3(n):
#     if n <= 1:
#         return 1
#     return n * sp3(n-1)
# print(sp3(n))

#Zadanie 9
# x = float(input())
# eps = float(input())
# def sp1(x,eps):
#     while True:
#         y1 = (y + x / y) / 2
#         if abs(y1 - y) < eps:
#             break
#         y = y1
#     return y1


# def sp2(x,eps,y=1):
#     y1 = (y + x /y)/2
#     if abs(y1-y) < eps:
#         return y1
#     return sp2(x,eps,y1)
# print(sp2(x,eps))

#Zadanie 10
# n = int(input())
# def dng(n):
#     bills = [64,32,16,8,4,2,1]
#     for i in bills:
#         cnt = n//i
#         if cnt > 0:
#             print(i,"-",cnt)
#         n = n % i
# dng(n)