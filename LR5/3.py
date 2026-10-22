def b():
    z = int(input())
    s = 0
    for i in range(z-1):
        n = int(input())
        s += n
    total = z * (z + 1)//2
    print(total-s)
b()