from matplotlib import pyplot as plt
import numpy as np

x_0 = 0
y_0 = 0
dx = 1E-1
x_max = 5 + dx
x = [x_0]
y = [y_0]
x_fasit = []
y_fasit = []


def next_y(x, yn, dx):
    return yn + (x + 2 * yn) * dx


def fasit(x):
    return -(1/2)*x+(1/4)*np.e**(2*x)-(1/4)


for i in np.arange(x_0+dx, x_max, dx):
    x.append(i)
    y.append(next_y(i, y[-1], dx))

for i in np.arange(0, 5+1E-5, 1E-5):
    x_fasit.append(i)
    y_fasit.append(fasit(i))

plt.plot(x, y, label="$\dfrac{dx}{dy} = x + 2y$"+", dx = {}".format(dx))
plt.plot(x_fasit, y_fasit,
         label="Fasit: $-\dfrac{1}{2}x+\dfrac{1}{4}e^{2x}-\dfrac{1}{4}$")
plt.grid()
plt.legend()
plt.show()
