#Python 3.5.2
import random

x = 0
n = 0
for x in range(1000):
    random_num = 0
    i = 0
    a = 0
    b = 0
    c = 0
    while i==0:
        random_num = random.randint(1,100)
        if random_num <= 20:
            a += 1
        elif random_num <= 50:
            b += 1
        else:
            c += 1
        n += 1
        i = a*b*c
avg_n = n/1000
#print(n)
print(avg_n)
