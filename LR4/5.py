m = int(input())
d = int(input())
if m == 1:
    days = 31
    passed = 0
elif m == 2:
    days = 28
    passed = 31
elif m == 3:
    days = 31
    passed = 59
elif m ==4:
    days = 30
    passed = 90
elif m == 5:
    days = 31
    passed = 120
elif m == 6:
    days = 30
    passed = 151
elif m == 7:
    days = 31
    passed = 181
elif m == 8:
    days = 31
    passed = 212
elif m == 9:
    days = 30
    passed = 243
elif m == 10:
    days = 31
    passed = 273
elif m == 11:
    days = 30
    passed = 304
elif m== 12:
    days = 31
    passed = 334
else:
    days = 0
    passed = 0
if d < 1 or d > days or m < 1 or m > 12:
    print(-1)
else:
    print(365 - passed - d)