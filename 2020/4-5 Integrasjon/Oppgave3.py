from matplotlib import pyplot as plt
import numpy as np

dx = 1E-2
Areal = 0
Def_T = 24+dx
x = []
y = []


def T(t):
    return 3.2*np.sin(0.3*t - 4.5) + 10.5


for i in np.arange(0, Def_T, dx):
    x.append(i)
    y.append(T(i))
    Areal += T(i+dx/2)*dx

print("Gjennomsnittstemperaturen denne dagen var {:.3f}C".format(Areal/Def_T))

plt.grid()
plt.bar(x, y, dx)
plt.plot(x, y, "r")
plt.show()
