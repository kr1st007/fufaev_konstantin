def zd1():
    stroka = str(input())
    if len(stroka) < 5:
        print("Короткая")
    elif len(stroka) >= 5 and len(stroka) < 10:
        print("Средняя")
    else:
        print("Длинная")
zd1()