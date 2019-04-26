#6
import random

a = [0,0,0,0,0,0]

for i in range(600):
    n = random.randint(1, 6)
    a[n-1] += 1

for k in range(1,7):
    print('주사위가 %d 인 경우는 %d 번'%(k, a[k-1]))
