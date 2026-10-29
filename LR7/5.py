def zd5():
    import random
    lst = [random.randint(1,100) for i in range(random.randint(1,10))]
    print(lst)
    print(min(lst),lst.index(min(lst)))
    print(max(lst),lst.index(max(lst)))
    print(len(lst))
    for i in range(len(lst)):
        print(lst[i], lst.count(lst[i]))

zd5()



