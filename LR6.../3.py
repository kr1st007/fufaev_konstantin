def pal():
    n = str(input()).lower().replace(" ","")
    if n == n[::-1]:
        print("Да")
    else:
        print("Нет")

pal()