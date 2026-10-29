def zd3():
    s = input()
    lst = list(map(int,s.replace("[","").replace("]","").split(sep=",")))
    k1 = int(input())
    k2 = int(input())
    print(lst[k2:]+lst[k1:k2]+lst[:k1])

zd3()