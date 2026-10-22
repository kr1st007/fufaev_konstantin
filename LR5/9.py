x = float(input())
eps = float(input())
y = 1
def sp1(x,eps,y):
    while True:
        y1 = (y + x / y) / 2
        if abs(y1 - y) < eps:
            break
        y = y1
    return y1

def sp2(x,eps,y=1):
    y1 = (y + x /y)/2
    if abs(y1-y) < eps:
        return y1
    return sp2(x,eps,y1)
print(sp1(x,eps,y))