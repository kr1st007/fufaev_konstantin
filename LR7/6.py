def zd6():
    s = input()
    s = s.split()
    s.sort()
    print("***".join(s))
    s.sort(reverse=True)
    print("+++".join(s))
zd6()