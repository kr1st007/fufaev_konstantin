def game():
    a = int(input())
    b = int(input())
    print("Введите число")
    n = int(input())
    while n < a or n > b:
        print("Введите число")
        n = int(input())
    print("Число корректное")
game()    