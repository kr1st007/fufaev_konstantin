def zd1():
    import random
    n = int(input())
    def n1(n):
        lst = list(range(n))
        print(lst)
    def n2(n): 
        lst = [random.randint(1,100) for i in range(n)]
        print(lst)
    def n3(n):
        s = input()
        lst =list(map(int,s.split()))
        print(lst)
    n1(n)
    n2(n)
    n3(n)    
zd1()