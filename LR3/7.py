h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
totalS1 = h1 * 3600 + m1 *60 + s1
totalS2 = h2 * 3600 + m2 *60 + s2
totalS = totalS2 - totalS1
totalh = totalS //3600
totalm = (totalS % 3600)//60
totalSec = (totalS % 3600) % 60
print(f"{totalh}ч {totalm}м {totalSec}с")