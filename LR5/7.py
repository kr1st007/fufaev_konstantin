a = int(input())
b = int(input())
def sp1(a,b):
    while a != b:
        if a > b:
            a=  a-b
        if b > a:
            b = b -a     
    print(a)
sp1(a,b)
def sp2(a,b):
    if a ==b:
        return a
    if a > b:
        return sp2(a-b,b)
    else:
        return sp2(a,b-a)
print(sp2(a,b))