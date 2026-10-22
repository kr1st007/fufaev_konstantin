def f(x):
    print((x-3)/(x-5))
for i in range(21):
    x = i * 0.5
    if x==5:
        continue
    if f(x) == None:
        continue
    print(f(x))