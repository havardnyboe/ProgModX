from matplotlib import pyplot as plt
import numpy as np

dx = 1E-2
tid = []
strekning = []
vel = []
aks = []


def deriver(f, x, dx):
    return (f(x+dx)-f(x))/dx


def s(t):
    return (-0.01*t**3) + (0.3*t**2) + (8*t)


def v(t):
    return deriver(s, t, dx)


def a(t):
    return deriver(v, t, dx)


for t in np.arange(0, 10 + dx, dx):
    tid.append(t)
    strekning.append(s(t))
    vel.append(v(t))
    aks.append(a(t))


plt.plot(tid, strekning, "r")
plt.plot(tid, vel, "g")
plt.plot(tid, aks, "b")
plt.grid()
plt.show()
