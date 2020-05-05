from matplotlib import pyplot as plt
import numpy as np

dx = 1E-4
x_verdier = []
y_verdier = []
y_derevert = []


def f(x):
    return x**2+2*x-3


def deriver(x):
    return (f(x+dx)-f(x))/dx


for i in np.arange(-5, 3, dx):
    x_verdier.append(i)
    y_verdier.append(f(i))
    y_derevert.append(deriver(i))

plt.plot(x_verdier, y_verdier, label="f(x)")
plt.plot(x_verdier, y_derevert, label="f'(x)")
plt.grid()
plt.legend()
plt.show()
