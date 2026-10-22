def zd6():
    n = int(input())
    minimum = 9999
    count = 0
    for i in range(n):
        t = int(input())
        if t < minimum:
            minimum = t
            count = 1
        elif t == minimum:
            count += 1
    print(count)
zd6()