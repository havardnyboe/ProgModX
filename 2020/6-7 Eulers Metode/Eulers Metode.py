from matplotlib import pyplot as plt
import numpy as np

x_0 = 0.0
y_0 = 1.0
dt = 1E-1
t_max = 5 + dt
# liste for teoretiske verdier
x = []
y = []
# lister for Eulers verdier
xe = [x_0]
ye = [y_0]


def f(t):  # returnener den teoretiske verdien
    return np.e**t


def next_y(y, dt):  # returnerer en tilnærmingverdi via Eulers metode
    return y + y * dt


# fyller listene for teoretiske verdier
for t in np.arange(0, 5+1E-4, 1E-4):
    x.append(t)
    y.append(f(t))
for t in np.arange(x_0+dt, t_max, dt):
    xe.append(t)
    ye.append(next_y(ye[-1], dt))

plt.plot(x, y, label="f(x)=e$^x$")
plt.plot(xe, ye, label="f(x) med Eulers metode, når $\Delta t={}$".format(dt))
plt.grid()
plt.legend()
plt.show()
