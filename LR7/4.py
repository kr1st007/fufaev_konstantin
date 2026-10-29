def zd4():
    n = int(input())
    def sp1(n):
        lst = [i*11 for i in range(n)]
        print(lst)
    def sp2(n):   
        lst = [[i, i * 10] for i in range(1,n+1)]
        res = []
        for i in lst:
            for a in i:
                res.append(a)
        print(res)
    def sp4():
        lst = [i for i in range(1,21)]
        for i in lst:
            print(i)
            if i%2 == 0:
                lst[i-1] = lst[i-1] **2
            else:
                lst[i-1] += 2
        print(lst)
    sp4()

zd4()