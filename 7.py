import random

a = random.randint(1, 100)
b = random.randint(1, 100)
while True:
    ans = int(input("%d+%d = ? : "%(a, b)))
    if ans != a+b:
        print("틀렸습니다.")
    else:
        print("맞았습니다.")
        break
