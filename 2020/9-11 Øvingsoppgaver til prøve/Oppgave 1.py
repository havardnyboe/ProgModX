from matplotlib import pyplot as plt
import numpy as np

dt = 1E-3
t = []
x_verdier = []
y_verdier = []


def deriver(f, x, dx):
    return (f(x+dx)-f(x))/dx


def x(t):
    return 3*t**2 + 4*t


def y(t):
    return 5*t + 4


for i in np.arange(0, 30, dt):
    t.append(i)
    x_verdier.append(deriver(x, i, dt))
    y_verdier.append(deriver(y, i, dt))

print(x_verdier)

plt.plot(t, x_verdier, label="$x(t)$")
plt.plot(t, y_verdier, label="$y(t)$")
plt.grid()
plt.xlabel('Tid')
plt.ylabel('Fart')
plt.legend()
plt.show()
