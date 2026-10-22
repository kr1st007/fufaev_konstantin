
def dng():
    n = int(input())
    bills = [64,32,16,8,4,2,1]
    for i in bills:
        cnt = n//i
        if cnt > 0:
            print(i,"-",cnt)
        n = n % i
dng()