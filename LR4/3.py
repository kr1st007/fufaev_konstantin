a = int(input())
b = int(input())
c = int(input())
if a + b > c and b + c > a and c+a > b:
    print("Да")
    if a == b == c :
        print("Равносторонний")
    elif a == b or b== c or a == c:
        print("Равнобедренный")
    else:
        print("Разностороний")
else:
    print("Нет")