from matplotlib import pyplot as plt
import numpy as np

dx = 1E-1
Areal = 0
Def_v = 360 + dx
x = []
y = []


def v(t):
    return 20 + 30 * np.log((1/2) + (t/4)) - (t/4) + 2 * np.sin(t/(4*np.pi))


for t in np.arange(0, Def_v, dx):
    x.append(t)
    y.append(v(t))
    Areal += v(t + dx/2) * dx

print(
    "\nBilen har tilbakelagt en strekning på {:.3f} km.\n".format(Areal/3600))

plt.grid()
plt.bar(x, y)
plt.plot(x, y, "r")
plt.xlabel("Tid i sekunder")
plt.ylabel("Hastighet i km/h")
plt.xlim(-10, 370)
plt.ylim(0, 100)
plt.show()
