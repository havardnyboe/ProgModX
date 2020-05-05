from matplotlib import pyplot as plt
import numpy as np

dx = 1E-2
Areal = 0
x = []
y = []


def f(t):
    return -0.003*t**3 + 0.1*t**2 - 0.7*t + 2


for i in np.arange(0, 24+dx, dx):
    x.append(i)
    y.append(f(i))
    Areal += f(i+dx/2)*dx

print("Husstandens totalestrømforbruk denne dagen er {:.3f} kWh".format(Areal))

plt.grid()
plt.bar(x, y, dx)
plt.plot(x, y, "r")
plt.show()
