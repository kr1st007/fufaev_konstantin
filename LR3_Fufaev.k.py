#Zadanie 1
# a = int(input())
# b = int(input())
# n = int(input())
# total_rub = n * a
# total_kop = n * b 
# if total_kop >= 100:
#     total_rub += total_kop//100
# print(total_rub,total_kop)


#Zadanie 2
# n = int(input())
# if n % 2 == 0:
#     print(True)
# else:
#     print(False)


#Zadanie 3
# n = int(input())
# k = int(input())
# print(k//n,k%n)


# Zadanie 4
# a = int(input())
# a = str(a)
# print(int(a[0])+int(a[1])+int(a[2]))
# print(int(a[0])*int(a[1])*int(a[2]))

 
#Zadanie 5
# a = int(input())
# b = int(input())
# c = int(input())
# sum = a + b + c
# res = sum//2
# if sum % 2 > 0:
#     res += 1
# print(res)


#Zadanie 6
# a = int(input())
# b = int(input())
# l = int(input())
# n = int(input())
# print((2 * n - 1) * a + 2 * (n - 1) * b + 2 * l)

#Zadanie 7
# h1 = int(input())
# m1 = int(input())
# s1 = int(input())
# h2 = int(input())
# m2 = int(input())
# s2 = int(input())
# totalS1 = h1 * 3600 + m1 *60 + s1
# totalS2 = h2 * 3600 + m2 *60 + s2
# totalS = totalS2 - totalS1
# totalh = totalS //3600
# totalm = (totalS % 3600)//60
# totalSec = (totalS % 3600) % 60
# print(f"{totalh}ч {totalm}м {totalSec}с")


#Zadanie 8*
# a = int(input())
# b = int(input())
# a = a + b 
# b = a  - b
# a = a - b
# print(a,b)