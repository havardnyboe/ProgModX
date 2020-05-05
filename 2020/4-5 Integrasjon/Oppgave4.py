from matplotlib import pyplot as plt
import numpy as np

dx = 1E-2
Areal = 0
Def_v = 2250+dx
x_funk = []
x_bar = []
y_funk = []
y_bar = []


def v(t):
    return -4*(t/1000)**3 + t/50


for i in np.arange(0, Def_v, dx):
    x_funk.append(i)
    y_funk.append(v(i))
    Areal += v(i+dx/2)*dx

for i in np.arange(0, Def_v, 0.8):
    x_bar.append(i)
    y_bar.append(v(i))

print('Tilbakelagt strekning er {:.3f} km'.format(Areal/1000))

plt.grid()
plt.bar(x_bar, y_bar)
plt.plot(x_funk, y_funk, "r")
plt.show()
