from matplotlib import pyplot as plt
import numpy as np

dx = 1E-2
x = []
y = []
A = 0
x_max = np.pi+dx


def f(x):
    return np.sin(x)


for i in np.arange(0, x_max, dx):
    x.append(i)
    y.append(f(i))
    A += f(i+dx/2)*dx

print('Arealet av flatestykket er {:.3f}'.format(A))

plt.bar(x, y, dx)
plt.plot(x, y, "r")
plt.grid()
plt.show()
