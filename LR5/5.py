import random
def game():
    a = int(input())
    b = int(input())
    ans = random.randint(a,b)
    attempt = int(input())
    while attempt != ans:
        if attempt > ans:
            print("Перелет")
            attempt = int(input())
        if attempt < ans:
            print("Недолет")
            attempt = int(input())
    print("Число угадано")
game()