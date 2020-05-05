from matplotlib import pyplot as plt
import numpy as np

dx = 1E-4
x_verdier = []
y_verdier = []
y_derevert = []


def deriver(f, x, dx):
    return (f(x+dx)-f(x))/dx


def f(x):
    return np.sin(x)


for i in np.arange(0, 2*np.pi, dx):
    x_verdier.append(i)
    y_verdier.append(f(i))
    y_derevert.append(deriver(f, i, dx))

plt.plot(x_verdier, y_verdier)
plt.plot(x_verdier, y_derevert)
plt.grid()
plt.show()
