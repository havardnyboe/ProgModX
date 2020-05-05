from matplotlib import pyplot as plt
import numpy as np

dx = 1E-4
x_verdier = []
y_derevert = []


def f(x):
    return x**3 - 2*x**2 - x + 5


def deriver(f, x, dx):
    return (f(x+dx)-f(x))/dx


for i in np.arange(0, 10, dx):
    x_verdier.append(i)
    y_derevert.append(deriver(f, i, dx))

plt.plot(x_verdier, y_derevert, label="$f'(x)=3x^2-4x-1$")
plt.grid()
plt.legend()
plt.show()
