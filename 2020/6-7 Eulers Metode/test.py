import random as r


def f(arr):
    a = []
    for n in arr:
        a.append(abs(n))
    a.sort()
    b = []
    for n in a:
        b.append(n**2)
    return b


liste = []
for i in range(2000):
    liste.append(r.randrange(-1000, 1000, 1))

print(f(liste))
