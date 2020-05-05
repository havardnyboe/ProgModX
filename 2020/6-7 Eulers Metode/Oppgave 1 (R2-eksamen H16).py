from matplotlib import pyplot as plt
import numpy as np
import math

dx = 1E-4
x0 = 2015
y0 = 5200000
x_max = x0 + 50 + dx
x = [x0]
y = [y0]


def next_y(yn, dx):
    return yn + (0.003*yn + 44000) * dx


for i in np.arange(x0+dx, x_max, dx):
    x.append(i)
    y.append(next_y(y[-1], dx))

passert_7mill_aar = 0
vekstfart = 0
for i in y:
    if i >= 7000000:
        passert_7mill_aar = math.floor(x[y.index(i)])
        vekstfart = math.floor(((next_y(i, dx)-i)/dx)*100)/100
        break


print('Folkertallet vil passere 7 millioner i år {}\nVekstfarten er da {}'.format(
    passert_7mill_aar, vekstfart))

plt.plot(x, y)
plt.grid()
plt.show()
