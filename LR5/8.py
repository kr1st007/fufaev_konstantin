n = int(input())
def sp1(n):
    res = 1
    for i in range(2,n+1):
        res *= i
        
    return res  
def sp2(n):
    res = 1
    i = 1
    while i <= n:
        res *= i
        i +=1
    return res
def sp3(n):
    if n <= 1:
        return 1
    return n * sp3(n-1)
print(sp3(n))
