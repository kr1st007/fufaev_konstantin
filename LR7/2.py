def zd2():
    res=0
    lst = list(range(10))
    print(lst)
    print(lst[0:3])
    print(lst[-1])
    print(lst[1:5])
    for i in range(1,10):
        res += lst[i]
    print(res)    
    
zd2()