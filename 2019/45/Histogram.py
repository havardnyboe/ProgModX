import matplotlib.pyplot as plt
import random

x = []

for kast in range(100000):
    t1 = random.randint(1,6)
    t2 = random.randint(1,6)
    x.append(t1+t2)

plt.hist(x, bins = 11)
plt.show()
